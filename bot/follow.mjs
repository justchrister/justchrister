import puppeteer from 'puppeteer';
import fs from 'fs';
import { config } from 'dotenv';

config(); // This loads the .env file

const scrape = async (username, org) => {
    const browser = await puppeteer.launch({ headless: 'false' }); // Set headless to false for debugging

    const page = await browser.newPage();
    const url = 'https://github.com/orgs/'+username+'/followers'
    const signinUrl = ''
    await page.goto(url);
    

    const selectors = await page.$$eval('.follow', buttons => 
        buttons.filter(button => button.innerHTML.includes('Follow') && !button.innerHTML.includes('Unfollow'))
              .map(button => button)
    );

    for (let button of selectors) {
        await page.evaluate((b) => b.click(), button);
    }
    await browser.close();
};

await scrape('supabase', true);
