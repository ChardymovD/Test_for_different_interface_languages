import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_must_see_button_add_to_basket(browser, language):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    button_name = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").text
    assert button_name != "Add to basket", "По задумке ты должен выбрать другой язык:)"
