import requests
from bs4 import BeautifulSoup as bs
import os
import urllib.request
import sys
import PyQt5
from PyQt5 import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QTextDocument
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QDialog, QLabel, QTextEdit, QPushButton, \
    QCheckBox, QComboBox, QFontComboBox, QColorDialog


# set up the app stuff they have to be done
mainWindow = QApplication(sys.argv)
rootWidget = QMainWindow = QMainWindow()

# set the style for the lables
lblStyle = "font-family: 'Times New Roman';\nfont-size: 16px; "

# set up the font used by the app
myFont = QFont("Times New Roman", 16)
# set up the font for QTextEdit
txtFont = QFont("Times New Roman", 14)
# set up the font for QPushButton
btnFont = QFont("Times New Roman", 14)

# a function to rename the downloaded file, if user has specified so
def checkFolders():
    for files in os.listdir(os.curdir):
        if not os.path.exists('InstaDownloads'):
            os.makedirs('InstaDownloads')

# function to download the image(for now just image, later even video, i hope so)
def download():
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

    txtUrl.clear()
    txtName.clear()


def newDownload():
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

    txtUrl.clear()
    txtName.clear()


# set up a label
linkLbl = QLabel("Link:", rootWidget)
linkLbl.setStyleSheet(lblStyle)
linkLbl.move(10, 10)

# set a multiline text box
txtUrl = QTextEdit(rootWidget)
txtUrl.setFont(txtFont)
txtUrl.move(5, 40)
txtUrl.resize(390, 50)

# set a download button
btnDownload = QPushButton('Download', rootWidget)
btnDownload.move(290, 105)
btnDownload.setFont(btnFont)
btnDownload.clicked.connect(newDownload)

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
rootWidget.show()
checkFolders()
sys.exit(mainWindow.exec_())
