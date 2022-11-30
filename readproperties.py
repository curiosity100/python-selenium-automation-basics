from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as firefoxservice
from selenium.webdriver.chrome.service import Service as chromeservice

# using jproperties
from jproperties import Properties
config = Properties()
with open(r'C:\Users\SoulHunter V2.0\Desktop\Work\Workspace\Python\Config.properties', "rb") as configfile:
    config.load(configfile)
#print(config.get("browser").data)



def testcode(browsertype):
    if browsertype == 'firefox':
        service = firefoxservice(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        url = "https://www.guvi.in/courses"
        driver.get(url)

    elif browsertype == 'chrome':
        service = chromeservice(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        url = "https://www.guvi.in/courses"
        driver.get(url)

testcode(config.get("browser1").data)