import requests
from bs4 import BeautifulSoup as bs
import subprocess
import os

def downlaod(imgUrl):
    print(f'{imgUrl}')
    request = requests.get(imgUrl)
    resault = request.content
    soup = bs(resault, 'lxml')
    for divdata in soup.findAll("meta",  property="og:image"):
        imgSrc = divdata['content']
        argument = 'wget --no-check-certificate ' + imgSrc
        subprocess.call(argument, shell=True)


def renameFild(newName):
    newName = newName + ".png"
    for files in os.listdir(os.curdir):
        if ".com" in files:
            os.rename(files, newName)




url1 = input('URL to Post >>> ')

downlaod(url1)

renameFild('BOI')

#'https://www.instagram.com/p/Bwz5CF7AgJf/'

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