from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("[type=\"submit\"]")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value")
    y = math.log(abs(12*math.sin(int(x.text))))

    browser.find_element_by_id("answer").send_keys(str(y))

    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла