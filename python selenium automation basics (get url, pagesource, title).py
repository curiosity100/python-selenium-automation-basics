from selenium import webdriver

class browser:
    driver = webdriver.Firefox()
    # to fetch the ttitle of the page
    def fetch_title(self, url):
        self.driver.get(url)
        return self.driver.title
    # to fetch the current url
    def fetch_url(self, url):
        self.driver.get(url)
        return self.driver.current_url

    # to fetch the entire content of page
    def fetch_pagesource(self, url):
        self.driver.get(url)
        return self.driver.page_source

url = "https://www.guvi.in"
browser().driver.get(url)
print(browser().driver.title)
print(browser().driver.current_url)
#print(browser().driver.page_source)

