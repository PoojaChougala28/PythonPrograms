from playwright.sync_api import Page, expect

def test_checkbox(page : Page):
    page.goto("https://practice-automation.com/form-fields/")
    # select single check box:
    check1=page.locator("#drink1")
    expect(check1).not_to_be_checked()
    check1.check()
    expect(check1).to_be_checked()
    # count the number of checkboxes
    drink=["Water","Milk","Coffee","Wine","Ctrl-Alt-Delight"]
    drinks=[]
    for drink1 in drink:
        drink_label=page.get_by_label(drink1)
        drinks.append(drink_label)
    #     drinks.append(drink_label.get_attribute("value"))
    # print(drinks) to print all the element use this code
    print("Length of drinks is:",len(drinks))

    # drinks=[page.get_by_label(drink1)for drink1 in drink]
    # print("length of the checkbox is",len(drinks))

    # check the all check boxes at a time
    for drink2 in drinks:
        drink2.check()
        expect(drink2).to_be_checked()
    page.wait_for_timeout(2000)

    #unselect last 2 checkbox
    for drink3 in drinks[-2:]:
        drink3.uncheck()
        expect(drink3).not_to_be_checked()
    page.wait_for_timeout(2000)
    # now check the unchecked check boxes and un check the checked check boxes
    for drink4 in drinks:
        if drink4.is_checked():
            drink4.uncheck()
            expect(drink4).not_to_be_checked()
        else:
            drink4.check()
            expect(drink4).to_be_checked()
    page.wait_for_timeout(2000)
    #using index check the checkboxes
    index=[2,3,4]
    for i in index:
        drinks[i].check()
        expect(drinks[i]).to_be_checked()
    page.wait_for_timeout(2000)





