from itertools import count

from playwright.sync_api import Page, expect
def test_flipkartDemo(page : Page):
    page.goto("https://www.flipkart.com/")
    page.locator(".b3wTlE").click()
    search=page.get_by_placeholder("Search for Products, Brands and More")
    search.first.fill("smart")
    page.wait_for_timeout(2000)
# find  the hidden elements
    smart=page.locator("ul>li")
    counts=smart.count()
    print("counts are:",counts)
    expect(smart).to_have_count(counts)
# 5th suggestion:
    if counts>5:
        print("5th innertest s:",smart.nth(5).inner_text())


# print the hidden elements
    for i in range(counts):
        print(smart.nth(i).inner_text())

    for i in range(counts):
        options=smart.nth(i).inner_text()
        if options=="smart tv":
            smart.nth(i).click()
            break


