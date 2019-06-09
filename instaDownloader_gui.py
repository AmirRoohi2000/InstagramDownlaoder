import requests
from bs4 import BeautifulSoup as bs
import os
import urllib.request
import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QErrorMessage

# set up the app stuff they have to be done
mainWindow = QApplication(sys.argv)
rootWidget = QMainWindow = QMainWindow()

# set the style for the labels
lblStyle = "font-family: 'Times New Roman';\nfont-size: 16px; "
# set up the font used by the app
myFont = QFont("Times New Roman", 16)
# set up the font for QTextEdit
txtFont = QFont("Times New Roman", 14)
# set up the font for QPushButton
btnFont = QFont("Times New Roman", 14)
# set an icon for the window
icon = QIcon('insta.ico')

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

# a function to rename the downloaded file, if user has specified so
def checkFolders():
    try:
        for files in os.listdir(os.curdir):
            if not os.path.exists('InstaDownloads'):
                os.makedirs('InstaDownloads')
    except Exception as ex:
        msg = QErrorMessage()
        msg.showMessage(str(ex))

# function to download the image(for now just image, later even video, i hope so)
def download():
    try:
        name = getName(txtUrl.toPlainText())
        request = requests.get(txtUrl.toPlainText())
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

        txtUrl.clear()
        txtName.clear()
    except Exception as ex:
        msg = QErrorMessage()
        msg.showMessage(str(ex))


def downloadName():  # this function is the same as above, only that you pick a name
    try:
        request = requests.get(txtUrl.toPlainText())
        resault = request.content
        soup = bs(resault, 'lxml')
        if soup.findAll("meta", property="og:video"):
            for divData in soup.findAll("meta", property="og:video"):
                imgSrc = divData['content']
                fileName = 'InstaDownloads/' + txtName.toPlainText() + '.mp4'
                urllib.request.urlretrieve(imgSrc, fileName)
        elif soup.findAll("meta", property="og:image"):
            for divData in soup.findAll("meta", property="og:image"):
                imgSrc = divData['content']
                fileName = 'InstaDownloads/' + txtName.toPlainText() + '.png'
                urllib.request.urlretrieve(imgSrc, fileName)

    except Exception as ex:
        print(str(ex))


# set up a label
linkLbl = QLabel("Link:", rootWidget)
linkLbl.setStyleSheet(lblStyle)
linkLbl.move(10, 10)

# set a multi-line text box
txtUrl = QTextEdit(rootWidget)
txtUrl.setFont(txtFont)
txtUrl.move(5, 40)
txtUrl.resize(390, 50)

# set a download button
btnDownload = QPushButton('Download', rootWidget)
btnDownload.move(290, 105)
btnDownload.setFont(btnFont)
btnDownload.clicked.connect(download)

# set another label to change file name
lblName = QLabel('Name:', rootWidget)
lblName.setStyleSheet(lblStyle)
lblName.move(8, 100)

# set up a text edit to enter a name
txtName = QTextEdit(rootWidget)
txtName.setFont(txtFont)
txtName.move(53, 102)
txtName.resize(90, 35)

# actually show the things, pretty standard stuff
rootWidget.setWindowTitle("InstaDownlaoder - @AmirRoohi2K")
rootWidget.setGeometry(100, 100, 400, 180)
rootWidget.setFont(myFont)
rootWidget.setWindowIcon(icon)
rootWidget.show()
checkFolders()
sys.exit(mainWindow.exec_())
