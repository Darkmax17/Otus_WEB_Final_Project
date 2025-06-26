import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.title("Sorting: проверка сортировки по имени A-Z")
@allure.feature("Sorting")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.sorting
def test_sort_by_name_az(driver, base_url, creds):
    login = LoginPage(driver, base_url)
    inv = InventoryPage(driver)

    with allure.step("Логин и загрузка страницы инвентаря"):
        login.load()
        login.login("standard_user", creds["standard_user"])
    with allure.step("Выбрать сортировку Name (A to Z)"):
        inv.sort('Name (A to Z)')
    with allure.step("Считать имена товаров и проверить порядок"):
        names = inv.get_item_names()
        assert names == sorted(names)