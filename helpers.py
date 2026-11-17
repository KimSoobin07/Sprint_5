import random
import string

def generate_email():
    """Генерирует уникальный email в формате: имя_фамилия_номеркогорты_3цифры@домен"""
    name = "test"
    surname = "testov"
    cohort = "1999"
    digits = f"{random.randint(100, 999)}"
    return f"{name}_{surname}_{cohort}_{digits}@yandex.ru"

def generate_password():
    """Генерирует случайный пароль длиной 8 символов"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=8))