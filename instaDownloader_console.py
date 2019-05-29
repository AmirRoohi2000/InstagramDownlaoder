import requests
from bs4 import BeautifulSoup as bs
import os
import urllib.request

def download(imgUrl, name):
    try:
        request = requests.get(imgUrl)
        resault = request.content
        soup = bs(resault, 'lxml')
        if soup.findAll("meta", property="og:video"):
            for divData in soup.findAll("meta", property="og:video"):
                imgSrc = divData['content']
                fileName = 'InstaDownloads/' + name + '.mp4'
                urllib.request.urlretrieve(imgSrc, fileName)
        elif soup.findAll("meta", property="og:image"):
            for divData in soup.findAll("meta", property="og:image"):
                imgSrc = divData['content']
                fileName = 'InstaDownloads/' + name + '.png'
                urllib.request.urlretrieve(imgSrc, fileName)

    except Exception as ex:
        print(str(ex))


def checkFolders():
    try:
        for files in os.listdir(os.curdir):
            if not os.path.exists('InstaDownloads'):
                os.makedirs('InstaDownloads')
    except Exception as ex:
        print(str(ex))


checkFolders()

url = input('URL to Post >>> ')
name = input('Name >>> ')

download(url, name)