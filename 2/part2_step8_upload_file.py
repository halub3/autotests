from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Alex")
    browser.find_element_by_name("lastname").send_keys("Su")
    browser.find_element_by_name("email").send_keys("a@a.ru")

    cur_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_path, "test.txt")
    browser.find_element_by_css_selector("[type=\"file\"]").send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла