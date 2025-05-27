import pytest
from playwright.async_api import async_playwright
from pages.scroll_to_element_page import ScrolltoElementPage

pytestmark = pytest.mark.asyncio

async def test_scroll_to_element():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        
        scroll_to_element_page = ScrolltoElementPage(page)
        await scroll_to_element_page.open()
        await scroll_to_element_page.scroll_to_button()
        await scroll_to_element_page.click_button()

        await page.pause()

        await browser.close()
