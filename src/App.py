import sys, traceback

import easygui

from YouTube import Download_video

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QRadioButton, QTextEdit, QMessageBox

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setGeometry(250,250, 550, 170)
        self.setWindowTitle("YouTube Downloader")

        self.initUI()

    def initUI(self):
        self.url_label = QtWidgets.QLabel(self)
        self.url_label.setText("URL: ")
        self.url_label.move(40, 22)

        self.textArea = QLineEdit(self)
        self.textArea.setText("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.textArea.resize(400, 18)
        self.textArea.move(70,  30)

        # self.optionFullHd = QRadioButton(self)
        # self.optionFullHd.setText("1080p")
        # self.optionFullHd.move(75,50)
        # self.optionFullHd.click()

        self.optionHd = QRadioButton(self)
        self.optionHd.setText("720p")
        self.optionHd.move(150,50)
        self.optionHd.click()

        self.optionVideoOnly = QRadioButton(self)
        self.optionVideoOnly.setText("Video Only")
        self.optionVideoOnly.move(225,50)

        self.optionAudioOnly = QRadioButton(self)
        self.optionAudioOnly.setText("Audio Only")
        self.optionAudioOnly.move(315,50)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Download")
        self.button.move(230,120)
        self.button.clicked.connect(self.clicker)

        self.dir_label = QtWidgets.QLabel(self)
        self.dir_label.setText("Output: ")
        self.dir_label.move(25, 83)

        self.outputDirectory = QLineEdit(self)
        self.outputDirectory.setText("Output\\")
        self.outputDirectory.resize(400, 18)
        self.outputDirectory.move(70,  90)

        self.selectDir = QtWidgets.QPushButton(self)
        self.selectDir.setText("...")
        self.selectDir.move(490,88)
        self.selectDir.resize(20,20)
        self.selectDir.clicked.connect(self.select)


    def clicker(self):
        option = -1

        # if self.optionFullHd.isChecked() == True:
        #     option = 0
        if self.optionHd.isChecked() == True:
            option = 1
        elif self.optionVideoOnly.isChecked() == True:
            option = 2
        elif self.optionAudioOnly.isChecked() == True:
            option = 3

        try:
            Download_video(self.textArea.text(), option, self.outputDirectory.text())
            self.show_popup("Video has been downloaded successfully")
        except :
            self.show_popup("URL not valid!", QMessageBox.Critical)
            traceback.print_exc(file=sys.stdout)
        

    def select(self):
        path = easygui.diropenbox()
        self.outputDirectory.setText(path + "\\")

    def show_popup(self, message, type = QMessageBox.Information):
        msg = QMessageBox()
        msg.setWindowTitle("YouTube Downloader")
        msg.setText(message)
        msg.setIcon(type)

        x = msg.exec_()


def window():
    app = QApplication(sys.argv)
    win = App()

    win.show()
    sys.exit(app.exec_())


window()






