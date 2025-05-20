import asyncio
import json
import os
from playwright.async_api import async_playwright

class ChatGPTClient:
    def __init__(self, session_file):
        self.session_file = session_file

    async def get_cookies(self):
        with open(self.session_file, "r", encoding="utf-8") as f:
            cookies = json.load(f)
        return cookies

    async def send_prompt(self, prompt):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            # Подгружаем cookies из файла auth.json
            cookies = await self.get_cookies()
            await context.add_cookies(cookies)
            page = await context.new_page()
            await page.goto("https://chat.openai.com/")
            await page.wait_for_selector("textarea", timeout=60000)
            await page.fill("textarea", prompt)
            await page.keyboard.press("Enter")
            await page.wait_for_timeout(15000)  # Ждём генерации (можно заменить на wait_for_selector ответа)
            elements = await page.query_selector_all("div.markdown")
            if elements:
                answer = await elements[-1].inner_text()
            else:
                answer = "Ответ не получен. Попробуйте еще раз."
            await browser.close()
        return answer
