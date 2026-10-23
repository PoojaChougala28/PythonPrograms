from playwright.sync_api import Page, expect
def test_dropdown(page : Page):
    page.goto("https://practice-automation.com/form-fields/")
    page.wait_for_timeout(300)
# Ways to select dopdown
#1. By label:
    page.locator("#automation").select_option("yes")
    page.wait_for_timeout(1000)
# 2 By value of the attribute:
    page.locator("#automation").select_option(value="undecided")
    page.wait_for_timeout(1000)
# 3 using index
    page.locator("#automation").select_option(index=2)
    page.wait_for_timeout(1000)
# get the count of all the dropdown elements
    dropdown=page.locator("#automation>option")
    expect(dropdown).to_have_count(4)
    optiontext=[text.strip() for text in dropdown.all_text_contents()]
    print(optiontext)
# to print in loop
    print("Looping droppdown values")
    for option in optiontext:
        print(option)

