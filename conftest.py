import pytest
from selene import browser


@pytest.fixture(scope="function")
def window_size():
    browser.config.window_height = 915
    browser.config.window_width = 412
    browser.open('https://google.com')

    yield

    browser.quit()