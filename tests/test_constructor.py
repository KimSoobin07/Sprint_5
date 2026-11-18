from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage
from urls import BASE_URL

class TestConstructor:
    def test_switch_to_sauces(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPage.SAUCES_TAB).click()
        
        # Проверяем, что таб Соусы получил класс активного таба
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.ACTIVE_SAUCES_TAB)
        )

    def test_switch_to_fillings(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPage.FILLINGS_TAB).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.ACTIVE_FILLINGS_TAB)
        )

    def test_switch_to_buns(self, driver):
        driver.get(BASE_URL)
        # Сначала переключаемся на Соусы, чтобы проверить смену класса обратно на Булки
        driver.find_element(*MainPage.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.ACTIVE_SAUCES_TAB)
        )
        
        driver.find_element(*MainPage.BUNS_TAB).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.ACTIVE_BUNS_TAB)
        )

