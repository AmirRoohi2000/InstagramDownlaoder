import requests
from bs4 import BeautifulSoup as bs
import os
import urllib.request
import argparse


def getName(imgUrl):  # with this function, i grab the id of the post
    try:
        request = requests.get(imgUrl)  # pass in the url
        resault = request.content  # scrap the data
        soup = bs(resault, 'lxml')  # i think this beutifies it
        for divData in soup.findAll("meta", property="og:url"):  # save the meta with the property "og:url" in divData
            text = divData['content']  # save the string
            name1 = text.lstrip('https://www.instagram.com/p/')  # remove this part form that string
            name = name1.replace('/', '')  # replace / with nothing

        return name  # return the post ID, meaning the way of using is like this
        # postName = getName(postURL)
    except Exception as ex:
        print(str(ex))


def download(imgUrl):  # this function grabs the data from the given url and downloads the post, with the post id as its name
    try:
        name = getName(imgUrl)
        request = requests.get(imgUrl)
        resault = request.content
        soup = bs(resault, 'lxml')
        if soup.findAll("meta", property="og:video"):  # so if we find a video
            for divData in soup.findAll("meta", property="og:video"):  # then we download the video, with the mp4 format
                imgSrc = divData['content']
                fileName = 'InstaDownloads/' + name + '.mp4'
                urllib.request.urlretrieve(imgSrc, fileName)
        elif soup.findAll("meta", property="og:image"):  # in case of an image, then we download the image with the png format
            for divData in soup.findAll("meta", property="og:image"):
                imgSrc = divData['content']
                fileName = 'InstaDownloads/' + name + '.png'
                urllib.request.urlretrieve(imgSrc, fileName)

    except Exception as ex:
        print(str(ex))


def downloadName(imgUrl, name):  # this function is the same as above, only that you pick a name
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


def checkFolders():  # with this function, a folder is created, if its not there
    try:
        for files in os.listdir(os.curdir):  # check all the folders in the directory of the app
            if not os.path.exists('InstaDownloads'):  # if the "InstaDownlaods" does not exist, create it
                os.makedirs('InstaDownloads')
    except Exception as ex:
        print(str(ex))


checkFolders()

# arguments, because it makes it simpler to use
# create an ArgumentParser object
parser = argparse.ArgumentParser(description='Download a post from Instagram, be it photo or video!')

# from the two first arguments, in my case, one has to be entered, the other one is not necessary
# create an argument to take
parser.add_argument('-u', '--URL', type=str, metavar='', required=True,
                    help='The URL of that post, something like this >>> https://www.instagram.com/[author]/p/xxxxxxxxxxxx/')
parser.add_argument('-n', '--Name', type=str, metavar='', required=False,
                    help='The name for the downloaded post, a name is enough, the programm will add the extension and formatting automagically!')

# create a group of extra arguments, only one can be used at a time
group = parser.add_mutually_exclusive_group()

# from the group, only one can be picked, or none
# add arguments to that group
group.add_argument('-q', '--quite', action='store_true', help='Will download the post and exit immediately')
group.add_argument('-v', '--verbose', action='store_true',
                   help='Full hacker style verbose for cool looks (like y not, right?)')

# put all the arguments in one value for later use
arguments = parser.parse_args()

# here we have the different scenarios, pretty self explanatory
if arguments.quite:
    if arguments.Name:
        downloadName(arguments.URL, arguments.Name)
    else:
        download(arguments.URL)
elif arguments.verbose:
    if arguments.Name:
        downloadName(arguments.URL, arguments.Name)
        print('[+] Got input')
        print('[+] Found post')
        print('[+] Downloaded post')
        print('[+] Renamed post')
        print('[+] Enjoy!')
    else:
        download(arguments.URL)
        print('[+] Got input')
        print('[+] Found post')
        print('[+] Downloaded post')
        print('[+] Renamed post')
        print('[+] Enjoy!')
else:
    if arguments.Name:
        downloadName(arguments.URL, arguments.Name)
        print('DONE!')
    else:
        download(arguments.URL)
        print('DONE!')
