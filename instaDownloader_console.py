import requests
from bs4 import BeautifulSoup as bs
import subprocess
import os
import urllib.request


def download(imgUrl):
    request = requests.get(imgUrl)
    renault = request.content
    soup = bs(renault, 'lxml')
    for divData in soup.findAll("meta", property="og:image"):
        imgSrc = divData['content']
        urllib.request.urlretrieve(imgSrc, 'Downloads/test.png')


''' obsolete code, but might be useful for later
def renameFile(newName):
    newName = newName + ".png"
    for files in os.listdir(os.curdir):
        if ".com" in files:
            os.rename(files, newName)
'''


def checkFolders():
    for files in os.listdir(os.curdir):
        if not os.path.exists('Downloads'):
            os.makedirs('Downloads')


checkFolders()

# url = input('URL to Post >>> ')

download('https://www.instagram.com/p/Bwz5CF7AgJf/')

# renameFile('BOI')

# 'https://www.instagram.com/p/Bwz5CF7AgJf/'

'''
working:
for divdata in soup.findAll('meta', {"property": "og:image"}):

https://www.instagram.com/p/BvynZtUgJVJ/?hl=en

for divdata in soup2.findAll('div', {"class": "preview"}):
    for getatag in divdata.findAll('a', {'class': 'zoom'}):
        for getimgtag in getatag.findAll('img',src=True):
            print getimgtag['src']

<meta property="og:image" content="https://scontent-waw1-1.cdninstagram.com/vp/c1407f2b38c9983f569881bf0fe483cb/5D55E275/t51.2885-15/e35/52626401_648321182275488_9133271219251416285_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com" />


title = soup.find("meta",  property="og:title")
url = soup.find("meta",  property="og:url")

print(title["content"] if title else "No meta title given")
print(url["content"] if url else "No meta url given")

'''
