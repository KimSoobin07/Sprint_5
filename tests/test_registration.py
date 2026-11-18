from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_email, generate_password
from locators import RegisterPage, LoginPage
from urls import BASE_URL, REGISTER_ENDPOINT

class TestRegistration:
    def test_successful_registration(self, driver):
        email = generate_email()
        password = generate_password()
        driver.get(f"{BASE_URL}{REGISTER_ENDPOINT}")
        
        driver.find_element(*RegisterPage.NAME_INPUT).send_keys("Иван")
        driver.find_element(*RegisterPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPage.REGISTER_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPage.LOGIN_BUTTON)
        )

    def test_registration_with_short_password_error(self, driver):
        email = generate_email()
        driver.get(f"{BASE_URL}{REGISTER_ENDPOINT}")
        
        driver.find_element(*RegisterPage.NAME_INPUT).send_keys("Иван")
        driver.find_element(*RegisterPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPage.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*RegisterPage.REGISTER_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPage.ERROR_PASSWORD)
        )

