import requests
import subprocess
import sys
from bs4 import BeautifulSoup as bs
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
txtFont = QFont("Times New Roman", 12)
# set up the font for QPushButton
btnFont = QFont("Times New Roman", 14)

# a function to rename the downloaded file, if user has specified so
def renameDnd():
    pass

# function to download the image(for now just image, later even video, i hope so)
def download():
    argument = 'wget ' + txtUrl.toPlainText()
    print(argument)
    txtUrl.clear()
    txtName.clear()
    # subprocess.call(argument, shell=True)


# set up a label
linkLbl = QLabel("Link:", rootWidget)
linkLbl.setStyleSheet(lblStyle)
linkLbl.move(10, 10)

# set a multiline text box
txtUrl = QTextEdit(rootWidget)
txtUrl.setFont(txtFont)
txtUrl.move(5, 40)
txtUrl.resize(290, 100)

# set a download button
btnDownload = QPushButton('Download', rootWidget)
btnDownload.move(190, 10)
btnDownload.setFont(btnFont)
btnDownload.clicked.connect(download)

# set another label to change file name
lblName = QLabel('Name:', rootWidget)
lblName.setStyleSheet(lblStyle)
lblName.move(10, 150)

# set up a text edit to enter a name
txtName = QTextEdit(rootWidget)
txtName.setFont(txtFont)
txtName.move(55, 152)
txtName.resize(90, 30)

# actually show the things, pretty standard stuff
rootWidget.setWindowTitle("InstaDownlaoder - @AmirRoohi2K")
rootWidget.setGeometry(100, 100, 300, 220)
rootWidget.setFont(myFont)
rootWidget.show()
sys.exit(mainWindow.exec_())
