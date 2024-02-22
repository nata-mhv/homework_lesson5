import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_open():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 4.0

    yield

    browser.quit()