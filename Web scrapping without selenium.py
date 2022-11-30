import requests
from bs4 import BeautifulSoup
import pandas as pd




class scrapping:
    data1 = requests.get(url="https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhdGVzdCBTYW1zdW5nIG1vYmlsZXMgIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=1.productCard.PMU_V2_1")
    soup = BeautifulSoup(data1.content, 'lxml')

    # to fetch entire page
    def website(self):
        return self.soup.prettify

    # to fetch product name
    def product_name(self):
        product_name= self.soup.find('div', class_='_4rR01T')
        return product_name.text

    # to fetch product rating
    def product_rating(self):
        product_rating= self.soup.find('div', class_='_3LWZlK')
        return product_rating.text
    # to scrap everyhing
    def scrap_everything(self):


        name= []
        rate=[]
        for items in self.soup.findAll('div', class_='_2kHMtA'):
            product_name = items.find('div', class_='_4rR01T').text
            product_rating = items.find('div', class_='_3LWZlK')

            name.append(product_name)
            rate.append(product_rating)
        return name
        #return rate

# to create excel
    def toexcel(self):
        self.scrap_everything()
        excel = {'product_name': self.scrap_everything()}
        excel1 = pd.DataFrame(excel)
        return excel1

# to create a file
file1 = open("product_names", "a")
for items in scrapping().scrap_everything():
    file1.write(items + "/n")
file1.close()


#print(scrapping().website())
#print(scrapping().product_name())
#print(scrapping().product_rating())
#print(scrapping().scrap_everything())
#print(scrapping().toexcel())
