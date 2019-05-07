import requests
from bs4 import BeautifulSoup as bs
import subprocess

def downlaod(imgUrl):
    request = requests.get(imgUrl)
    resault = request.content
    soup = bs(resault, 'lxml')
    for divdata in soup.findAll('span', {"id": "react-root"}):
        for links in divdata.findAll('section', {"calss": "_9eogI E3X2T"}):
            print(links)


downlaod('https://www.instagram.com/p/BvynZtUgJVJ/?hl=en')


'''
https://www.instagram.com/p/BvynZtUgJVJ/?hl=en

for divdata in soup2.findAll('div', {"class": "preview"}):
    for getatag in divdata.findAll('a', {'class': 'zoom'}):
        for getimgtag in getatag.findAll('img',src=True):
            print getimgtag['src']

'''