# import libraries
import csv
import urllib2
import re
from bs4 import BeautifulSoup

# specify the url
url = 'http://www.bkfrem.dk/default.asp?id=76'

# query the website and return the html to the variable
page = urllib2.urlopen(url)

# parse the html using beautiful soup and store in variable soup
soup = BeautifulSoup(page, 'html.parser')

# create CSV file
csvfile = csv.writer(open('poty.csv', 'w'))
csvfile.writerow(["Year", "Name", "ID"])

# take out the <div> of name and get its value
items1 = soup.find_all('tr', attrs={'height': '16'})
items2 = soup.find_all('tr', attrs={'height': '15'})
items = items2 + items1

# print the data (encoded) to the CSV file
for i in range(len(items)):
    
    temp = items[i].getText().encode('utf-8').split()
    link = items[i].find('a').get('href').encode('utf-8')
    playerId = re.findall(r"\d+", link)[1]
    print playerId
    alldata = temp[0] + ','
    for j in range(len(temp)-1):
        alldata += temp[j+1] + ' '
    alldata += ','+playerId
    alldataSplitted = alldata.split(',', 1)
    csvfile.writerow(alldataSplitted)
    
