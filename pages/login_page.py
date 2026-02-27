from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    success_message = (By.ID, "flash")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def enter_username(self, username):
        self.driver.find_element(*self.username).clear()
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_message(self):
        return self.driver.find_element(*self.success_message).text