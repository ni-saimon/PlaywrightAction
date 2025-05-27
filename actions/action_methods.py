import asyncio
from playwright.async_api import TimeoutError

class ActionMethods:

    saved_values = {}

    @staticmethod
    def get_locator_by_input(locator_type, locator_value, index=None):
        locators = {
            "class": f".{locator_value}",
            "id": f"#{locator_value}",
            "text": f"text={locator_value}",
            "index": f"{locator_value} >> nth={index}" if index is not None else locator_value,
        }
        locator = locators.get(locator_type)
        if locator is None:
            raise ValueError(f"Invalid locator type: {locator_type}")
        return locator

    @staticmethod
    async def visit_url(page, url, timeout, window_width=None, window_height=None):
        try:
            if window_width and window_height:
                await page.set_viewport_size({"width": window_width, "height": window_height})
            
            await page.goto(url, timeout=timeout * 1000)
            return True
        
        except TimeoutError:
            print(f"❌ Page failed to load within {timeout} seconds.")
            return False

    @staticmethod
    async def input_text(page, locator_type, locator_value, text, timeout=None, index=None):
        locator_string = ActionMethods.get_locator_by_input(locator_type, locator_value, index)
        locator_obj = page.locator(locator_string)
        try:
            await locator_obj.wait_for(timeout=timeout * 1000 if timeout else 30000)
            await locator_obj.fill(text)
        except TimeoutError:
            print(f"❌ Failed to find input element '{locator_type}={locator_value}' within {timeout} seconds.")

    @staticmethod
    async def click_element(page, locator_type, locator_value, timeout=None, index=None):
        locator_string = ActionMethods.get_locator_by_input(locator_type, locator_value, index)
        locator_obj = page.locator(locator_string)
        try:
            await locator_obj.wait_for(timeout=timeout * 1000 if timeout else 30000)
            await locator_obj.click()
        except TimeoutError:
            print(f"❌ Failed to click element '{locator_type}={locator_value}' within {timeout} seconds.")

    @staticmethod
    async def validate_partial_text(page, locator_type, locator_value, expected_text, timeout=None, index=None):
        locator_string = ActionMethods.get_locator_by_input(locator_type, locator_value, index)
        locator_obj = page.locator(locator_string)
        try:
            await locator_obj.wait_for(timeout=timeout * 1000 if timeout else 30000)
            actual_text = await locator_obj.inner_text()
            if expected_text in actual_text:
                print(f"✅ Validation Passed: Found '{expected_text}' in '{actual_text}'")
                return True
            else:
                print(f"❌ Validation Failed: '{expected_text}' not found in '{actual_text}'")
                return False
        except TimeoutError:
            print(f"❌ Failed to find element '{locator_type}={locator_value}' within {timeout} seconds.")
            return False

    @staticmethod
    async def wait_for_time(time_in_seconds):
        await asyncio.sleep(time_in_seconds)

    @staticmethod
    async def save_text(page, locator_type, locator_value, key, timeout=None, index=None):
        locator_string = ActionMethods.get_locator_by_input(locator_type, locator_value, index)
        locator_obj = page.locator(locator_string)
        try:
            await locator_obj.wait_for(timeout=timeout * 1000 if timeout else 30000)
            text = await locator_obj.inner_text()
            ActionMethods.saved_values[key] = text
        except TimeoutError:
            print(f"❌ Failed to extract text from '{locator_type}={locator_value}' within {timeout} seconds.")

    @staticmethod
    def get_saved_text(key):
        return ActionMethods.saved_values.get(key, None)
    
    @staticmethod
    async def scroll_to_element(page, locator_type, locator_value, index=None, timeout=None):
        locator_string = ActionMethods.get_locator_by_input(locator_type, locator_value, index)
        locator_obj = page.locator(locator_string)
        try:
            await locator_obj.wait_for(timeout=timeout * 1000 if timeout else 30000)
            await locator_obj.scroll_into_view_if_needed()
        except TimeoutError:
            print(f"❌ Failed to scroll to element '{locator_type}={locator_value}' within {timeout} seconds.")

    @staticmethod
    async def select_dropdown_value(page, locator_type, locator_value, option_value, index=None, timeout=None):
        locator_string = ActionMethods.get_locator_by_input(locator_type, locator_value, index)
        locator_obj = page.locator(locator_string)
        try:
            await locator_obj.wait_for(timeout=timeout * 1000 if timeout else 30000)
            await locator_obj.select_option(option_value)
        except TimeoutError:
            print(f"❌ Failed to select '{option_value}' from dropdown '{locator_type}={locator_value}' within {timeout} seconds.")

    @staticmethod
    async def switch_to_iframe(page, locator_type, locator_value, index=None, timeout=None):
        locator_string = ActionMethods.get_locator_by_input(locator_type, locator_value, index)
        iframe_element = page.frame_locator(locator_string)
        try:
            await iframe_element.wait_for(timeout=timeout * 1000 if timeout else 30000)
            return iframe_element
        except TimeoutError:
            print(f"❌ Failed to switch to iFrame '{locator_type}={locator_value}' within {timeout} seconds.")
            return None