import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import Select

def test_code(browsertype):

    if browsertype == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browsertype == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    driver.get("https://testautomationpractice.blogspot.com/")

    driver.switch_to.frame("frame-one1434677811")

    driver.find_element(By.ID,value="Email").clear()

    driver.find_element(By.CSS_SELECTOR, value="input#Password").clear()

    driver.find_element(By.ID,value="Email").send_keys("admin@yourstore.com")

    driver.find_element(By.CSS_SELECTOR, value="input#Password").send_keys("admin")

    driver.find_element(By.CSS_SELECTOR,value="button[class$='login-button']").click()

    time.sleep(3)

    driver.find_element(By.XPATH,value="//a[@href='#']//p[contains(text(),'Catalog')]").click()

    driver.find_element(By.XPATH,value="//a[@href='/Admin/Product/List']//p[contains(text(),'Products')]").click()

    select = Select(driver.find_element(By.ID,"SearchCategoryId"))

    select.select_by_value('5')

    time.sleep(5)

    select.select_by_index(3)

    time.sleep(5)

    select.select_by_visible_text("Apparel")

    for option in select.all_selected_options:
        print("Selected Option is :",option.text)

    for option in select.options:
        print(option.text)


   # select.deselect_by_visible_text("Apparel")

   # select.deselect_all()

test_code("firefox")
