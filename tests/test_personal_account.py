from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login_user
from locators import MainPage, PersonalAccountPage
from urls import BASE_URL, PROFILE_ENDPOINT

class TestPersonalAccount:
    def test_go_to_personal_account(self, driver, registered_user):
        email, password = registered_user
        login_user(driver, email, password)
        driver.get(BASE_URL)
        
        driver.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(EC.url_contains(PROFILE_ENDPOINT))

    def test_go_from_account_to_constructor_button(self, driver, registered_user):
        email, password = registered_user
        login_user(driver, email, password)
        driver.get(f"{BASE_URL}{PROFILE_ENDPOINT}")
        
        driver.find_element(*MainPage.CONSTRUCTOR_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))

    def test_go_from_account_to_constructor_logo(self, driver, registered_user):
        email, password = registered_user
        login_user(driver, email, password)
        driver.get(f"{BASE_URL}{PROFILE_ENDPOINT}")
        
        driver.find_element(*MainPage.LOGO).click()
        
        assert WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))

    def test_logout(self, driver, registered_user):
        email, password = registered_user
        login_user(driver, email, password)
        driver.get(f"{BASE_URL}{PROFILE_ENDPOINT}")
        
        driver.find_element(*PersonalAccountPage.LOGOUT_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(EC.url_contains("/login"))