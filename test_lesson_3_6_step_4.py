import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

numbers = [
    "236895","236896","236897","236898","236899", "236903", "236904", "236905"
]


def calc():
  return str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number',numbers)
def test_magic_message(browser,number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.implicitly_wait(5)
    browser.get(link)
    answer = calc()
    input1 = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view")
    input1.send_keys(str(answer))
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    assert "Correct!" == welcome_text

