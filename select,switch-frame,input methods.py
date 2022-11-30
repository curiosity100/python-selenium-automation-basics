import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


def testcode():
    service=Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    url ='https://testautomationpractice.blogspot.com/'
    driver.get(url)
    driver.maximize_window()
    actions =ActionChains(driver)
    # entering search value
    driver.find_element(By.CSS_SELECTOR,"input#Wikipedia1_wikipedia-search-input").send_keys("just checking")

    # click search
    driver.find_element(By.CSS_SELECTOR, "input.wikipedia-search-button").click()

    # click alert
    driver.find_element(By.XPATH, "//button[contains(text(),'Click Me')]").click()
    time.sleep(5)

    # entering date
    driver.find_element(By.CSS_SELECTOR, "input#datepicker").click()

    # to go to march (today's date 18-7-2022)
    driver.find_element(By.CSS_SELECTOR,"a[data-handler='prev']").click()
    driver.find_element(By.CSS_SELECTOR, "a[data-handler='prev']").click()
    driver.find_element(By.CSS_SELECTOR, "a[data-handler='prev']").click()
    driver.find_element(By.CSS_SELECTOR, "a[data-handler='prev']").click()

    # to select (15-03-2022)
    driver.find_element(By.XPATH, "//td[@data-month='2']//a[contains(text(), '15')]").click()

    # to select a speed (faster)
    select =Select(driver.find_element(By.CSS_SELECTOR, "select#speed"))
    select.select_by_visible_text('Fast')

    # to select a file (pdf file)
    select = Select(driver.find_element(By.ID,"files"))
    select.select_by_value("2")

    # to select a number (3)
    select = Select(driver.find_element(By.ID, "number"))
    select.select_by_visible_text('3')

    # to select a product (iphone)
    select = Select(driver.find_element(By.ID, "products"))
    select.select_by_value("Apple")

    # to select a animal (avatar)
    select = Select(driver.find_element(By.ID, "animals"))
    select.select_by_value("avatar")

    # to enter age
    driver.find_element(By.ID, "age").send_keys("12")

    # to enter value to field1
    driver.find_element(By.CSS_SELECTOR, 'input#field1').clear()
    driver.find_element(By.CSS_SELECTOR, 'input#field1').send_keys("panther")

    # to slect in frames
    driver.switch_to.frame("frame-one1434677811")

    # to enter first & last name
    driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("someone")
    driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("noone")

    # phone number
    driver.find_element(By.CSS_SELECTOR, 'input#RESULT_TextField-3').send_keys('9876543210')

    # country
    driver.find_element(By.CSS_SELECTOR, 'input#RESULT_TextField-4').send_keys('India')

    # city
    driver.find_element(By.ID, 'RESULT_TextField-5').send_keys('Pink City')

    # email
    driver.find_element(By.ID, 'RESULT_TextField-6').send_keys('someone@gmail.com')

    # gender
    #driver.find_element(By.XPATH, "//label[@for='RESULT_RadioButton-7_0']").click()

    # executescript() method if click doesn't work
    element = driver.find_element(By.XPATH, "//label[@for='RESULT_RadioButton-7_0']")
    driver.execute_script("arguments[0].click();", element)

    #actions chains another mthod to click
    #actions.click(element).perform()

    # available days
    #driver.find_element(By.ID, 'RESULT_CheckBox-8_0').click()

    element= driver.find_element(By.ID, 'RESULT_CheckBox-8_0')
    driver.execute_script('arguments[0].click()', element)

    element = driver.find_element(By.ID, 'RESULT_CheckBox-8_6')
    driver.execute_script('arguments[0].click()', element)

    element = driver.find_element(By.XPATH, "//label[@for='RESULT_CheckBox-8_3']")
    driver.execute_script('arguments[0].click()', element)

    # timing (evening)
    select=Select(driver.find_element(By.ID,'RESULT_RadioButton-9'))
    select.select_by_value('Radio-2')
    time.sleep(5)

    # submit
    #driver.find_element(By.CSS_SELECTOR,'input#FSsubmit').click()
    #element = driver.find_element(By.CSS_SELECTOR, 'input#FSsubmit')
    #driver.execute_script('arguments[0].click()', element)

testcode()