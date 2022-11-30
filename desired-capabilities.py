from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



def testcode():
    service =Service(executable_path=GeckoDriverManager().install())
    options = Options()
    options.page_load_strategy = 'normal'
    # desiredcapabilities =DesiredCapabilities.FIREFOX.copy()
    # desiredcapabilities['pageLoadStrategy']= "normal"
    driver = webdriver.Firefox(service=service,options=options)
    driver.get("https://www.zenclass.in/class")

    element = WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.ID,'')))

testcode()