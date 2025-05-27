from locators.scroll_to_element_locators import ScrolltoElementLocators
from actions.action_methods import ActionMethods

class ScrolltoElementPage:
    def __init__(self, page):
        self.page = page

    async def open(self):
        url = ScrolltoElementLocators.URL
        timeout = ScrolltoElementLocators.MAX_PAGE_LOAD_TIME * 1000
        width = ScrolltoElementLocators.WINDOW_WIDTH
        height = ScrolltoElementLocators.WINDOW_HEIGHT
        await ActionMethods.visit_url(self.page, url, timeout, width, height)

    async def scroll_to_button(self, timeout=None):
        locator_type = ScrolltoElementLocators.BUTTON_LOCATOR_TYPE
        locator_value = ScrolltoElementLocators.BUTTON_LOCATOR_VALUE
        timeout = timeout or ScrolltoElementLocators.BUTTON_TIMEOUT
        await ActionMethods.scroll_to_element(self.page, locator_type, locator_value)


    async def click_button(self, timeout=None):
        locator_type = ScrolltoElementLocators.BUTTON_LOCATOR_TYPE
        locator_value = ScrolltoElementLocators.BUTTON_LOCATOR_VALUE
        timeout = timeout or ScrolltoElementLocators.BUTTON_TIMEOUT
        await ActionMethods.click_element(self.page, locator_type, locator_value, timeout)
