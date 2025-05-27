from locators.iframe_locators import iFrameLocators
from actions.action_methods import ActionMethods

class iFramePage:
    def __init__(self, page):
        self.page = page

    async def open(self):
        url = iFrameLocators.URL
        timeout = iFrameLocators.MAX_PAGE_LOAD_TIME * 1000
        width = iFrameLocators.WINDOW_WIDTH
        height = iFrameLocators.WINDOW_HEIGHT
        await ActionMethods.visit_url(self.page, url, timeout, width, height)

    async def locate_iframe(self):
        locator_type = iFrameLocators.IFRAME_LOCATOR_TYPE
        locator_value = iFrameLocators.IFRAME_LOCATOR_VALUE

        iframe_locator = self.page.frame_locator(
            ActionMethods.get_locator_by_input(locator_type, locator_value)
        )
        return iframe_locator

    async def click_button_inside_iframe(self, timeout=None):
        iframe_locator = await self.locate_iframe()

        if iframe_locator:
            button_locator_type = iFrameLocators.BUTTON2_LOCATOR_TYPE
            button_locator_value = iFrameLocators.BUTTON2_LOCATOR_VALUE
            timeout = timeout or iFrameLocators.BUTTON2_TIMEOUT

            await iframe_locator.locator(
                ActionMethods.get_locator_by_input(button_locator_type, button_locator_value)
            ).click()
