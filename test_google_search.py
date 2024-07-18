import pytest
from selene import browser, be, have


# @pytest.fixture()
# def window_size():
#     browser.config.window_height = 915
#     browser.config.window_width = 412
#
#     yield
#
#     browser.quit()


def test_first(window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

