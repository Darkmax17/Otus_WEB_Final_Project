import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.title("Add product to cart and complete checkout")
@allure.feature("Cart & Checkout")
@allure.story("Полный путь от добавления товара до завершения заказа")
def test_add_to_cart_and_checkout(driver, base_url, creds):
    login = LoginPage(driver, base_url)
    inv = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step("Логин стандартным пользователем и загрузка страницы инвентаря"):
        login.load()
        login.login("standard_user", creds["standard_user"])
    with allure.step("Добавить товар 'Sauce Labs Backpack' в корзину"):
        inv.add_to_cart("Sauce Labs Backpack")
    with allure.step("Открыть корзину"):
        inv.open_cart()
    with allure.step("Нажать Checkout"):
        cart.proceed_to_checkout()
    with allure.step("Ввести данные покупателя и продолжить"):
        checkout.enter_info("John", "Doe", "12345")
    with allure.step("Завершить оформление заказа"):
        checkout.finish()
    with allure.step("Проверить успешное завершение заказа"):
        assert checkout.is_complete()