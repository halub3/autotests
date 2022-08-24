from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
try:
    # Указываем ссылку на страницу, которую тестируем
    # link = "http://suninjuly.github.io/registration2.html"
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    # Поиск элемента по плейсхолдеру
    first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your first name']")
    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your last name']")
    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your email']")
    # Заполняем поля
    first_name.send_keys("Ivan")
    last_name.send_keys("Petrov")
    email.send_keys("asd@asd.ru")
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
    # Если успешно – печатаем:
    print("Test Passed")



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()