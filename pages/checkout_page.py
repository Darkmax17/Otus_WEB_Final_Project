from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_info(self, first, last, postal):
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)
        self.driver.find_element(By.ID, "continue").click()

    def finish(self):
        self.driver.find_element(By.ID, "finish").click()

    def is_complete(self):
        try:
            header = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
            )
            return "THANK YOU FOR YOUR ORDER" in header.text
        except:
            return False