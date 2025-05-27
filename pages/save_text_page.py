from locators.save_text_locators import SaveTextLocators
from actions.action_methods import ActionMethods

class SaveTextPage:
    def __init__(self, page):
        self.page = page

    async def open(self):
        url = SaveTextLocators.URL
        timeout = SaveTextLocators.MAX_PAGE_LOAD_TIME * 1000
        width = SaveTextLocators.WINDOW_WIDTH
        height = SaveTextLocators.WINDOW_HEIGHT
        await ActionMethods.visit_url(self.page, url, timeout, width, height)

    async def save_text(self, key, timeout=None):
        locator_type = SaveTextLocators.GET_TEXT_LOCATOR_TYPE
        locator_value = SaveTextLocators.GET_TEXT_LOCATOR_VALUE
        timeout = timeout or SaveTextLocators.GET_TEXT_TIMEOUT
        await ActionMethods.save_text(self.page, locator_type, locator_value, key, timeout)

    #async def get_saved_text():
        #saved_text = ActionMethods.get_saved_text("random_text_key")

    async def input_saved_text(self, text, timeout=None):
        locator_type = SaveTextLocators.INPUT_TEXT_LOCATOR_TYPE
        locator_value = SaveTextLocators.INPUT_TEXT_LOCATOR_VALUE
        timeout = timeout or SaveTextLocators.INPUT_TEXT_TIMEOUT
        await ActionMethods.input_text(self.page, locator_type, locator_value, text, timeout)

    async def click_verify_button(self, timeout=None):
        locator_type = SaveTextLocators.VERIFY_BUTTON_LOCATOR_TYPE
        locator_value = SaveTextLocators.VERIFY_BUTTON_LOCATOR_VALUE
        timeout = timeout or SaveTextLocators.VERIFY_BUTTON_TIMEOUT
        await ActionMethods.click_element(self.page, locator_type, locator_value, timeout)

