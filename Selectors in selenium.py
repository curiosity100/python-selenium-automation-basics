import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class selectors1:
    driver = webdriver.Firefox()
# using Id has a selector
    def use_id(self, url, link_id):
        try:
            self.driver.get(url)
            link_id = self.driver.find_element(by=By.ID, value=link_id)
            if link_id:
                time.sleep(3)
                link_id.click()
        except:
            print("ID not found !!!!")

# using Class has a selector
    def use_class(self, url, link_class):
        try:
            self.driver.get(url)
            link_class = self.driver.find_element(by=By.CLASS_NAME, value=link_class)
            if link_class:
                time.sleep(3)
                link_class.click()
        except:
            print("class not found")

# using X-path has a selector
    def use_xpath(self, url, link_xpath):
        try:
            self.driver.get(url)
            link_xpath = self.driver.find_element(by=By.XPATH, value=link_xpath)
            if link_xpath:
                time.sleep(3)
                link_xpath.click()
                print("xpath is present")
        except:
            print("X-path not found")


url_1 ="https://www.w3schools.com/"

url_2 ="https://www.guvi.in/"

id_1 = "w3loginbtn"

class_1 = "fa fa-logo"

x_path1 ="/html/body/main/section[4]/div/a"

selectors1().use_id(url_1, id_1)

#selectors1().use_class(url_1, class_1)

#selectors1().use_xpath(url_2, x_path1)