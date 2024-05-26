import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def setting_browser():
    browser.config.window_height = 1024
    browser.config.window_width = 1280
    yield
    browser.quit()
