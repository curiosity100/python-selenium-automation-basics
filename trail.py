import requests
from bs4 import BeautifulSoup


class Suman:
    url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    # make a connection with the flipkart.com
    data = requests.get(url)

    # create an object for the class BeautifulSoup and use it with its constructor with data and lxml as decoder
    soup = BeautifulSoup(data.content, 'lxml')

    # method for fetching entire website on the terminal
    def website(self):
        return self.soup.prettify()

    # method to fetch the product name
    def product_name(self):
        product_name = self.soup.find('div', class_='_4rR01T')
        return product_name.text

    # method for fetching the star ratings
    def product_rating(self):
        product_rating = self.soup.find('div', class_='_3LWZlK')
        return product_rating.text

    # method to fetch the product price
    def product_price(self):
        product_price = self.soup.find('div', class_='_30jeq3 _1_WHN1')
        return product_price.text

    # method to fetch everything present on the webpage
    def scrap_everything(self):
        product_name = []
        product_ratings = []
        product_prices = []
        # itirate over the entire div element to get the data
        for data in self.soup.findAll('div', class_='_3pLy-c row'):
            names = data.find('div', class_='_4rR01T')
            ratings = data.find('div', class_='_3LWZlK')
            prices = data.find('div', class_='_30jeq3 _1_WHN1')
            # append the information into the blank list
            product_name.append(names.text)
            product_ratings.append(ratings.text)
            product_prices.append(prices.text)
        print(product_name)
        print('#########################################')
        print(product_ratings)
        print('#########################################')
        print(product_prices)


# print(Suman().website())
#print(Suman().product_name())

# print(Suman().product_rating())

# print(Suman().product_price())

#print(Suman().scrap_everything())