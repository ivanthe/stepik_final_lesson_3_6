import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_is_add_to_basket_buttom_exist(browser):
    browser.get(link)
    time.sleep(30)

    assert browser.find_elements(By.XPATH, '//button[contains(@class, "btn-add-to-basket")]'), 'КНОПКИ "Добавить в корзину" НЕТ НА СТРАНИЦЕ'

    # на странице у нужной кропки есть уникальный класс, такой элемент для этой страницы встречается только один раз
    # исходим из того что такой элемент один на странице и для других не используется.
    # выбираем массив из таких элементов, чтобы проверить есть ли на странице. Если выполняется условие что массив не пустой, то тест проходит
    # Если массив пустой, то сработает Assert
    # .find_element не использую поскольку при отсутствии элеметна тест ложиться без Asserta с сообщением NoSuchElementException
