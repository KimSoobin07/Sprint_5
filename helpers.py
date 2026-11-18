import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPage, LoginPage, MainPage
from urls import BASE_URL, REGISTER_ENDPOINT, LOGIN_ENDPOINT

def generate_email():
    name = "test"
    surname = "testov"
    cohort = "1999"
    digits = f"{random.randint(100, 999)}"
    return f"{name}_{surname}_{cohort}_{digits}@yandex.ru"

def generate_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=8))

def register_user(driver, email, password, name="Иван"):
    """Регистрирует пользователя через UI."""
    driver.get(f"{BASE_URL}{REGISTER_ENDPOINT}")
    driver.find_element(*RegisterPage.NAME_INPUT).send_keys(name)
    driver.find_element(*RegisterPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPage.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPage.REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains(f"/{LOGIN_ENDPOINT}"))

def login_user(driver, email, password):
    """Логинит пользователя через UI."""
    driver.get(f"{BASE_URL}{LOGIN_ENDPOINT}")
    driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPage.ORDER_BUTTON)
    )