from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element(By.ID, "treasure")

    x = int(chest.get_attribute("valuex"))
    y = math.log(abs(12*math.sin(x)))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(y))

    label1 = browser.find_element(By.ID, "robotCheckbox")
    label1.click()

    label2 = browser.find_element(By.ID, "robotsRule")
    label2.click()

    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла