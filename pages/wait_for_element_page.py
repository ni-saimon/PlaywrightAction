from locators.wait_for_element_locators import WaitforElementPageLocators
from actions.action_methods import ActionMethods

class WaitforElementPage:
    def __init__(self, page):
        self.page = page

    async def open(self):
        url = WaitforElementPageLocators.URL
        timeout = WaitforElementPageLocators.MAX_PAGE_LOAD_TIME * 1000
        width = WaitforElementPageLocators.WINDOW_WIDTH
        height = WaitforElementPageLocators.WINDOW_HEIGHT
        await ActionMethods.visit_url(self.page, url, timeout, width, height)

    async def wait_for_button_to_appear(self, timeout=None):
        timeout = timeout or WaitforElementPageLocators.TIMEOUT
        await ActionMethods.wait_for_time(timeout)

    async def click_button(self, timeout=None):
        locator_type = WaitforElementPageLocators.BUTTON_LOCATOR_TYPE
        locator_value = WaitforElementPageLocators.BUTTON_LOCATOR_VALUE
        timeout = timeout or WaitforElementPageLocators.BUTTON_TIMEOUT
        await ActionMethods.click_element(self.page, locator_type, locator_value, timeout)
