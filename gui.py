
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from champlist import *
from history import *
class Ui_login(object):
    def openChampList(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_ChampListWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def openHistory(self):
        try:
            self.window2=QtWidgets.QMainWindow()
            self.ui2=matchHistory()
            self.ui2.setupUi(self.window2,self.summoner_name.text())
            self.window2.show()
        except:
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('Wrong summoner name try again')


        
        
    def setupUi(self, login):
        login.setObjectName("login")
        login.setFixedSize(584, 471)
        login.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"")
        self.app_name = QtWidgets.QLabel(login)
        self.app_name.setGeometry(QtCore.QRect(170, 50, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.app_name.setFont(font)
        self.app_name.setObjectName("app_name")
        self.summoner_name = QtWidgets.QLineEdit(login)
        self.summoner_name.setGeometry(QtCore.QRect(290, 200, 221, 31))
        self.summoner_name.setStyleSheet("\n"
"alternate-background-color: rgb(54, 54, 54);\n"
"")
        self.summoner_name.setFrame(True)
        self.summoner_name.setObjectName("summoner_name")
        
        self.match_button = QtWidgets.QPushButton(login)
        self.match_button.setGeometry(QtCore.QRect(290, 230, 221, 51))
        self.match_button.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.match_button.setObjectName("match_button")
        self.match_button.clicked.connect(self.openHistory)
        self.list_button = QtWidgets.QPushButton(login)
        self.list_button.setGeometry(QtCore.QRect(40, 230, 221, 51))
        self.list_button.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.list_button.clicked.connect(self.openChampList)
        self.list_button.setObjectName("list_button")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Dialog"))
        self.app_name.setWhatsThis(_translate("login", "<html><head/><body><p>League of Stats</p></body></html>"))
        self.app_name.setText(_translate("login", "League of Stats "))
        self.summoner_name.setText(_translate("login", "enter summoner name here"))
        self.match_button.setText(_translate("login", "Enter Match History"))
        self.list_button.setText(_translate("login", "Enter Champion List"))












if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(login)
    login.setWindowTitle("League of Stats")
    login.show()
    sys.exit(app.exec_())
