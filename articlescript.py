# import libraries
import csv
import urllib2
from bs4 import BeautifulSoup

# baseline for upper limit of article ids
articles = 4459

# boolean used to check if the article exists
isValid = True

# image url for first image in each article
imageURL = None

# while loop to check if the article exists. If it does, we get the last 10 articles
while isValid:
    url = 'http://www.bkfrem.dk/default.asp?vis=nyheder&id='+str(articles)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    if soup.find('h1', attrs={'style': 'margin-bottom:0px'}).text == '':
        isValid = False
    else:
        articles +=1

articleid = articles - 20

# create CSV file
csvfile = csv.writer(open('news.csv', 'w'))

while articleid < articles:
    # specify the url and article id
    url = 'http://www.bkfrem.dk/default.asp?vis=nyheder&id='+str(articleid)
    # query the website and return the html to the variable
    page = urllib2.urlopen(url)

    # parse the html using beautiful soup and store in variable soup
    soup = BeautifulSoup(page, 'html.parser')    

    # take out the <div> of name and get its value and text
    title_box = soup.find('h1', attrs={'style': 'margin-bottom:0px'})
    title = title_box.text.encode('utf-8').strip()
    date_box = soup.find('div', attrs={'style': 'font-style:italic; padding-bottom:10px'})
    date = date_box.text.encode('utf-8').strip()
    articleText_box = soup.find('div', attrs={'class': 'news'})
    articleText = articleText_box.text.encode('utf-8').strip()

    if articleText_box.find('h4') is not None:
        articleSecondTitle_box = articleText_box.find('h4')
        secondTitle = articleSecondTitle_box.text.encode('utf-8').strip().replace('\"','')
    else:
        secondTitle = ''
    
    print secondTitle

    image = soup.find('div', attrs={'class': 'mainwidth'})
    if image.find('img') is not None:
        imageURLPath = image.find('img')['src']
        imageURL = 'http://www.bkfrem.dk'+imageURLPath
    else:
        imageURL = ''
    print imageURL

    # print the data to the CSV file
    csvfile.writerow((title, '~', date, '~', articleText, '~', imageURL, '~', secondTitle, '~', articleid, '::::'))
    articleid += 1
