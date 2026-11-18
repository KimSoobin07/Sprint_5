from selenium.webdriver.common.by import By

class MainPage:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    # Ищем ссылку, внутри которой есть текст "Личный Кабинет" (с заглавной К)
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[.//p[contains(text(), 'Личный Кабинет')]]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")            # Кнопка «Конструктор» в шапке
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип Stellar Burgers
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")          # Кнопка «Оформить заказ» (видна после входа)

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")                         # Таб «Булки»
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")                       # Таб «Соусы»
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")                   # Таб «Начинки»                  # Таб «Начинки»
    ACTIVE_BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Булки']]")
    ACTIVE_SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Соусы']]")
    ACTIVE_FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Начинки']]")

class RegisterPage:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")    # Поле «Имя»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле «Email»
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # Поле «Пароль»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")       # Кнопка «Зарегистрироваться»
    ERROR_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")            # Текст ошибки (пароль < 6 символов)
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")                              # Ссылка «Войти»

class LoginPage:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")   # Поле «Email»
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # Поле «Пароль»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")                          # Кнопка «Войти»
    RECOVER_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")                 # Ссылка «Восстановить пароль»

class PersonalAccountPage:
    # Кнопка "Выйти"
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    # "Профиль"
    PROFILE_HEADER = (By.XPATH, "//*[text()='Профиль']")