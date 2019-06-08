import requests
from bs4 import BeautifulSoup as bs
import os
import urllib.request
import argparse

def getName(imgUrl):
    try:
        request = requests.get(imgUrl)
        resault = request.content
        soup = bs(resault, 'lxml')
        for divData in soup.findAll("meta", property="og:url"):
            text = divData['content'] # so first save the string
            name1 = text.lstrip('https://www.instagram.com/p/') # remove this part form that string
            name = name1.replace('/', '') # replace / with nothing

        return name
    except Exception as ex:
        print(str(ex))

def download(imgUrl):
    try:
        name = getName(imgUrl)
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

def downloadName(imgUrl, name):
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

# create an ArgumentParser object
parser = argparse.ArgumentParser(description='Download a post from Instagram, be it photo or video!')

# create an argument to take
parser.add_argument('-u', '--URL', type=str, metavar='', required=True, help='The URL of that post, something like this >>> https://www.instagram.com/[author]/p/xxxxxxxxxxxx/')
parser.add_argument('-n', '--Name', type=str, metavar='', required=False, help='The name for the downloaded post, a name is enough, the programm will add the extension and formatting automagically!')

# create a group of extra arguments, only one can be used at a time
group = parser.add_mutually_exclusive_group()

# add arguments to that group
group.add_argument('-q', '--quite', action='store_true', help='Will download the post and exit immediately')
group.add_argument('-v', '--verbose', action='store_true', help='Full hacker style verbose for cool looks (like y not, right?)')

# put all the arguments in one value for later use
arguments = parser.parse_args()

if arguments.quite:
    if arguments.Name:
        downloadName(arguments.URL, arguments.Name)
    else:
        download(arguments.URL)
elif arguments.verbose:
    download(arguments.URL, arguments.Name)
    print('[+] Got input')
    print('[+] Found post')
    print('[+] Downloaded post')
    print('[+] Renamed post')
    print('[+] Enjoy!')
else:
    download(arguments.URL, arguments.Name)
    print('DONE!')