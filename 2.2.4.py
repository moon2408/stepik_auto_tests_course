from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "[name=firstname]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name=lastname]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name=email]")
    input3.send_keys("ivan.petrov@hgg.com")
    file = browser.find_element(By.CSS_SELECTOR, "[name=file]")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'record.txt')
    print(file_path)
    file.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("window.scrollBy(0, 40);")
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