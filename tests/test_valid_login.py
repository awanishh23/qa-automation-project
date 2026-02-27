from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from testdata.test_data import valid_username, valid_password

def test_valid_login():

    driver = get_driver()

    login = LoginPage(driver)

    login.open()

    login.enter_username(valid_username)
    login.enter_password(valid_password)

    login.click_login()

    message = login.get_message()

    assert "You logged into a secure area!" in message

    driver.quit()