from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Процедура проверки ссылки (запустится 2 раза для разных ссылок)
def run_test(link):
    try: 
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.first_class > input.form-control")
        input1.send_keys("Su")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.second_class > input.form-control")
        input2.send_keys("Alex")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.third_class > input.form-control")
        input3.send_keys("Email")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

# Запускаем проверку двух ссылок
def main():
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    run_test(link1)
    run_test(link2)

if __name__ == '__main__': 
    main()
