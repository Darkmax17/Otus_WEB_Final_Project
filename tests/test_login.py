import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.title("Smoke: успешный логин стандартным пользователем")
@allure.feature("Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver, base_url, creds):
    login = LoginPage(driver, base_url)
    inv = InventoryPage(driver)

    with allure.step("Открыть страницу логина"):
        login.load()
    with allure.step("Ввести валидные учетные данные"):
        login.login("standard_user", creds["standard_user"])
    with allure.step("Проверить, что инвентори загружен"):
        assert inv.is_loaded()