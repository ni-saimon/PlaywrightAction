class LoginPageLocators:

    URL = "https://demo.zeuz.ai/web/level/one/scenerios/login"
    MAX_PAGE_LOAD_TIME = 30
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1080

    USERNAME_LOCATOR_TYPE = "id"
    USERNAME_LOCATOR_VALUE = "username_id"
    USERNAME_TEXT = "zeuzTest"
    USERNAME_TIMEOUT = 15

    PASSWORD_LOCATOR_TYPE = "id"
    PASSWORD_LOCATOR_VALUE = "password_id"
    PASSWORD_TEXT = "zeuzPass"
    PASSWORD_TIMEOUT = 15

    SIGNIN_LOCATOR_TYPE = "id"
    SIGNIN_LOCATOR_VALUE = "signin_id"
    SIGNIN_TIMEOUT = 15

    SUCCESS_TEXT = "Login Successful"
    SUCCESS_LOCATOR_TYPE = "id"
    SUCCESS_LOCATOR_VALUE = "text_showing"
    SUCCESS_TIMEOUT = 5