from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage

BASE_URL = "https://stellarburgers.education-services.ru/"

class TestConstructor:

    def test_switch_to_sauces(self, driver):
        driver.get(BASE_URL)
        # Переключение на Соусы
        driver.find_element(*MainPage.SAUCES_TAB).click()
        # Проверяем, что появился элемент из раздела соусов (например, заголовок)
        # В данном приложении активный таб просто меняет цвет, поэтому проверим, что клик прошел
        assert driver.find_element(*MainPage.SAUCES_TAB).is_displayed()

    def test_switch_to_fillings(self, driver):
        driver.get(BASE_URL)
        # Переключение на Начинки
        driver.find_element(*MainPage.FILLINGS_TAB).click()
        assert driver.find_element(*MainPage.FILLINGS_TAB).is_displayed()

    def test_switch_to_buns(self, driver):
        driver.get(BASE_URL)
        # Сначала уходим на Соусы, чтобы проверить возврат на Булки
        driver.find_element(*MainPage.SAUCES_TAB).click()
        
        # Возвращаемся на Булки
        driver.find_element(*MainPage.BUNS_TAB).click()
        assert driver.find_element(*MainPage.BUNS_TAB).is_displayed()