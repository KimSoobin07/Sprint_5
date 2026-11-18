from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage, LoginPage, RegisterPage
from urls import BASE_URL, REGISTER_ENDPOINT, LOGIN_ENDPOINT

class TestLogin:
    def test_login_via_main_page_button(self, driver, registered_user):
        email, password = registered_user
        driver.get(BASE_URL)
        driver.find_element(*MainPage.LOGIN_ACCOUNT_BUTTON).click()
        
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        
        # Ожидание внутри ассерта
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.ORDER_BUTTON)
        )

    def test_login_via_personal_account_button(self, driver, registered_user):
        email, password = registered_user
        driver.get(BASE_URL)
        driver.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()
        
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.ORDER_BUTTON)
        )

    def test_login_via_register_form(self, driver, registered_user):
        email, password = registered_user
        driver.get(f"{BASE_URL}{REGISTER_ENDPOINT}")
        driver.find_element(*RegisterPage.LOGIN_LINK).click()
        
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.ORDER_BUTTON)
        )

    def test_login_via_recover_form(self, driver, registered_user):
        email, password = registered_user
        driver.get(f"{BASE_URL}{LOGIN_ENDPOINT}")
        driver.find_element(*LoginPage.RECOVER_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/forgot-password"))
        
        driver.find_element(*RegisterPage.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_contains(f"/{LOGIN_ENDPOINT}"))
        
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.ORDER_BUTTON)
        )

