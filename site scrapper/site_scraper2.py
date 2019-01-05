from bs4 import BeautifulSoup
import urllib.request
import csv

sauce=urllib.request.urlopen('https://www.newegg.com/global/in-en/Product/ProductList.aspx?Submit=ENE&N=100209765&IsNodeId=1&name=Wearable%20Technology&isdeptsrh=1').read()

soup=BeautifulSoup(sauce,'lxml')

csv_file = open('site_scrape2.csv','w')

csv_writer=csv.writer(csv_file)
csv_writer.writerow(['brand','features','price','link'])

containers=soup.find_all("div",class_="item-container")

for container in containers:
    brand=container.find("a",class_="item-title").text
    print(brand)

    features=container.find("ul",class_="item-features").text
    print(features)

    price=container.find("li",class_="price-was").text
    print(price)

    page=container.find("a",class_="item-title")["href"]
    print(page)
    print()

    csv_writer.writerow([brand,features,price,page])

csv_file.close()