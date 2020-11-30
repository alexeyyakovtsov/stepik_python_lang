link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_catalogue_item(browser):
    browser.get(link)
    browser.implicitly_wait(4)
    btn = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert btn.is_displayed() == True, "the button did not find"
