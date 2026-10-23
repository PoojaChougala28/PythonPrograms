import time
from playwright.sync_api import Page,expect
import pytest

def test_demolocator(page:Page):
    page.goto("https://www.udemy.com/")
    # time.sleep(5) # seconds
    locator = page.get_by_alt_text("Nasdaq")
    expect(locator).to_be_visible()
    expect(page.get_by_text("Trending courses")).to_be_visible()

#get by role
    page.goto("https://www.udemy.com/join/passwordless-auth/?locale=en_US&next=https%3A%2F%2Fwww.udemy.com%2F&response_type=html&action=login&mode")
    expect(page.get_by_role("heading", name='Log in to continue your learning journey')).to_be_visible()
#get by label
    page.get_by_label("Email").fill("pooja@gmail.com")
    page.wait_for_timeout(2000)

#get by place holder
    #page.goto("https://www.udemy.com/join/passwordless-auth/?locale=en_US&next=https%3A%2F%2Fwww.udemy.com%2F&response_type=html&action=login&mode")
    page.get_by_placeholder("Search for anything").fill("Python automation")
    page.wait_for_timeout(2000)

# get by tittle
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")