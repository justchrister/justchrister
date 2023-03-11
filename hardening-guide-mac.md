# Hardening guide for macbooks
Written by @justchrister on the 22.10.2020

## Displaying file extensions help you identify malicious file.

1. Open the terminal
2. run ```defaults write NSGlobalDomain AppleShowAllExtensions -bool true;```


## Enable encryption

 > System Preferences > security & privacy > filevault.

Then press Turn on FileVault.

## Disable Spotlight suggestions
Why? It turns off the sharing of search history with Apple, it also makes the search more user friendly, as it will only search your own macbook, rather than the internet.

1.  > System Preferences > Spotlight
2. Unselect ‘Allow Spotlight Suggestions in Look up’

## Lock mac after 1 minute of inactivity
1.  > System Preferences > Security & Privacy > General tab
2. Select ‘Require password 1 minute after sleep or screen saver begins’

## Require admin account to change settings
1.  > System Preferences > Security & Privacy > General tab 	> Advanced
2. Select ‘Require an administrator password to access system-wide preferences’

## Enable firewall
1.  > System Preferences > Security & Privacy > Firewall tab
2. Select ‘Turn On Firewall’
3. Then select ‘Firewall Options…’
4. and ensure these three tick boxes are checked:

## Limit ad tracking
1.  > System Preferences > Security & Privacy > Privacy tab
2. Look for the Advertising section
3. Select Limit Ad Tracking

## Stop sharing analatics with Apple
1.  > System Preferences > Security & Privacy > Privacy tab
2. Look for the Analytics & Improvements section
3. Unselect ‘Share Mac Analytics’
4. Unselect ‘Improve Siri & Dictation’

##
 > System Preferences > Security & Privacy > Privacy tab
Review the selections and remove any other apps you don’t want to have access to your disk.

##
 > System Preferences > Security & Privacy > Privacy tab
Select Location Services, then unselect ‘Enable Location Services’

## Turn on automatic updates
1.  > System Preferences > Software Update
2. Check you’re on the latest version of macOS, then select ‘Automatically keep my Mac up-to-date’.
3. Select Advanced
4. Choose automatically check for updates
4. Choose automatically download new updates when available
4. Choose automatically install app updates from the App Store
4. Choose automatically install macOS updates.
4. Choose automatically install system data files and security updates.


## Set DNS addresses to OpenDNS' ones 

1.  > System Preferences > Network > Advanced > DNS tab
2. Ensure ‘DNS Servers’ contains DNS servers for OpenDNS:
- 208.67.220.220
- 208.67.222.222
3. Remove any other addresses.

## Disable bluetooth
1.  > System Preferences > Bluetooth
2. Click ‘Turn Bluetooth Off’ when not in use.

## Turn off sharing options
1.  > System Preferences > Sharing
2. Unchecked these:
- Screen Sharing
- File Sharing
- Media Sharing
- Printer Sharing
- Remote Login
- Remote Managment
- Remote Apple Events
- Bluetooth Sharing
- Internet Sharing
- Content Caching

## Change computer name
1.  > System Preferences > Sharing
2. Change your Computer Name to something that isn’t directly identifiable.

## Disable wake for Wi-Fi network access
1.  > System Preferences > Energy Saver > Power Adapter tab
2. Unselect Wake for Wi-Fi network access.

## ??
1.  > System Preferences > Date & Time > Time Zone tab
2. Select ‘Set time zone automatically using current location’
