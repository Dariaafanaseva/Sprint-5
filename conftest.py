from selenium import webdriver
import pytest
from faker import Faker
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

fake = Faker()
@pytest.fixture
def user_data():
    name = fake.name()
    email = fake.email()
    password = fake.password(length=7, special_chars=True)
    #print(f'Generated user_data: {name}, {email}, {password}')  # Для отладки
    return {
        'name': name,
        'email': email,
        'password': password,
    }