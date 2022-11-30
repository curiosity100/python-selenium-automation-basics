from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def testcode():
    service = Service(executable_path=GeckoDriverManager().install())

    driver = webdriver.Firefox(service=service)
    url ="https://admin-demo.nopcommerce.com/"
    driver.get(url)
    driver.find_element(by=By.ID, value="Email").clear()
    driver.find_element(by=By.ID, value="Password").clear()
    # enter mail & password
    driver.find_element(by=By.ID, value="Email").send_keys("admin@yourstore.com")
    driver.find_element(by=By.ID, value="Password").send_keys("admin")
    driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']").click()
    time.sleep(15)
    # to click sales dropdown
    driver.find_element(by=By.XPATH, value="//a[@href='#']//p[contains(text(),'Sales')]").click()
    driver.find_element(by=By.XPATH, value="//a[@href='/Admin/Order/List']//p[contains(text(), 'Orders')]").click()
    time.sleep(15)
    # enter start and end date
    driver.find_element(by=By.ID, value='StartDate').send_keys("01-02-22")
    driver.find_element(by=By.ID, value='EndDate').send_keys("17-07-22")
    # to select warehouse details
    select = Select(driver.find_element(by=By.CSS_SELECTOR, value="select[data-val ='true']"))
    select.select_by_visible_text('Warehouse 1 (New York)')
    # product name
    driver.find_element(by=By.ID, value='search-product-name').send_keys("samsung galaxy")
    # to enter order status
    driver.find_element(by=By.CSS_SELECTOR, value="div[role='listbox']").click()
    driver.find_element(by=By.XPATH, value="//li[text()='Complete']").click()

    # enter payment status
    driver.find_element(By.XPATH, value="//input[@aria-labelledby='PaymentStatusIds_label']").click()
    driver.find_element(By.XPATH, value="//li[text()='Partially refunded']").click()

    # enter shipping status
    driver.find_element(By.XPATH, value="//input[@aria-labelledby='ShippingStatusIds_label']").click()
    driver.find_element(By.XPATH, value="//li[text()='Partially shipped']").click()

    #IF above method doesn't work use below (sometimes select works, Othertime it doesn't)

    # to enter order status(cancelled)
    # select = Select(driver.find_element(by=By.ID, value="OrderStatusIds"))
    # select.select_by_value("40")

    # enter payment status(partilley refunded)
    # select = Select(driver.find_element(by=By.ID, value="PaymentStatusIds"))
    # select.select_by_value('35')

    # enter shipping status(delivred)
    # select = Select(driver.find_element(by=By.ID, value="ShippingStatusIds"))
    # select.select_by_visible_text('Delivered')

    # enter ventor Id
    select = Select(driver.find_element(By.ID, value='VendorId'))
    select.select_by_value('2')
    # billing number
    driver.find_element(By.ID, value='BillingPhone').send_keys('9876543210')
    # email id
    driver.find_element(By.ID, value='BillingEmail').send_keys('qwerty@gmail.com')
    # billing last name
    driver.find_element(By.ID, value='BillingLastName').send_keys('qwerty')
    # select billing country
    select = Select(driver.find_element(By.ID, value='BillingCountryId'))
    select.select_by_index(9)
    #payment method
    select = Select(driver.find_element(By.ID, value='PaymentMethodSystemName'))
    select.select_by_value('Payments.CheckMoneyOrder')
    # order notes
    driver.find_element(By.ID, value='OrderNotes').send_keys('just careful')
    # click search
    driver.find_element(by=By.ID,value='search-orders').click()



testcode()
