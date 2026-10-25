from playwright.sync_api import Page

def test_booking(page: Page):
    page.goto("https://www.abhibus.com/")
    # page.wait_for_timeout(5000)
    # page.locator("input[placeholder='Leaving From']").fill("Pune")
    # page.locator("//input[@placeholder='Going To']").fill("Sankeshwar")
    # date=page.locator("input[placeholder$='Onward Journey Date']")
    # date.fill("25/10/2026")
    # page.wait_for_timeout(5000)
# for boarding point selection
    page.locator("input[placeholder='Leaving From']").click()
    city=page.locator("ul.collection.auto-complete-list li")
    count=city.count()
    print("Count of the boarding cities",count)
    for i in range(count):
        print(city.nth(i).get_attribute("data-id"))
    for j in range(count):
        boarding_city=city.nth(j).get_attribute("data-id")
        if boarding_city=="Bengaluru":
            city.nth(j).click()
            break
# for dropping point selection:
    drop=page.get_by_placeholder("Going To")
    drop.click()
    drop_city=page.locator("ul.collection.auto-complete-list.light li")
    count_drop=drop_city.count()
    print("count of dropping cities",count_drop)
    for a in range(count_drop):
        print(drop_city.nth(a).get_attribute("data-id"))
    for b in range(count_drop):
        city_check=drop_city.nth(b).get_attribute("data-id")
        if city_check=="Mangalore":
            drop_city.nth(b).click()
            break
    date_click=page.locator(".input-prefix.col.auto .text-neutral-500").nth(3)
    date_click.click()
    page.wait_for_timeout(5000)
    date=page.locator(".container.calendar a[data-date='31']")
    date.click()
    page.wait_for_timeout(5000)
    page.locator(".btn-search-wrapper.col.auto.m4").click()
    page.wait_for_timeout(5000)
#seat booking
    page.locator("#show-service-btn-4703311511").click()
    page.locator(".seat-v1-price.text-black").nth(1).click()
    page.wait_for_timeout(5000)
    page.locator(".radio-indicator").nth(1).click()
    page.wait_for_timeout(5000)
    page.locator("#place-192380-4703311511").click()
    page.wait_for_timeout(5000)




