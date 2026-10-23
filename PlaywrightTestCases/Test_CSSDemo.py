from playwright.sync_api import Page

def test_demo(page: Page):
    page.goto("https://demowebshop.tricentis.com/login")
    #tag and id
    page.locator("input#Email").fill("abc@demo.com")
    # tage and class
    page.locator("input.password").fill("12345")
    #tag and attribute
    page.locator("[value=true]").click()
    # tag and class,attribute
    page.locator("input.button-1[value='Register']").click()
    page.wait_for_timeout(5000)
