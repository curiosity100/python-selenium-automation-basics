from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


def testcode():
    url ='https://testautomationpractice.blogspot.com/'
    service =Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get(url)
    driver.maximize_window()

    #entering search value
    driver.find_element(By.CSS_SELECTOR, "input#Wikipedia1_wikipedia-search-input").send_keys("just checking")

    # click search
    driver.find_element(By.CSS_SELECTOR, "input.wikipedia-search-button").click()
    time.sleep(3)

    #click link
    driver.find_element(By.LINK_TEXT,'Just Checking: Scenes From the Life of an Obsessive-Compulsive').click()

    # switch to new window
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    print(driver.current_url)
    driver.find_element(By.XPATH, "//li[@class='toclevel-1 tocsection-2']").click()
    time.sleep(3)
    print(driver.current_url)

    #swith back to previous window
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)
    print(driver.current_url)
    print(len(driver.window_handles))

    # click alert
    driver.find_element(By.XPATH, "//button[contains(text(),'Click Me')]").click()
    time.sleep(2)
    print(Alert(driver).text)
    Alert(driver).accept()

    # draggable
    element = driver.find_element(By.ID,'draggable')
    element1 = driver.find_element(By.ID,'droppable')
    action = ActionChains(driver)
    action.drag_and_drop(element,element1).perform()
    time.sleep(3)


    #draggable example 2
    element= driver.find_element(By.XPATH,"//ul[@id='gallery']/li[1]")
    element1= driver.find_element(By.XPATH,"//ul[@id='gallery']/li[2]")
    drop = driver.find_element(By.ID,'trash')
    ## to scroll into view
    driver.execute_script("arguments[0].scrollIntoView()",element)

    action.drag_and_drop(element,drop).perform()
    action.drag_and_drop(element1,drop).perform()
    time.sleep(3)

    # recylce image
    element=driver.find_element(By.XPATH,"//div[@id='trash']//ul//li[2]//a")
    action.click(element).perform()
    time.sleep(3)

    #Scroll down
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(3)
    #scroll up
    driver.execute_script("window.scrollBy(0,-2000)","")
    time.sleep(3)
    element=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
    action.double_click(element).perform()
    #Slider
    driver.execute_script("window.scrollBy(0,1000)","")
    time.sleep(3)
    element=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
    action.drag_and_drop_by_offset(element,200,0).perform()

    #resizable
    element=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
    action.drag_and_drop_by_offset(element,100,200).perform()




testcode()
