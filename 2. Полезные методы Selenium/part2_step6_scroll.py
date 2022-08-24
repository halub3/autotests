from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value")
    y = math.log(abs(12*math.sin(int(x.text))))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(y))

    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    label1 = browser.find_element(By.CSS_SELECTOR, "[for=\"robotCheckbox\"]")
    label1.click()

    label2 = browser.find_element(By.CSS_SELECTOR, "[for=\"robotsRule\"]")
    label2.click()

    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла