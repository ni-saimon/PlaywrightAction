from locators.dropdown_locators import DropdownPageLocators
from actions.action_methods import ActionMethods

class DropdownPage:
    def __init__(self, page):
        self.page = page

    async def open(self):
        url = DropdownPageLocators.URL
        timeout = DropdownPageLocators.MAX_PAGE_LOAD_TIME * 1000
        width = DropdownPageLocators.WINDOW_WIDTH
        height = DropdownPageLocators.WINDOW_HEIGHT
        await ActionMethods.visit_url(self.page, url, timeout, width, height)

    async def select_from_dropdown(self, text=None, timeout=None):
        locator_type = DropdownPageLocators.DROPDOWN_LOCATOR_TYPE
        locator_value = DropdownPageLocators.DROPDOWN_LOCATOR_VALUE
        dropdown_value = DropdownPageLocators.DROPDOWN_TEXT
        timeout = timeout or DropdownPageLocators.DROPDOWN_TIMEOUT
        await ActionMethods.select_dropdown_value(self.page, locator_type, locator_value, dropdown_value, timeout)

    async def validate_partial_text(self, text=None, timeout=None):
        locator_type = DropdownPageLocators.SUCCESS_LOCATOR_TYPE
        locator_value = DropdownPageLocators.SUCCESS_LOCATOR_VALUE
        text = DropdownPageLocators.DROPDOWN_TEXT
        timeout = timeout or DropdownPageLocators.SUCCESS_TIMEOUT
        await ActionMethods.validate_partial_text(self.page, locator_type, locator_value, text, timeout)
