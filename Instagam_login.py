from vignesh import confidential_data
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests

class insta_login:
    url0 ="https://www.instagram.com/accounts/login/"
    url1="https://www.instagram.com/"
    driver = webdriver.Chrome()

    def first_page(self):
        insta_username = confidential_data().insta_username
        insta_password = confidential_data().insta_password
        self.driver.get(self.url0)
        time.sleep(5)
        fb_click = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[5]/button/span[2]')
        fb_click.click()
        insta_username1 = self.driver.find_element(by=By.XPATH, value='//*[@id="email"]')
        insta_password1 = self.driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
        insta_login = self.driver.find_element(by=By.XPATH, value='//*[@id="loginbutton"]')
        insta_username1.send_keys(insta_username)
        time.sleep(3)
        insta_password1.send_keys(insta_password)
        time.sleep(3)
        insta_login.click()
        time.sleep(10)
        not_now = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
        not_now.click()
        time.sleep(3)

    def insta_followers(self):
        self.first_page()
        profile_icon =self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img')
        profile_icon.click()
        time.sleep(3)
        profile_icon_menu = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div')
        profile_icon_menu.click()
        time.sleep(5)
        followers = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul')
        #following = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/ul/li[3]/a/div/span')
        return followers.text
        #return following.text



#print(insta_login().insta_followers())
