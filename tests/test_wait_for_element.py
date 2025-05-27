import pytest
from playwright.async_api import async_playwright
from pages.wait_for_element_page import WaitforElementPage

pytestmark = pytest.mark.asyncio

async def test_wait_for_element():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        
        wait_for_element_page = WaitforElementPage(page)
        await wait_for_element_page.open()
        await wait_for_element_page.click_button()

        await page.pause()

        await browser.close()
