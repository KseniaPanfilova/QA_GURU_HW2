from selene import browser, be, have


def test_first(window_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_second(window_size):
    browser.element('[name="q"]').should(be.blank).type('kjdfngoi47u20').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу kjdfngoi47u20 ничего не найдено. '))
