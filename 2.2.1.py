import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def calc(x,y):
  return str(x+y)

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1 = int(num1_element.text)
    num2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    num2 = int(num2_element.text)
    result = calc(num1,num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)  # ищем элемент с текстом "Python"


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()