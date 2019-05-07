import requests
from bs4 import BeautifulSoup as bs
import subprocess
import os

def downlaod(imgUrl):
    request = requests.get(imgUrl)
    resault = request.content
    soup = bs(resault, 'lxml')
    for divdata in soup.findAll("meta",  property="og:image"):
        imgSrc = divdata['content']
        print(imgSrc)
        argument = 'wget --no-check-certificate ' + imgSrc
        subprocess.call(argument, shell=False)


def renameFild(origName, newName):
    newName = newName + ".png"
    os.rename(origName, newName)

renameFild('test.com', 'oh_boi')

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