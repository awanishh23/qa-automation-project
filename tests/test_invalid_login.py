from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from testdata.test_data import invalid_username, invalid_password
import os

def test_invalid_login():

    driver = get_driver()

    login = LoginPage(driver)

    login.open()

    login.enter_username(invalid_username)
    login.enter_password(invalid_password)

    login.click_login()

    message = login.get_message()

    try:
        assert "Your username is invalid!" in message

    except AssertionError:

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        driver.save_screenshot("screenshots/invalid_login_failure.png")

        raise

    driver.quit()