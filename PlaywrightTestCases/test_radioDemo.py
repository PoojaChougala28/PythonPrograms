from playwright.sync_api import Page, expect

def test_radiobutton(page : Page):
    page.goto("https://practice-automation.com/form-fields/")
    name=page.locator("#name-input")
    expect(name).to_be_visible()
    expect(name).to_be_enabled()
    name.fill("John")
    password=page.locator("[type='password']")
    expect(password).to_be_enabled()
    password.fill("12345")
    # Radio button
    radio=page.locator("[name='fav_color'][value='Red']")
    expect(radio).not_to_be_checked()
    radio.check()
    expect(radio).to_be_checked()
    page.wait_for_timeout(1000)
    radio1=page.get_by_label("Blue")
    radio1.check()
    expect(radio).not_to_be_checked()
    expect(radio1).to_be_checked()
    page.wait_for_timeout(2000)

