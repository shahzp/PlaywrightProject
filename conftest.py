import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope='function')
def login_creds(request):
    return request.param

#Register options
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chromium')

@pytest.fixture(scope='function')
def browser_instance(playwright:Playwright,request):
    browserName=request.config.getoption('--browser_name')
    browser=None
    if browserName=='chromium':
        browser=playwright.chromium.launch(headless=False)
    elif browserName=='firefox':
        browser=playwright.firefox.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    yield  page
    context.close()
    browser.close()
