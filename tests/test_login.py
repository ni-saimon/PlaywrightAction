import pytest
from playwright.async_api import async_playwright
from pages.login_page import LoginPage

pytestmark = pytest.mark.asyncio

async def test_login():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        
        login_page = LoginPage(page)
        await login_page.open()
        await login_page.input_username()
        await login_page.input_password()
        await login_page.click_login()
        await login_page.validate_partial_text()

        await page.pause()

        await browser.close()
