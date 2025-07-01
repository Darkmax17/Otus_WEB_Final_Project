from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def load(self):
        self.driver.get(self.base_url)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text

    def is_error_displayed(self, text):
        try:
            return text in self.get_error_message()
        except NoSuchElementException:
            return False