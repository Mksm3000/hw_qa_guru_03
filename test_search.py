from selene import browser, be, have


def test_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_wrong_request():
    # gaga - crazy or foolish
    gaga = '+_+_*!&@^#%$#@^!'
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type(gaga).press_enter()
    browser.element('[id="react-layout"]').should(have.text(gaga))
