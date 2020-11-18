from bs4 import BeautifulSoup
import csv
import urllib2
import pandas as pd

# baseline for upper limit of player ids
playersmin = 0
playersmax = 2000

open('formerplayers.csv', 'w')

# while loop to iterate through every player
while playersmin < playersmax:
    url = 'http://www.bkfrem.dk/default.asp?id=19&spillerid='+str(playersmin)+'&todo=arkiv'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    # using the soup object to find the class which contains the relevant data
    container = soup.find('div', class_='main')

    # creating an array of rows
    rows = []
    
    # making a for loop to append every player from every 'td' instance
    for r in container.select('tr'):
        rows.append([col.text.strip() for col in r.select('td')])
        rows.append(['~', '~'])
    
    if rows != []:
        player = soup.find('div', attrs={'class': 'mainwidth'})
        playername = player.find('h1').text
        if player.find('img') is not None:
            imageURL = player.find('img')['src']
            rows.append(['ImageURL', imageURL])
            rows.append(['~', '~'])
            print imageURL
        rows.append(['Name', playername])
        rows.append(['~', '~'])
        rows.append(['ID', playersmin])
        rows.append(['::::', '::::'])
    
        print playername
    
    zipped = zip(*rows)

    # first row needs to have the header of the table on the website
    csvfile = pd.DataFrame(zipped)

    # writing the data to a csv file, encoded, and without indexing
    csvfile.to_csv('formerplayers.csv', encoding='utf-8', mode='a', header=None, index=None)
    playersmin +=1

