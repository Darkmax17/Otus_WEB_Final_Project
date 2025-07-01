import pytest, json, os, allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Load credentials
creds_path = os.path.join(os.path.dirname(__file__), 'credentials.json')
with open(creds_path) as f:
    CREDENTIALS = json.load(f)


def pytest_addoption(parser):
    parser.addoption("--url", default="https://www.saucedemo.com", help="Base URL")
    parser.addoption("--browser", default="chrome", help="Browser: chrome, firefox, edge")
    parser.addoption("--headless", action="store_true", help="Headless mode")

@pytest.fixture(scope="session")
def creds():
    return CREDENTIALS

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    if browser == 'chrome':
        opts = Options()
        if headless: opts.add_argument('--headless')
        drv = webdriver.Chrome(options=opts)
    elif browser == 'firefox':
        from selenium.webdriver.firefox.options import Options as FF
        opts = FF()
        if headless: opts.add_argument('--headless')
        drv = webdriver.Firefox(options=opts)
    else:
        from selenium.webdriver.edge.options import Options as Ed
        opts = Ed()
        if headless: opts.add_argument('--headless')
        drv = webdriver.Edge(options=opts)
    drv.implicitly_wait(5)
    drv.maximize_window()
    yield drv
    drv.quit()

# Hook for screenshots on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            png = driver.get_screenshot_as_png()
            allure.attach(png, name='screenshot', attachment_type=allure.attachment_type.PNG)

@pytest.fixture(scope="function")
def base_url(request):
    return request.config.getoption("--url")