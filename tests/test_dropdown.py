import pytest
from playwright.async_api import async_playwright
from pages.dropdown_page import DropdownPage

pytestmark = pytest.mark.asyncio

async def test_dropdown():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        
        select_from_dropdown = DropdownPage(page)
        await select_from_dropdown.open()
        await select_from_dropdown.select_from_dropdown()
        await select_from_dropdown.validate_partial_text()

        await page.pause()

        await browser.close()
