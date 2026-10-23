from playwright.sync_api  import Page, expect
def test_assignment(page: Page):
    page.goto("https://demowebshop.tricentis.com/login")
    expect(page.locator("img[alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.goto("https://demowebshop.tricentis.com/desktops")
    count=page.locator("h2>a[href*='computer']").count()
    print("count of computer is:",count)
    product=page.locator(".product-item:first-child")
    print(product.first.inner_text())
    print(product.all_inner_texts())
    print(page.locator(".column.follow-us li:first-child").inner_text())
    print(page.locator(".column.follow-us li:last-child").inner_text())
    print(page.locator(".column.follow-us li:nth-child(3)").inner_text())


