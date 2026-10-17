import time
from playwright.sync_api import Page,expect
import pytest

def test_demolocator(page:Page):
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    # time.sleep(5) # seconds
    page.wait_for_timeout(5000)
    locator = page.get_by_alt_text("nopCommerce demo store")
    expect(locator).to_be_visible()

    #expect(page.get_by_text("Subscription")).to_be_visible()