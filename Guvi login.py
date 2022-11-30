from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

def guvilogin():
    service = Service(executable_path=GeckoDriverManager().install())
    driver1 = webdriver.Firefox(service=service)
    url = "https://www.guvi.in/sign-in"
    email = "example@gmail.com"
    password = "123$%^"
    email_input_id = "login_email"
    password_input_id ="login_password"
    login_id ="login_button"
    driver1.get(url)
    inputmail = driver1.find_element(by=By.ID, value=email_input_id)
    inputpassword = driver1.find_element(by=By.ID, value=password_input_id)
    login = driver1.find_element(by=By.ID, value=login_id)
    inputmail.send_keys(email)
    inputpassword.send_keys(password)
    login.click()

guvilogin()

