import pytest
import allure
from pages.login_page import LoginPage

@allure.title("Негативный логин: неверные учетные данные и заблокированный пользователь")
@allure.feature("Login")
@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        ("wrong_user", "wrong_pass", "Username and password do not match"),
        ("locked_out_user", "secret_sauce",       "Sorry, this user has been locked out.")
    ]
)
def test_invalid_login(driver, base_url, creds, username, password, expected_message):
    login = LoginPage(driver, base_url)

    with allure.step(f"Открыть страницу логина и попытаться залогиниться как {username}"):
        login.load()
        login.login(username, password)
    with allure.step("Проверить сообщение об ошибке"):
        assert login.is_error_displayed(expected_message)