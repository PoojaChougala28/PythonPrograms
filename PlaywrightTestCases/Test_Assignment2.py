from playwright.sync_api import Page,expect
def test_demo(page : Page):
    page.goto("https://bstackdemo.com/")
    dropdown=page.locator(".sort select").select_option(value="lowestprice")
    page.wait_for_timeout(2000)
    title=page.locator(".shelf-item__title").all_text_contents()

    for i in title:
        print(i)
    price=page.locator(".val")
    print("price of the first element is:",price.first.inner_text())
    print("price of the first element is:",price.last.inner_text())


