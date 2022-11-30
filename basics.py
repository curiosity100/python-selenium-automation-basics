from selenium import webdriver

#from different browsers
from selenium.webdriver.firefox.service import service
from selenium.webdriver.firefox.options import Options


#from common
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#from support
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#from webdriver
from webdriver_manager.firefox import GeckoDriverManager