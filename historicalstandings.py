import requests
from bs4 import BeautifulSoup
import pandas as pd

# specify the url and get the text
url = "http://www.bkfrem.dk/default.asp?id=81"
urlpagetext = requests.get(url).text

# making the beautiful soup object
soup = BeautifulSoup(urlpagetext, 'html5lib')

# find instance of div tag with class "main"
container = soup.find_all('div', class_='main')[0]

# create array that will store the rows
rows = []

# for loop to store the data in the rows
for r in container.select('tr'):
    rows.append([col.text.strip() for col in r.select('td')])

# let the first row be the header as on the website
data = pd.DataFrame(rows[1:])
data.columns = rows[0]

# writing the data to a csv file, encoded, and without indexing
data.to_csv('historicalstandings.csv', encoding='utf-8', index=False)
