from selenium.webdriver.common.by import By

class MestoLocators:
    #главная страница
    #кнопка "войти в аккаунт":
    LOGIN_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button]']
    #кнопка "личный кабинет":
    ACCOUNT_BUTTON = [By.XPATH, '//*[@id="root"]/div/header/nav/a/p']
    #кнопка "Зарегистрироваться" на странице входа
    REGISTRATION_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a']



