import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        await page.goto("https://projetogerar.000webhostapp.com/")
        print(await page.title())

        await page.fill("id=resp", "Olá, serve sim!")

        await page.click("//html/body/main/form/input[2]")

        codigo = await page.query_selector("//html/body/main/form/div/h6")
        print(await codigo.inner_text())

        pergunta = await page.query_selector("//html/body/main/form/div/h4")

        print(await pergunta.inner_text())

        await browser.close()

asyncio.run(main())