from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return "inventory" in self.driver.current_url

    def add_to_cart(self, product_name):
        btn = self.driver.find_element(
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        )
        btn.click()

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def sort(self, option_text):
        select_el = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        Select(select_el).select_by_visible_text(option_text)

    def get_item_names(self):
        elems = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [e.text for e in elems]