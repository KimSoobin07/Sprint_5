from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_email, generate_password
from locators import MainPage, RegisterPage, LoginPage, PersonalAccountPage

BASE_URL = "https://stellarburgers.education-services.ru/"

class TestPersonalAccount:
    
    def setup_method(self):
        self.email = generate_email()
        self.password = generate_password()
        
    def login_user(self, driver):
        # Регистрация
        driver.get(f"{BASE_URL}register")
        driver.find_element(*RegisterPage.NAME_INPUT).send_keys("Иван")
        driver.find_element(*RegisterPage.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(*RegisterPage.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*RegisterPage.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        
        # Логин
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPage.ORDER_BUTTON))

    def test_go_to_personal_account(self, driver):
        self.login_user(driver)
        driver.get(BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountPage.PROFILE_HEADER)
        )
        
        assert "/account/profile" in driver.current_url

    def test_go_to_personal_account(self, driver):
        self.login_user(driver)
        driver.get(BASE_URL)
        
        # Ждем, пока кнопка "Личный Кабинет" станет кликабельной
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем перехода на страницу профиля (URL содержит /account/profile)
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        assert "/account/profile" in driver.current_url

    def test_go_from_account_to_constructor_logo(self, driver):
        self.login_user(driver)
        driver.get(f"{BASE_URL}account/profile")
        
        # Переход в конструктор по логотипу
        driver.find_element(*MainPage.LOGO).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(BASE_URL))
        
        assert driver.current_url == BASE_URL

    def test_logout(self, driver):
        self.login_user(driver)
        driver.get(f"{BASE_URL}account/profile")
        
        # Ждем до 10 секунд, пока кнопка "Выйти" станет кликабельной
        logout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountPage.LOGOUT_BUTTON)
        )
        logout_btn.click()
        
        # Ждем перехода на страницу логина
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        
        assert "/login" in driver.current_url