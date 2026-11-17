import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Запускаем браузер Chrome
    browser = webdriver.Chrome()
    browser.maximize_window()  # Разворачиваем на весь экран
    browser.get("https://stellarburgers.education-services.ru/")  # Открываем сайт
    
    yield browser  # Отдаем браузер тесту. Всё, что ниже, выполнится ПОСЛЕ теста.
    
    browser.quit()  # Обязательно закрываем браузер