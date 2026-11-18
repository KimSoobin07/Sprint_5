import pytest
from selenium import webdriver
from helpers import generate_email, generate_password, register_user
from urls import BASE_URL

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(BASE_URL)
    yield browser
    browser.quit()

@pytest.fixture
def registered_user(driver):
    """Создает нового пользователя и возвращает его email и пароль."""
    email = generate_email()
    password = generate_password()
    register_user(driver, email, password)
    return email, password