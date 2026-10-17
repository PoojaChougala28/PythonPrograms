from playwright.sync_api import Page,expect
def test_link(page:Page):
    page.goto("https://www.youtube.com/")
    expect(page).to_have_url("https://www.youtube.com/")

def test_gettittle(page:Page):
    page.goto("https://www.amazon.in/ref=nav_logo")
    tittle=page.title()
    print("Tittle of the page is :",tittle)
    expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")