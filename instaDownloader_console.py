import requests
from bs4 import BeautifulSoup as bs
import subprocess

def downlaod(imgUrl):
    request = requests.get(imgUrl)
    resault = request.content
    soup = bs(resault, 'lxml')
    links = soup.find_all("a")

    print(links)


url = input('URL to post >>> ')

downlaod(url)