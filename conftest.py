import pytest
from selene import browser


@pytest.fixture(scope="session")
def window_size():
    browser.config.window_height = 915
    browser.config.window_width = 412

    yield

    browser.quit()
