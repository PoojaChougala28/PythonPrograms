from playwright.sync_api import Page

def test_booking(page: Page):
    page.goto("https://www.abhibus.com/")
    page.wait_for_timeout(5000)
    page.locator("input[placeholder='Leaving From']").fill("Pune")
    page.locator("//input[@placeholder='Going To']").fill("Sankeshwar")
    date=page.locator("input[placeholder$='Onward Journey Date']")
    date.fill("25/10/2026")
    page.wait_for_timeout(5000)
