import asyncio
from playwright.async_api import async_playwright
import re

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        await page.goto("https://www.mercadolivre.com/jms/mlb/lgz/msl/login/H4sIAAAAAAAEAzXOwQrDIBAE0H-ZsyR3j_2RsDGrkWqVdVNbQv692NLjwPBmTqQS4mPRd2VY8Kum6KLCoCZSXyQvcYNFTjBoUfkf11EhoczK0mDPAQXebuyLDErlYBjQofviU-mwvykYhAKLXbU2O8-99ymzONpKik_hyZU8rTLDQDjEpiw8Hny9y8BT00WF3B3WU2p8fQC9dzgpxAAAAA/user")

        loop = True

        while (loop == True):
            try:
                await page.click('//*[@id="nav-header-menu"]/div/label/a')

                await page.goto("https://www.mercadolivre.com.br/perguntas/vendedor")

                loop = False

            except:
                loop = True

        try:
            number_question = await page.query_selector('//*[@id="page"]/div[4]/div[3]/div')
            number_questions = re.sub('[^0-9]', '', await number_question.inner_text())
        except:
            print("erro")

        print(number_questions)
        await browser.close()

asyncio.run(main())
