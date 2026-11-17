from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_email, generate_password
from locators import RegisterPage, LoginPage

class TestRegistration:
    
    def test_successful_registration(self, driver):
        email = generate_email()
        password = generate_password()
        
        # Переходим на страницу регистрации
        driver.get("https://stellarburgers.education-services.ru/register")
        
        # Находим поля по локаторам и вводим данные
        driver.find_element(*RegisterPage.NAME_INPUT).send_keys("Иван")
        driver.find_element(*RegisterPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPage.REGISTER_BUTTON).click()
        
        # Ждем до 5 секунд, пока появится кнопка «Войти» (признак того, что регистрация прошла)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPage.LOGIN_BUTTON)
        )
        
        # Проверяем, что URL изменился на страницу логина
        assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    def test_registration_with_short_password_error(self, driver):
        email = generate_email()
        short_password = "12345" # Меньше 6 символов
        
        driver.get("https://stellarburgers.education-services.ru/register")
        
        driver.find_element(*RegisterPage.NAME_INPUT).send_keys("Иван")
        driver.find_element(*RegisterPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPage.PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*RegisterPage.REGISTER_BUTTON).click()
        
        # Ждем появления ошибки
        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegisterPage.ERROR_PASSWORD)
        )
        
        # Проверяем текст ошибки
        assert error.text == "Некорректный пароль"