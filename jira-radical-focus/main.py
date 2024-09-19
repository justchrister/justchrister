import requests
from datetime import datetime, timedelta
import json
import openai

# Jira configuration
JIRA_URL = 'https://your-domain.atlassian.net'
API_TOKEN = 'your-api-token'
EMAIL = 'your-email'
BOARD_ID = 'your-board-id'

# Slack Webhook URL
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/your-webhook-url'

# OpenAI API Key
OPENAI_API_KEY = 'your-openai-api-key'

# Headers for the API requests
HEADERS = {
    'Authorization': f'Basic {requests.auth._basic_auth_str(EMAIL, API_TOKEN)}',
    'Content-Type': 'application/json'
}

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

def get_sprints(board_id):
    url = f'{JIRA_URL}/rest/agile/1.0/board/{board_id}/sprint'
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()['values']

def move_issues_to_sprint(issue_ids, target_sprint_id):
    url = f'{JIRA_URL}/rest/agile/1.0/sprint/{target_sprint_id}/issue'
    data = {
        'issues': issue_ids
    }
    response = requests.post(url, headers=HEADERS, data=json.dumps(data))
    response.raise_for_status()
    print(f'Moved issues to sprint {target_sprint_id}.')

def close_sprint(sprint_id):
    url = f'{JIRA_URL}/rest/agile/1.0/sprint/{sprint_id}'
    data = {
        'state': 'closed'
    }
    response = requests.put(url, headers=HEADERS, data=json.dumps(data))
    response.raise_for_status()
    print(f'Sprint {sprint_id} closed.')

def rename_sprint(sprint_id, new_name):
    url = f'{JIRA_URL}/rest/agile/1.0/sprint/{sprint_id}'
    data = {
        'name': new_name
    }
    response = requests.put(url, headers=HEADERS, data=json.dumps(data))
    response.raise_for_status()
    print(f'Sprint {sprint_id} renamed to {new_name}.')

def start_sprint(sprint_id):
    url = f'{JIRA_URL}/rest/agile/1.0/sprint/{sprint_id}'
    data = {
        'state': 'active'
    }
    response = requests.put(url, headers=HEADERS, data=json.dumps(data))
    response.raise_for_status()
    print(f'Sprint {sprint_id} started.')

def create_sprint(board_id, name, start_date, end_date):
    url = f'{JIRA_URL}/rest/agile/1.0/sprint'
    data = {
        'name': name,
        'originBoardId': board_id,
        'startDate': start_date,
        'endDate': end_date
    }
    response = requests.post(url, headers=HEADERS, data=json.dumps(data))
    response.raise_for_status()
    sprint_id = response.json()['id']
    print(f'Created sprint {sprint_id} with name {name}.')
    return sprint_id

def send_slack_message(resolved_issues, total_issues, summary):
    message = f"Great pulse! {resolved_issues} issues resolved out of {total_issues} registered.\n\nSprint Summary:\n{summary}"
    data = {
        'text': message
    }
    response = requests.post(SLACK_WEBHOOK_URL, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
    response.raise_for_status()
    print('Slack message sent.')

def transition_issue_to_done(issue_id):
    # Assuming 'Done' status has a transition ID of '31', this needs to be checked in Jira.
    transition_id = '31'
    url = f'{JIRA_URL}/rest/api/3/issue/{issue_id}/transitions'
    data = {
        'transition': {
            'id': transition_id
        }
    }
    response = requests.post(url, headers=HEADERS, data=json.dumps(data))
    if response.status_code == 204:
        print(f'Issue {issue_id} transitioned to Done.')
    else:
        print(f'Failed to transition issue {issue_id}: {response.content}')

def close_child_issues_if_parent_closed(issues):
    for issue in issues:
        if issue['fields'].get('issuetype', {}).get('name') == 'Epic' or issue['fields'].get('subtasks'):
            if issue['fields']['status']['name'] == 'Done':
                for subtask in issue['fields'].get('subtasks', []):
                    if subtask['fields']['status']['name'] != 'Done':
                        transition_issue_to_done(subtask['id'])

def summarize_sprint(issues):
    # Collect data for summary
    issue_descriptions = [issue['fields']['summary'] for issue in issues]
    # Construct prompt for OpenAI
    prompt = (
        "Summarize the following list of tasks completed during this sprint:\n\n" +
        "\n".join(f"- {desc}" for desc in issue_descriptions) +
        "\n\nProvide a brief summary of the main focus of this sprint."
    )
    
    # Get summary from OpenAI
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5
    )
    
    summary = response.choices[0].text.strip()
    return summary

def main():
    # Get sprints
    sprints = get_sprints(BOARD_ID)
    delta_sprint = next((sprint for sprint in sprints if sprint['name'] == 'Delta Sprint'), None)
    delta_sprint_next = next((sprint for sprint in sprints if sprint['name'] == 'Delta Sprint Next'), None)

    if not delta_sprint or not delta_sprint_next:
        print('Sprints not found.')
        return

    # Get issues in "Delta Sprint"
    url = f'{JIRA_URL}/rest/agile/1.0/sprint/{delta_sprint["id"]}/issue'
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    issues = response.json()['issues']
    total_issues = len(issues)
    resolved_issues = sum(1 for issue in issues if issue['fields']['status']['name'] == 'Done')

    # Close child issues if their parent is closed
    close_child_issues_if_parent_closed(issues)

    # Move open issues to "Delta Sprint Next"
    issue_ids = [issue['key'] for issue in issues if issue['fields']['status']['name'] != 'Done']
    if issue_ids:
        move_issues_to_sprint(issue_ids, delta_sprint_next['id'])

    # Close "Delta Sprint"
    close_sprint(delta_sprint['id'])

    # Rename "Delta Sprint Next" to "Delta Sprint"
    rename_sprint(delta_sprint_next['id'], 'Delta Sprint')

    # Start the "Delta Sprint"
    start_sprint(delta_sprint_next['id'])

    # Create "Delta Sprint Next" with next Monday and Sunday dates
    today = datetime.today()
    next_monday = today + timedelta(days=(7 - today.weekday()))
    next_sunday = next_monday + timedelta(days=6)
    create_sprint(
        BOARD_ID,
        'Delta Sprint Next',
        next_monday.strftime('%Y-%m-%dT%H:%M:%S.000%z'),
        next_sunday.strftime('%Y-%m-%dT%H:%M:%S.000%z')
    )

    # Get summary of the sprint using OpenAI
    sprint_summary = summarize_sprint(issues)

    # Send Slack message
    send_slack_message(resolved_issues, total_issues, sprint_summary)

if __name__ == '__main__':
    main()