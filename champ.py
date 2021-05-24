
from  items import *
from  Champs import *
from runes import *
from PyQt5 import QtCore, QtGui, QtWidgets
from pandas import DataFrame,read_csv
import json
from functools import partial

class Ui_ChampWindow(object):
    def setupUi(self, MainWindow,champion):
        self.getstats(champion)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(975, 737)
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.champion_pic = QtWidgets.QLabel(self.centralwidget)
        self.champion_pic.setGeometry(QtCore.QRect(40, 40, 100, 50))
        self.champion_pic.setText("")
        self.champion_pic.setPixmap(QtGui.QPixmap("champion/tiles/{0}_0.jpg".format(champion.name)))
        self.champion_pic.setScaledContents(True)
        self.champion_pic.setObjectName("champion_pic")
        self.champion_name = QtWidgets.QLabel(self.centralwidget)
        self.champion_name.setGeometry(QtCore.QRect(40, 90, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.champion_name.setFont(font)
        self.champion_name.setObjectName("champion_name")
        
        self.Role = QtWidgets.QLabel(self.centralwidget)
        self.Role.setGeometry(QtCore.QRect(40, 110, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Role.setFont(font)
        self.Role.setObjectName("Role")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 90, 101, 51))
        self.label.setObjectName("label")
        self.WinRate = QtWidgets.QLabel(self.centralwidget)
        self.WinRate.setGeometry(QtCore.QRect(600, 90, 101, 51))
        self.WinRate.setObjectName("WinRate")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 140, 101, 51))
        self.label_3.setObjectName("label_3")
        self.BanRate = QtWidgets.QLabel(self.centralwidget)
        self.BanRate.setGeometry(QtCore.QRect(600, 140, 101, 51))
        self.BanRate.setObjectName("BanRate")
        self.Rank = QtWidgets.QComboBox(self.centralwidget)
        self.Rank.setGeometry(QtCore.QRect(750, 30, 161, 61))
        self.Rank.setObjectName("Rank")
        self.Rank.addItem("")
        self.Rank.addItem("")
        self.Rank.addItem("")
        self.Rank.addItem("")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(750, 90, 161, 41))
        self.refresh.setObjectName("refresh")
        self.refresh.clicked.connect(partial(self.refresh_clicked, champion))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 151, 41))
        self.label_2.setObjectName("label_2")
        self.item0_name = QtWidgets.QLabel(self.centralwidget)
        self.item0_name.setGeometry(QtCore.QRect(40, 230, 111, 21))
        self.item0_name.setScaledContents(True)
        self.item0_name.setObjectName("item0_name")
        self.item0 = QtWidgets.QLabel(self.centralwidget)
        self.item0.setGeometry(QtCore.QRect(50, 260, 111, 51))
        self.item0.setText("")
        self.item0.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[0]).item_id)))
        self.item0.setScaledContents(True)
        self.item0.setObjectName("item0")
        self.item1 = QtWidgets.QLabel(self.centralwidget)
        self.item1.setGeometry(QtCore.QRect(160, 260, 111, 51))
        self.item1.setText("")
        self.item1.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[1]).item_id)))
        self.item1.setScaledContents(True)
        self.item1.setObjectName("item1")
        self.item2 = QtWidgets.QLabel(self.centralwidget)
        self.item2.setGeometry(QtCore.QRect(270, 260, 111, 51))
        self.item2.setText("")
        self.item2.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[2]).item_id)))
        self.item2.setScaledContents(True)
        self.item2.setObjectName("item2")
        self.item3 = QtWidgets.QLabel(self.centralwidget)
        self.item3.setGeometry(QtCore.QRect(380, 260, 111, 51))
        self.item3.setText("")
        self.item3.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[3]).item_id)))
        self.item3.setScaledContents(True)
        self.item3.setObjectName("item3")
        self.item4 = QtWidgets.QLabel(self.centralwidget)
        self.item4.setGeometry(QtCore.QRect(490, 260, 111, 51))
        self.item4.setText("")
        self.item4.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[4]).item_id)))
        self.item4.setScaledContents(True)
        self.item4.setObjectName("item4")
        self.item5 = QtWidgets.QLabel(self.centralwidget)
        self.item5.setGeometry(QtCore.QRect(600, 260, 111, 51))
        self.item5.setText("")
        self.item5.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[5]).item_id)))
        self.item5.setScaledContents(True)
        self.item5.setObjectName("item5")
        self.item1_name = QtWidgets.QLabel(self.centralwidget)
        self.item1_name.setGeometry(QtCore.QRect(160, 230, 111, 21))
        self.item1_name.setScaledContents(True)
        self.item1_name.setObjectName("item1_name")
        self.item2_name = QtWidgets.QLabel(self.centralwidget)
        self.item2_name.setGeometry(QtCore.QRect(270, 230, 111, 21))
        self.item2_name.setScaledContents(True)
        self.item2_name.setObjectName("item2_name")
        self.item3_name = QtWidgets.QLabel(self.centralwidget)
        self.item3_name.setGeometry(QtCore.QRect(380, 230, 111, 21))
        self.item3_name.setScaledContents(True)
        self.item3_name.setObjectName("item3_name")
        self.item4_name = QtWidgets.QLabel(self.centralwidget)
        self.item4_name.setGeometry(QtCore.QRect(490, 230, 111, 21))
        self.item4_name.setScaledContents(True)
        self.item4_name.setObjectName("item4_name")
        self.item5_name = QtWidgets.QLabel(self.centralwidget)
        self.item5_name.setGeometry(QtCore.QRect(610, 230, 111, 21))
        self.item5_name.setScaledContents(True)
        self.item5_name.setObjectName("item5_name")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 350, 151, 41))
        self.label_16.setObjectName("label_16")
        self.rune0 = QtWidgets.QLabel(self.centralwidget)
        self.rune0.setGeometry(QtCore.QRect(70, 420, 100, 50))
        self.rune0.setText("")
        self.rune0.setPixmap(QtGui.QPixmap(Rune(self.runelist[0]).png))
        self.rune0.setScaledContents(True)
        self.rune0.setObjectName("rune0")
        self.rune0_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.rune0_text.setGeometry(QtCore.QRect(30, 480, 161, 141))
        self.rune0_text.setObjectName("rune0_text")
        self.rune1_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.rune1_text.setGeometry(QtCore.QRect(180, 480, 161, 141))
        self.rune1_text.setObjectName("rune1_text")
        self.rune1 = QtWidgets.QLabel(self.centralwidget)
        self.rune1.setGeometry(QtCore.QRect(230, 440, 81, 31))
        self.rune1.setText("")
        self.rune1.setPixmap(QtGui.QPixmap(Rune(self.runelist[1]).png))
        self.rune1.setScaledContents(True)
        self.rune1.setObjectName("rune1")
        self.rune2 = QtWidgets.QLabel(self.centralwidget)
        self.rune2.setGeometry(QtCore.QRect(380, 440, 81, 31))
        self.rune2.setText("")
        self.rune2.setPixmap(QtGui.QPixmap(Rune(self.runelist[2]).png))
        self.rune2.setScaledContents(True)
        self.rune2.setObjectName("rune2")
        self.rune3 = QtWidgets.QLabel(self.centralwidget)
        self.rune3.setGeometry(QtCore.QRect(540, 440, 81, 31))
        self.rune3.setText("")
        self.rune3.setPixmap(QtGui.QPixmap(Rune(self.runelist[3]).png))
        self.rune3.setScaledContents(True)
        self.rune3.setObjectName("rune3")
        self.rune4 = QtWidgets.QLabel(self.centralwidget)
        self.rune4.setGeometry(QtCore.QRect(690, 440, 81, 31))
        self.rune4.setText("")
        self.rune4.setPixmap(QtGui.QPixmap(Rune(self.runelist[4]).png))
        self.rune4.setScaledContents(True)
        self.rune4.setObjectName("rune4")
        self.rune5 = QtWidgets.QLabel(self.centralwidget)
        self.rune5.setGeometry(QtCore.QRect(840, 440, 81, 31))
        self.rune5.setText("")
        self.rune5.setPixmap(QtGui.QPixmap(Rune(self.runelist[5]).png))
        self.rune5.setScaledContents(True)
        self.rune5.setObjectName("rune5")
        self.rune2_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.rune2_text.setGeometry(QtCore.QRect(340, 480, 161, 141))
        self.rune2_text.setObjectName("rune2_text")
        self.rune3_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.rune3_text.setGeometry(QtCore.QRect(500, 480, 161, 141))
        self.rune3_text.setObjectName("rune3_text")
        self.rune4_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.rune4_text.setGeometry(QtCore.QRect(650, 480, 161, 141))
        self.rune4_text.setObjectName("rune4_text")
        self.rune5_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.rune5_text.setGeometry(QtCore.QRect(810, 480, 161, 141))
        self.rune5_text.setObjectName("rune5_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow,champion)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def refresh_clicked(self,champion):
        _translate = QtCore.QCoreApplication.translate
        rank = str(self.Rank.currentText())
        self.getstats(champion,rank)
        self.rune0_text.setPlainText(Rune(self.runelist[0]).desc)
        self.rune1_text.setPlainText(Rune(self.runelist[1]).desc)
        self.rune2_text.setPlainText(Rune(self.runelist[2]).desc)
        self.rune3_text.setPlainText(Rune(self.runelist[3]).desc)
        self.rune4_text.setPlainText(Rune(self.runelist[4]).desc)
        self.rune5_text.setPlainText(Rune(self.runelist[5]).desc)
        self.item0.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[0]).item_id)))
        self.item1.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[1]).item_id)))
        self.item2.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[2]).item_id)))
        self.item3.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[3]).item_id)))
        self.item4.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[4]).item_id)))
        self.item5.setPixmap(QtGui.QPixmap("item/{0}.png".format(Item(self.item_ids[5]).item_id)))
        self.item0_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[0]).name)))
        self.item1_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[1]).name)))
        self.item2_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[2]).name)))
        self.item3_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[3]).name)))
        self.item4_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[4]).name)))
        self.item5_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[5]).name)))
        self.rune0.setPixmap(QtGui.QPixmap(Rune(self.runelist[0]).png))
        self.rune1.setPixmap(QtGui.QPixmap(Rune(self.runelist[1]).png))
        self.rune2.setPixmap(QtGui.QPixmap(Rune(self.runelist[2]).png))
        self.rune3.setPixmap(QtGui.QPixmap(Rune(self.runelist[3]).png))
        self.rune4.setPixmap(QtGui.QPixmap(Rune(self.runelist[4]).png))
        self.rune5.setPixmap(QtGui.QPixmap(Rune(self.runelist[5]).png))
        self.BanRate.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">{0}</span></p></body></html>".format(self.banrate)))
        self.WinRate.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">{0}</span></p></body></html>".format(self.winrate)))
        self.Role.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">{0}</span></p></body></html>".format(self.role_name)))
        
    def getstats(self,champion,rank="bronze"):
        df=read_csv("{0}stats.csv".format(rank))
        championstats=df[df['id']==int(champion.key)]
        fakelist=championstats["Runes"].to_list()
        #list of rune ids
        self.runelist=json.loads(fakelist[0])
        role=championstats.Role.to_string()
        role=role.split(" ")
        #name for the role lable
        self.role_name=role[len(role)-1]
        #winrate float
        self.winrate=float(championstats.WinRate)
        #banrate float
        self.banrate=float(championstats.BanRate)
        builds=championstats["Builds"].to_list()[0]
        builds=builds.replace('\'', '')
        builds=json.loads(builds)
        #item ids
        self.item_ids=[str(x) for x in builds]
        
        
        
        
        
    def retranslateUi(self, MainWindow,champion):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.champion_name.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">{0}</span></p></body></html>".format(champion.name)))
        self.Role.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">{0}</span></p></body></html>".format(self.role_name)))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Win Rate</span></p></body></html>"))
        self.WinRate.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">{0}</span></p></body></html>".format(self.winrate)))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Ban Rate</span></p></body></html>"))
        self.BanRate.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">{0}</span></p></body></html>".format(self.banrate)))
        self.Rank.setItemText(0, _translate("MainWindow", "Bronze"))
        self.Rank.setItemText(1, _translate("MainWindow", "Silver"))
        self.Rank.setItemText(2, _translate("MainWindow", "Gold"))
        self.Rank.setItemText(3, _translate("MainWindow", "plat"))
        self.refresh.setText(_translate("MainWindow", "refresh"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Build</span></p></body></html>"))
        self.item0_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[0]).name)))
        self.item1_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[1]).name)))
        self.item2_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[2]).name)))
        self.item3_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[3]).name)))
        self.item4_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[4]).name)))
        self.item5_name.setText(_translate("MainWindow", "<html><head/><body><p>{0}</p></body></html>".format(Item(self.item_ids[5]).name)))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Runes</span></p></body></html>"))
        self.rune0_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Hitting a champion with 3 separate attacks or abilities in 3s deals bonus adaptive damage.</span></p></body></html>"))
        self.rune1_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Gain a burst of Lethality and Magic Penetration after using a dash, leap, blink, teleport, or when leaving stealth.</span></p></body></html>"))
        self.rune2_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Collect eyeballs for champion takedowns. Gain permanent AD or AP, adaptive for each eyeball plus bonus upon collection completion.</span></p></body></html>"))
        self.rune3_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Unique takedowns grant permanent healing from ability damage</span></p></body></html>"))
        self.rune4_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Takedowns restore mana or energy and increase their maximum amounts</span></p></body></html>"))
        self.rune5_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Takedowns on enemies grant permanent Tenacity</span></p></body></html>"))
        self.rune0_text.setPlainText(Rune(self.runelist[0]).desc)
        self.rune1_text.setPlainText(Rune(self.runelist[1]).desc)
        self.rune2_text.setPlainText(Rune(self.runelist[2]).desc)
        self.rune3_text.setPlainText(Rune(self.runelist[3]).desc)
        self.rune4_text.setPlainText(Rune(self.runelist[4]).desc)
        self.rune5_text.setPlainText(Rune(self.runelist[5]).desc)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_ChampWindow()
    ui.setupUi(Window,Champion("Alistar"))
    Window.setWindowTitle("League of Stats-{0}".format("Zed"))
    Window.show()
    app.exec()


        





