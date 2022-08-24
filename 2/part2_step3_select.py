from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    val1 = int(browser.find_element_by_id("num1").text)
    val2 = int(browser.find_element_by_id("num2").text)

    answ = val1 + val2

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(answ))

    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла