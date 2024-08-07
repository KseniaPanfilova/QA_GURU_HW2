import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def window_size():
    browser.config.window_height = 915
    browser.config.window_width = 412
    browser.config.base_url = 'https://google.com'

    yield

    browser.quit()