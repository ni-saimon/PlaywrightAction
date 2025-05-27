from locators.login_page_locators import LoginPageLocators
from actions.action_methods import ActionMethods

class LoginPage:
    def __init__(self, page):
        self.page = page

    async def open(self):
        url = LoginPageLocators.URL
        timeout = LoginPageLocators.MAX_PAGE_LOAD_TIME * 1000
        width = LoginPageLocators.WINDOW_WIDTH
        height = LoginPageLocators.WINDOW_HEIGHT
        await ActionMethods.visit_url(self.page, url, timeout, width, height)

    async def input_username(self, text=None, timeout=None):
        locator_type = LoginPageLocators.USERNAME_LOCATOR_TYPE
        locator_value = LoginPageLocators.USERNAME_LOCATOR_VALUE
        text = text or LoginPageLocators.USERNAME_TEXT
        timeout = timeout or LoginPageLocators.USERNAME_TIMEOUT
        await ActionMethods.input_text(self.page, locator_type, locator_value, text, timeout)

    async def input_password(self, text=None, timeout=None):
        locator_type = LoginPageLocators.PASSWORD_LOCATOR_TYPE
        locator_value = LoginPageLocators.PASSWORD_LOCATOR_VALUE
        text = text or LoginPageLocators.PASSWORD_TEXT
        timeout = timeout or LoginPageLocators.PASSWORD_TIMEOUT
        await ActionMethods.input_text(self.page, locator_type, locator_value, text, timeout)

    async def click_login(self, timeout=None):
        locator_type = LoginPageLocators.SIGNIN_LOCATOR_TYPE
        locator_value = LoginPageLocators.SIGNIN_LOCATOR_VALUE
        timeout = timeout or LoginPageLocators.SIGNIN_TIMEOUT
        await ActionMethods.click_element(self.page, locator_type, locator_value, timeout)

    async def validate_partial_text(self, text=None, timeout=None):
        locator_type = LoginPageLocators.SUCCESS_LOCATOR_TYPE
        locator_value = LoginPageLocators.SUCCESS_LOCATOR_VALUE
        text = LoginPageLocators.SUCCESS_TEXT
        timeout = timeout or LoginPageLocators.SUCCESS_TIMEOUT
        await ActionMethods.validate_partial_text(self.page, locator_type, locator_value, text, timeout)
