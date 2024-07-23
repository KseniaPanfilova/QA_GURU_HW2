from selene import browser, be, have


def test_first():
    browser.open('/ncr')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_second():
    browser.open('/ncr')
    browser.element('[name="q"]').should(be.blank).type('kjdfngoi47u20').press_enter()
    browser.element('[id="botstuff"]').should(have.text('Your search - kjdfngoi47u20 - did not match any documents.'))
