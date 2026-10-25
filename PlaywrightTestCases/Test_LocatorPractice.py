from playwright.sync_api import Page, expect
def test_LocatorDemo(page : Page):
#get_t_alt_text
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    logo=page.get_by_alt_text("logo image")
    expect(logo).to_be_visible()
#get_by_text
    page.get_by_text("Locate elements by their text content.")
#get_by_role
    expect(page.get_by_role("heading", name="Username:")).to_be_visible()
#get_by_label






