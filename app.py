# import libraries
import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Specify the URL
quote_page = ['https://www.fool.com/quote/nasdaq/invesco-qqq-trust/qqq/',
              'https://www.fool.com/quote/nysemkt/spdr-sp-500/spy/',
              'https://www.fool.com/quote/nysemkt/technology-spdr/xlk/',
              'https://www.fool.com/quote/nysemkt/vanguard-information-technology-etf/vgt/']

# For loop
data = []

for site in quote_page:
    # query the website and return the html to the variable ‘page’
    page = urllib.request.urlopen(site)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, "html.parser")

    # Take out the <div> of name and get its value
    name_box = soup.find("h2", attrs={"class": "company-name"})
    name = name_box.text.strip()

    # get the index price
    price_box = soup.find("span", attrs={"class": "current-price"})
    price = price_box.text.strip()

    # save the data in tuple
    data.append((name, price))

# open a csv file with append, so old data will not be erased
with open("index.csv", "a") as csv_file:
    writer = csv.writer(csv_file)
    # The for loop
    for name, price in data:
        writer.writerow([name, price, datetime.now()])
