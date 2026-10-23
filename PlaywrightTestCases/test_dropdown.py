from operator import index

from playwright.sync_api import Page,expect
def test_demo(page : Page):
    page .goto("https://testautomationpractice.blogspot.com/")
# # Input box
#     name=page.locator("#name")
#     name.fill("aaa")
#     expect(name).to_have_attribute("maxlength","15")
#     email=page.locator("#email")
#     email.fill("aa@demo.com")
#     email.get_attribute("maxlength")
#     phone=page.get_by_placeholder("Enter Phone")
#     phone.fill("12345678")
#     phone.input_value()
#     area=page.locator("#textarea")
#     area.fill("Pune")
#
# # Radio button:
#     radio=page.locator("#male")
#     radio.check()
#     expect(radio).to_be_checked()
# # check box:
# # select 1 check box:
#     checkbox=page.locator("[value=sunday]")
#     checkbox.check()
#     expect(checkbox).to_be_checked()
#     page.wait_for_timeout(2000)
# # Count of check boxes:
#     check1=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
#     check2=[]
#     for day in check1:
#         days=page.get_by_label(day)
#         check2.append(days)
#     print("Count of checklist are:",len(check2))
# # select all check boxes
#     for check3 in check2:
#         check3.check()
#         expect(check3).to_be_checked()
#     page.wait_for_timeout(1000)
# # select first 2 check box:
#     for check4 in check2[1:4:1]:
#         check4.uncheck()
#         expect(check4).not_to_be_checked()
#     page.wait_for_timeout(2000)
# # check the unchecked check boxes and uncheck the checked check boxes
#     for check5 in check2:
#         if check5.is_checked():
#             check5.uncheck()
#             expect(check5).not_to_be_checked()
#         else:
#             check5.check()
#             expect(check5).to_be_checked()
#     page.wait_for_timeout(2000)
# #check by index:
#     index=[1,2,3]
#     for i in index:
#         check2[i].check()
#         expect(check2[i]).to_be_checked()
#     page.wait_for_timeout(2000)
#multiple dropdown by label:
    page.locator("#colors").select_option(["Red","Blue"])
    page.wait_for_timeout(2000)
#select by value
    page.locator("#colors").select_option(value=["blue","yellow","red"])
    page.wait_for_timeout(2000)
#select by index
    page.locator("#colors").select_option(index=[1,3,6])
    page.wait_for_timeout(3000)
# print all the elements of the dropdown list
    dropdown=page.locator("#colors>option")
    dropdown1=[data.strip() for data in dropdown.all_text_contents()]
    print(dropdown1)
# to print list:
    for i in dropdown1:
        print(i)
#drop is sorted or not
    dropdown2=dropdown1.copy()
    sortlist=sorted(dropdown2)
    if(dropdown1==sortlist):
        print("Dropdown is sorted")
    else:
        print("Dropdow is not soeted")
