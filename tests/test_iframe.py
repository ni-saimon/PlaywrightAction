import pytest
from playwright.async_api import async_playwright
from pages.iframe_page import iFramePage

pytestmark = pytest.mark.asyncio

async def test_iframe():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        
        iframe_page = iFramePage(page)
        await iframe_page.open()
        await iframe_page.click_button_inside_iframe()

        await page.pause()

        await browser.close()
