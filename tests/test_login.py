from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_email, generate_password
from locators import MainPage, RegisterPage, LoginPage, PersonalAccountPage

BASE_URL = "https://stellarburgers.education-services.ru/"

class TestLogin:
    
    def setup_method(self):
        # Регистрируем пользователя перед каждым тестом, чтобы было с кем входить
        self.email = generate_email()
        self.password = generate_password()
        
    def register_user(self, driver):
        driver.get(f"{BASE_URL}register")
        driver.find_element(*RegisterPage.NAME_INPUT).send_keys("Иван")
        driver.find_element(*RegisterPage.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(*RegisterPage.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*RegisterPage.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))

    def test_login_via_main_page_button(self, driver):
        self.register_user(driver)
        driver.get(BASE_URL)
        
        # Способ 1: Вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*MainPage.LOGIN_ACCOUNT_BUTTON).click()
        
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        
        # Проверяем, что вошли (появилась кнопка Оформить заказ)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPage.ORDER_BUTTON))

    def test_login_via_personal_account_button(self, driver):
        self.register_user(driver)
        driver.get(BASE_URL)
        
        # Способ 2: Вход через кнопку «Личный кабинет»
        driver.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()
        
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPage.ORDER_BUTTON))

    def test_login_via_register_form(self, driver):
        self.register_user(driver)
        # Мы уже на странице логина после регистрации, поэтому просто входим
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPage.ORDER_BUTTON))

    def test_login_via_recover_form(self, driver):
        self.register_user(driver)
        driver.get(f"{BASE_URL}login")
        
        # Способ 4: Вход через кнопку на форме восстановления пароля
        driver.find_element(*LoginPage.RECOVER_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/forgot-password"))
        
        driver.find_element(*RegisterPage.LOGIN_LINK).click() # Ссылка "Войти" на странице восстановления
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPage.ORDER_BUTTON))