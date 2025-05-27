from playwright.async_api import async_playwright
from pages.save_text_page import SaveTextPage
from actions.action_methods import ActionMethods  

async def test_save_text():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        
        save_text_page = SaveTextPage(page)
        await save_text_page.open()
        await save_text_page.save_text("random_text_key", 10)
        saved_text = ActionMethods.get_saved_text("random_text_key")
        await save_text_page.input_saved_text(saved_text)
        await save_text_page.click_verify_button()

        await page.pause()
        await browser.close()
