from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as firefoxservice
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.common.by import By
import time

def testcode(browsertype):
    if browsertype == 'firefox':
        service = firefoxservice(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        url = "https://www.guvi.in/courses"
        driver.get(url)
        time.sleep(3)
        signup = driver.find_element(by=By.XPATH, value='/html/body/header/nav/div[2]/ul/li[2]/a')
        signup.click()
        time.sleep(3)
        if driver.current_url =='https://www.guvi.in/register':
            driver.back()
        else:
            driver.refresh()
        time.sleep(3)
        if driver.title == "GUVI | courses":
            print('code worked')
        else:
            print('try again')
    elif browsertype == 'chrome':
        service = chromeservice(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        url = "https://www.guvi.in/courses"
        driver.get(url)
        time.sleep(3)
        signup = driver.find_element(by=By.XPATH, value='/html/body/header/nav/div[2]/ul/li[2]/a')
        signup.click()
        time.sleep(3)
        if driver.current_url == 'https://www.guvi.in/register':
            driver.back()
        else:
            driver.refresh()
        time.sleep(3)
        if driver.title == "GUVI | courses":
            print('code worked')
        else:
            print('try again')




#testcode("chrome")
testcode("firefox")