import pytest
import allure
from pages.login_page import LoginPage

@allure.title("Role tests: проверка доступа для разных пользователей")
@allure.feature("Login Roles")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.roles
@pytest.mark.parametrize('user', [
    'standard_user', 'locked_out_user',
    'problem_user', 'performance_glitch_user',
    'error_user', 'visual_user'
])
def test_user_roles(driver, base_url, creds, user):
    login = LoginPage(driver, base_url)

    with allure.step(f"Попытка входа как '{user}'"):
        login.load()
        login.login(user, creds[user])

    if user == 'locked_out_user':
        with allure.step("Проверить сообщение о заблокированном пользователе"):
            assert login.is_error_displayed('Sorry, this user has been locked out.')
    else:
        with allure.step("Проверить, что перешли на страницу инвентаря"):
            assert 'inventory' in login.driver.current_url