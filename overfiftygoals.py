from bs4 import BeautifulSoup
import csv
import urllib2
import pandas as pd
import re

# specify the url
url = 'http://www.bkfrem.dk/default.asp?id=78'

# query the website and return the html to the variable
page = urllib2.urlopen(url)

# making the beautiful soup object
soup = BeautifulSoup(page, 'html.parser')

# using the soup object to find the class which contains the relevant data
container = soup.find('div', class_='main')

# creating an array of rows
rows = []

# making a for loop to append every player from every 'td' instance
for r in container.select('tr'):
    v = r.find('a')
    if v is not None:
        v = v.get('href').encode('utf-8')
        playerId = re.findall(r"\d+", v)[1]
        rows.append([col.text.strip() for col in r.select('td')]+[playerId])

# first row needs to have the header of the table on the website
csvfile = pd.DataFrame(rows[1:])
csvfile.columns = rows[0]

# writing the data to a csv file, encoded, and without indexing
csvfile.to_csv('overfiftygoals.csv', encoding='utf-8', index=False)


