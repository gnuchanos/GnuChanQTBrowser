#!/usr/bin/python

from PyQt5.QtCore import QUrl, Qt, QPoint, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton, QToolBar)
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5.QtGui import QKeySequence, QCursor
from PyQt5.QtWidgets import QShortcut

import sys, os

class GnuChanQT(QMainWindow):
    def __init__(self):
        super(GnuChanQT, self).__init__()
        self.initUI()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Update)
        self.timer.start(1000)

        # Default VAR
        self.GameMode = False

        # Shortcut
        self.GameModeOpen = QShortcut(QKeySequence('"'), self)
        self.GameModeOpen.activated.connect(self.GModeChange)

    def initUI(self):
        self.pyFilePath = os.path.dirname(os.path.abspath(__file__)) 
        print(self.pyFilePath)


        self.toolBar = QToolBar(self)
        self.addToolBar(self.toolBar)
        self.toolBar.setStyleSheet("background-color: #5a189a")

        # Back Button
        self.BackButton = QPushButton(self)
        self.BackButton.setEnabled(False)
        self.BackButton.setIcon(QIcon(f"{self.pyFilePath}/img/gcLeft.png"))
        self.BackButton.clicked.connect(self.Back) # Button Event Function
        self.toolBar.addWidget(self.BackButton)
        self.BackButton.setStyleSheet("background-color: #0e0021")

        # Forward Button
        self.ForwardButton = QPushButton(self)
        self.ForwardButton.setEnabled(False)
        self.ForwardButton.setIcon(QIcon(f"{self.pyFilePath}/img/gcRight.png"))
        self.ForwardButton.clicked.connect(self.Forward) # Button Event Function
        self.toolBar.addWidget(self.ForwardButton)
        self.ForwardButton.setStyleSheet("background-color: #0e0021")

        # Reload Page
        self.ReloadPageButton = QPushButton(self)
        self.ReloadPageButton.setIcon(QIcon(f"{self.pyFilePath}/img/refresh.png"))
        self.ReloadPageButton.clicked.connect(self.Reload) # Button Event Function
        self.toolBar.addWidget(self.ReloadPageButton)
        self.ReloadPageButton.setStyleSheet("background-color: #0e0021")

        #Return Home Page
        self.HomePageButton = QPushButton(self)
        self.HomePageButton.setIcon(QIcon(f"{self.pyFilePath}/img/home.png"))
        self.HomePageButton.clicked.connect(self.HomePage) # Button Event Function
        self.toolBar.addWidget(self.HomePageButton)
        self.HomePageButton.setStyleSheet("background-color: #0e0021")

        # Address Bar
        self.address = QLineEdit(self)
        self.address.returnPressed.connect(self.Load) # AdressBar Event Function
        self.toolBar.addWidget(self.address)
        self.address.setStyleSheet("""
            color: #d2a2fc; background-color: #150129; 
            selection-color: #8b6ca6; selection-background-color: #23004a; selection-border: 1px solid #260147
        """)

        # Web Page -> Body
        self.webEngineView = QWebEngineView(self)
        self.setCentralWidget(self.webEngineView)
        self.webEngineView.page().urlChanged.connect(self.onLoadFinished)
        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)
        self.webEngineView.page().urlChanged.connect(self.UrlChanged) # Button Event Function
        
        # Main Window
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle("GnuChanQT")
        self.show()

        # Default Home Page
        self.webEngineView.load(QUrl("https://github.com/gnuchanos"))

    def onLoadFinished(self):
        # Back Button Action
        if self.webEngineView.history().canGoBack():
            self.BackButton.setEnabled(True)
        else:
            self.BackButton.setEnabled(False)
        
        # Forward Button Action
        if self.webEngineView.history().canGoForward():
            self.ForwardButton.setEnabled(True)
        else:
            self.ForwardButton.setEnabled(False)

    def Load(self):
        url = QUrl.fromUserInput(self.address.text())
        if url.isValid():
            self.webEngineView.load(url)
        else:
            QMessageBox.warning(self, "Hata", "Geçersiz URL!")

    def Back(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def Forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def UrlChanged(self, url):
        self.address.setText(url.toString())

    def Reload(self):
        self.webEngineView.reload()

    def HomePage(self):
        self.webEngineView.load(QUrl("https://github.com/gnuchanos"))

    # Shourtcut Event
    def GModeChange(self):
        if not self.GameMode:
            self.GameMode = True
        else:
            self.GameMode = False


    def Update(self):
        pass







if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_UseDesktopOpenGL)
    app = QApplication(sys.argv)
    ex = GnuChanQT()
    sys.exit(app.exec_())


