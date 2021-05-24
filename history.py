
from PyQt5 import QtCore, QtGui, QtWidgets
from matchinfo import *
from items import *
import time
from Champs import *
from pandas import DataFrame,read_csv
class matchHistory(object):
    def setupUi(self, MainWindow,name):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1087, 900)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("\n"
"\n"
"background-color: rgb(54, 54, 54);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(300, 0, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 190, 1121, 20))
        self.line.setStyleSheet("alternate-background-color: rgb(49, 49, 49);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 250, 1121, 20))
        self.line_2.setStyleSheet("alternate-background-color: rgb(49, 49, 49);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.kda2 = QtWidgets.QLabel(self.centralwidget)
        self.kda2.setGeometry(QtCore.QRect(810, 270, 51, 41))
        self.kda2.setObjectName("kda2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(86, 200, 16, 671))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(180, 200, 16, 681))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.picitem11 = QtWidgets.QLabel(self.centralwidget)
        self.picitem11.setGeometry(QtCore.QRect(200, 210, 81, 41))
        self.picitem11.setText("")
        self.picitem11.setPixmap(QtGui.QPixmap("item/1001.png"))
        self.picitem11.setScaledContents(True)
        self.picitem11.setObjectName("picitem11")
        self.item11 = QtWidgets.QLabel(self.centralwidget)
        self.item11.setGeometry(QtCore.QRect(190, 180, 101, 20))
        self.item11.setObjectName("item11")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(280, 200, 20, 681))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.item12 = QtWidgets.QLabel(self.centralwidget)
        self.item12.setGeometry(QtCore.QRect(290, 180, 101, 20))
        self.item12.setObjectName("item12")
        self.picitem12 = QtWidgets.QLabel(self.centralwidget)
        self.picitem12.setGeometry(QtCore.QRect(300, 210, 81, 41))
        self.picitem12.setText("")
        self.picitem12.setPixmap(QtGui.QPixmap("item/1031.png"))
        self.picitem12.setScaledContents(True)
        self.picitem12.setObjectName("picitem12")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(380, 200, 20, 671))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.picitem13 = QtWidgets.QLabel(self.centralwidget)
        self.picitem13.setGeometry(QtCore.QRect(400, 210, 81, 41))
        self.picitem13.setText("")
        self.picitem13.setPixmap(QtGui.QPixmap("item/1033.png"))
        self.picitem13.setScaledContents(True)
        self.picitem13.setObjectName("picitem13")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(480, 200, 20, 671))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.item13 = QtWidgets.QLabel(self.centralwidget)
        self.item13.setGeometry(QtCore.QRect(390, 180, 101, 20))
        self.item13.setObjectName("item13")
        self.picitem14 = QtWidgets.QLabel(self.centralwidget)
        self.picitem14.setGeometry(QtCore.QRect(500, 210, 81, 41))
        self.picitem14.setText("")
        self.picitem14.setPixmap(QtGui.QPixmap("item/1036.png"))
        self.picitem14.setScaledContents(True)
        self.picitem14.setObjectName("picitem14")
        self.item14 = QtWidgets.QLabel(self.centralwidget)
        self.item14.setGeometry(QtCore.QRect(490, 180, 101, 20))
        self.item14.setObjectName("item14")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(580, 200, 20, 681))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.picitem15 = QtWidgets.QLabel(self.centralwidget)
        self.picitem15.setGeometry(QtCore.QRect(600, 210, 81, 41))
        self.picitem15.setText("")
        self.picitem15.setPixmap(QtGui.QPixmap("item/1011.png"))
        self.picitem15.setScaledContents(True)
        self.picitem15.setObjectName("picitem15")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(680, 200, 20, 671))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.item15 = QtWidgets.QLabel(self.centralwidget)
        self.item15.setGeometry(QtCore.QRect(590, 180, 101, 20))
        self.item15.setObjectName("item15")
        self.picitem16 = QtWidgets.QLabel(self.centralwidget)
        self.picitem16.setGeometry(QtCore.QRect(700, 210, 81, 41))
        self.picitem16.setText("")
        self.picitem16.setPixmap(QtGui.QPixmap("item/1027.png"))
        self.picitem16.setScaledContents(True)
        self.picitem16.setObjectName("picitem16")
        self.item16 = QtWidgets.QLabel(self.centralwidget)
        self.item16.setGeometry(QtCore.QRect(690, 180, 101, 20))
        self.item16.setObjectName("item16")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(790, 200, 16, 691))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.winlose1 = QtWidgets.QLabel(self.centralwidget)
        self.winlose1.setGeometry(QtCore.QRect(100, 210, 81, 41))
        self.winlose1.setObjectName("winlose1")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(870, 200, 16, 681))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(1070, 200, 16, 771))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(0, 320, 1071, 16))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.winlose2 = QtWidgets.QLabel(self.centralwidget)
        self.winlose2.setGeometry(QtCore.QRect(100, 270, 81, 41))
        self.winlose2.setObjectName("winlose2")
        self.item21 = QtWidgets.QLabel(self.centralwidget)
        self.item21.setGeometry(QtCore.QRect(190, 260, 101, 20))
        self.item21.setObjectName("item21")
        self.picitem21 = QtWidgets.QLabel(self.centralwidget)
        self.picitem21.setGeometry(QtCore.QRect(200, 280, 81, 41))
        self.picitem21.setText("")
        self.picitem21.setPixmap(QtGui.QPixmap("item/2422.png"))
        self.picitem21.setScaledContents(True)
        self.picitem21.setObjectName("picitem21")
        self.picitem22 = QtWidgets.QLabel(self.centralwidget)
        self.picitem22.setGeometry(QtCore.QRect(300, 280, 81, 41))
        self.picitem22.setText("")
        self.picitem22.setPixmap(QtGui.QPixmap("item/3053.png"))
        self.picitem22.setScaledContents(True)
        self.picitem22.setObjectName("picitem22")
        self.item22 = QtWidgets.QLabel(self.centralwidget)
        self.item22.setGeometry(QtCore.QRect(290, 260, 101, 20))
        self.item22.setObjectName("item22")
        self.picitem23 = QtWidgets.QLabel(self.centralwidget)
        self.picitem23.setGeometry(QtCore.QRect(400, 280, 81, 41))
        self.picitem23.setText("")
        self.picitem23.setPixmap(QtGui.QPixmap("item/1037.png"))
        self.picitem23.setScaledContents(True)
        self.picitem23.setObjectName("picitem23")
        self.item23 = QtWidgets.QLabel(self.centralwidget)
        self.item23.setGeometry(QtCore.QRect(390, 260, 101, 20))
        self.item23.setObjectName("item23")
        self.picitem24 = QtWidgets.QLabel(self.centralwidget)
        self.picitem24.setGeometry(QtCore.QRect(500, 280, 81, 41))
        self.picitem24.setText("")
        self.picitem24.setPixmap(QtGui.QPixmap("item/1029.png"))
        self.picitem24.setScaledContents(True)
        self.picitem24.setObjectName("picitem24")
        self.item24 = QtWidgets.QLabel(self.centralwidget)
        self.item24.setGeometry(QtCore.QRect(490, 260, 101, 20))
        self.item24.setObjectName("item24")
        self.picitem25 = QtWidgets.QLabel(self.centralwidget)
        self.picitem25.setGeometry(QtCore.QRect(600, 280, 81, 41))
        self.picitem25.setText("")
        self.picitem25.setPixmap(QtGui.QPixmap("item/1035.png"))
        self.picitem25.setScaledContents(True)
        self.picitem25.setObjectName("picitem25")
        self.item25 = QtWidgets.QLabel(self.centralwidget)
        self.item25.setGeometry(QtCore.QRect(590, 260, 101, 20))
        self.item25.setObjectName("item25")
        self.picitem26 = QtWidgets.QLabel(self.centralwidget)
        self.picitem26.setGeometry(QtCore.QRect(700, 280, 81, 41))
        self.picitem26.setText("")
        self.picitem26.setPixmap(QtGui.QPixmap("item/4637.png"))
        self.picitem26.setScaledContents(True)
        self.picitem26.setObjectName("picitem26")
        self.item26 = QtWidgets.QLabel(self.centralwidget)
        self.item26.setGeometry(QtCore.QRect(700, 260, 101, 20))
        self.item26.setObjectName("item26")
        self.kda1 = QtWidgets.QLabel(self.centralwidget)
        self.kda1.setGeometry(QtCore.QRect(810, 210, 51, 41))
        self.kda1.setObjectName("kda1")
        self.descreption2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.descreption2.setGeometry(QtCore.QRect(880, 270, 191, 51))
        self.descreption2.setAutoFillBackground(False)
        self.descreption2.setStyleSheet("border-color: rgb(85, 255, 0);")
        self.descreption2.setObjectName("descreption2")
        self.winlose3 = QtWidgets.QLabel(self.centralwidget)
        self.winlose3.setGeometry(QtCore.QRect(100, 340, 81, 41))
        self.winlose3.setObjectName("winlose3")
        self.picitem31 = QtWidgets.QLabel(self.centralwidget)
        self.picitem31.setGeometry(QtCore.QRect(200, 350, 81, 41))
        self.picitem31.setText("")
        self.picitem31.setPixmap(QtGui.QPixmap("item/2052.png"))
        self.picitem31.setScaledContents(True)
        self.picitem31.setObjectName("picitem31")
        self.item31 = QtWidgets.QLabel(self.centralwidget)
        self.item31.setGeometry(QtCore.QRect(190, 330, 101, 20))
        self.item31.setObjectName("item31")
        self.item32 = QtWidgets.QLabel(self.centralwidget)
        self.item32.setGeometry(QtCore.QRect(290, 330, 101, 20))
        self.item32.setObjectName("item32")
        self.picitem32 = QtWidgets.QLabel(self.centralwidget)
        self.picitem32.setGeometry(QtCore.QRect(300, 350, 81, 41))
        self.picitem32.setText("")
        self.picitem32.setPixmap(QtGui.QPixmap("item/2051.png"))
        self.picitem32.setScaledContents(True)
        self.picitem32.setObjectName("picitem32")
        self.item33 = QtWidgets.QLabel(self.centralwidget)
        self.item33.setGeometry(QtCore.QRect(390, 330, 101, 20))
        self.item33.setObjectName("item33")
        self.item34 = QtWidgets.QLabel(self.centralwidget)
        self.item34.setGeometry(QtCore.QRect(490, 330, 101, 20))
        self.item34.setObjectName("item34")
        self.item35 = QtWidgets.QLabel(self.centralwidget)
        self.item35.setGeometry(QtCore.QRect(590, 330, 101, 20))
        self.item35.setObjectName("item35")
        self.item36 = QtWidgets.QLabel(self.centralwidget)
        self.item36.setGeometry(QtCore.QRect(690, 330, 101, 20))
        self.item36.setObjectName("item36")
        self.picitem33 = QtWidgets.QLabel(self.centralwidget)
        self.picitem33.setGeometry(QtCore.QRect(400, 350, 81, 41))
        self.picitem33.setText("")
        self.picitem33.setPixmap(QtGui.QPixmap("item/1083.png"))
        self.picitem33.setScaledContents(True)
        self.picitem33.setObjectName("picitem33")
        self.picitem34 = QtWidgets.QLabel(self.centralwidget)
        self.picitem34.setGeometry(QtCore.QRect(500, 350, 81, 41))
        self.picitem34.setText("")
        self.picitem34.setPixmap(QtGui.QPixmap("item/1026.png"))
        self.picitem34.setScaledContents(True)
        self.picitem34.setObjectName("picitem34")
        self.picitem35 = QtWidgets.QLabel(self.centralwidget)
        self.picitem35.setGeometry(QtCore.QRect(600, 350, 81, 41))
        self.picitem35.setText("")
        self.picitem35.setPixmap(QtGui.QPixmap("item/1035.png"))
        self.picitem35.setScaledContents(True)
        self.picitem35.setObjectName("picitem35")
        self.picitem36 = QtWidgets.QLabel(self.centralwidget)
        self.picitem36.setGeometry(QtCore.QRect(700, 350, 81, 41))
        self.picitem36.setText("")
        self.picitem36.setPixmap(QtGui.QPixmap("item/1058.png"))
        self.picitem36.setScaledContents(True)
        self.picitem36.setObjectName("picitem36")
        self.kda3 = QtWidgets.QLabel(self.centralwidget)
        self.kda3.setGeometry(QtCore.QRect(810, 340, 51, 41))
        self.kda3.setObjectName("kda3")
        self.descreption3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.descreption3.setGeometry(QtCore.QRect(880, 340, 201, 51))
        self.descreption3.setAutoFillBackground(False)
        self.descreption3.setStyleSheet("border-color: rgb(85, 255, 0);")
        self.descreption3.setObjectName("descreption3")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(0, 390, 1081, 16))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.winlose4 = QtWidgets.QLabel(self.centralwidget)
        self.winlose4.setGeometry(QtCore.QRect(100, 410, 81, 41))
        self.winlose4.setObjectName("winlose4")
        self.item41 = QtWidgets.QLabel(self.centralwidget)
        self.item41.setGeometry(QtCore.QRect(190, 400, 101, 20))
        self.item41.setObjectName("item41")
        self.picitem41 = QtWidgets.QLabel(self.centralwidget)
        self.picitem41.setGeometry(QtCore.QRect(200, 420, 81, 41))
        self.picitem41.setText("")
        self.picitem41.setPixmap(QtGui.QPixmap("item/1026.png"))
        self.picitem41.setScaledContents(True)
        self.picitem41.setObjectName("picitem41")
        self.item42 = QtWidgets.QLabel(self.centralwidget)
        self.item42.setGeometry(QtCore.QRect(290, 400, 101, 20))
        self.item42.setObjectName("item42")
        self.item43 = QtWidgets.QLabel(self.centralwidget)
        self.item43.setGeometry(QtCore.QRect(390, 400, 101, 20))
        self.item43.setObjectName("item43")
        self.item44 = QtWidgets.QLabel(self.centralwidget)
        self.item44.setGeometry(QtCore.QRect(490, 400, 101, 20))
        self.item44.setObjectName("item44")
        self.item45 = QtWidgets.QLabel(self.centralwidget)
        self.item45.setGeometry(QtCore.QRect(590, 400, 101, 20))
        self.item45.setObjectName("item45")
        self.item46 = QtWidgets.QLabel(self.centralwidget)
        self.item46.setGeometry(QtCore.QRect(690, 400, 101, 20))
        self.item46.setObjectName("item46")
        self.picitem42 = QtWidgets.QLabel(self.centralwidget)
        self.picitem42.setGeometry(QtCore.QRect(300, 420, 81, 41))
        self.picitem42.setText("")
        self.picitem42.setPixmap(QtGui.QPixmap("item/1027.png"))
        self.picitem42.setScaledContents(True)
        self.picitem42.setObjectName("picitem42")
        self.picitem43 = QtWidgets.QLabel(self.centralwidget)
        self.picitem43.setGeometry(QtCore.QRect(400, 420, 81, 41))
        self.picitem43.setText("")
        self.picitem43.setPixmap(QtGui.QPixmap("item/1018.png"))
        self.picitem43.setScaledContents(True)
        self.picitem43.setObjectName("picitem43")
        self.picitem44 = QtWidgets.QLabel(self.centralwidget)
        self.picitem44.setGeometry(QtCore.QRect(500, 420, 81, 41))
        self.picitem44.setText("")
        self.picitem44.setPixmap(QtGui.QPixmap("item/1001.png"))
        self.picitem44.setScaledContents(True)
        self.picitem44.setObjectName("picitem44")
        self.picitem45 = QtWidgets.QLabel(self.centralwidget)
        self.picitem45.setGeometry(QtCore.QRect(600, 420, 81, 41))
        self.picitem45.setText("")
        self.picitem45.setPixmap(QtGui.QPixmap("item/3157.png"))
        self.picitem45.setScaledContents(True)
        self.picitem45.setObjectName("picitem45")
        self.picitem46 = QtWidgets.QLabel(self.centralwidget)
        self.picitem46.setGeometry(QtCore.QRect(700, 420, 81, 41))
        self.picitem46.setText("")
        self.picitem46.setPixmap(QtGui.QPixmap("item/3142.png"))
        self.picitem46.setScaledContents(True)
        self.picitem46.setObjectName("picitem46")
        self.kda4 = QtWidgets.QLabel(self.centralwidget)
        self.kda4.setGeometry(QtCore.QRect(810, 410, 51, 41))
        self.kda4.setObjectName("kda4")
        self.descreption4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.descreption4.setGeometry(QtCore.QRect(880, 410, 201, 51))
        self.descreption4.setAutoFillBackground(False)
        self.descreption4.setStyleSheet("border-color: rgb(85, 255, 0);")
        self.descreption4.setObjectName("descreption4")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(10, 460, 1071, 16))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.champ_pic5 = QtWidgets.QLabel(self.centralwidget)
        self.champ_pic5.setGeometry(QtCore.QRect(10, 480, 71, 41))
        self.champ_pic5.setText("")
        self.champ_pic5.setPixmap(QtGui.QPixmap("champion/tiles/Ahri_0.jpg"))
        self.champ_pic5.setScaledContents(True)
        self.champ_pic5.setObjectName("champ_pic5")
        self.winlose5 = QtWidgets.QLabel(self.centralwidget)
        self.winlose5.setGeometry(QtCore.QRect(100, 480, 81, 41))
        self.winlose5.setObjectName("winlose5")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(10, 530, 1071, 16))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.item51 = QtWidgets.QLabel(self.centralwidget)
        self.item51.setGeometry(QtCore.QRect(190, 470, 101, 20))
        self.item51.setObjectName("item51")
        self.item52 = QtWidgets.QLabel(self.centralwidget)
        self.item52.setGeometry(QtCore.QRect(290, 470, 101, 20))
        self.item52.setObjectName("item52")
        self.item53 = QtWidgets.QLabel(self.centralwidget)
        self.item53.setGeometry(QtCore.QRect(390, 470, 101, 20))
        self.item53.setObjectName("item53")
        self.item54 = QtWidgets.QLabel(self.centralwidget)
        self.item54.setGeometry(QtCore.QRect(490, 470, 101, 20))
        self.item54.setObjectName("item54")
        self.item55 = QtWidgets.QLabel(self.centralwidget)
        self.item55.setGeometry(QtCore.QRect(590, 470, 101, 20))
        self.item55.setObjectName("item55")
        self.item56 = QtWidgets.QLabel(self.centralwidget)
        self.item56.setGeometry(QtCore.QRect(690, 470, 101, 20))
        self.item56.setObjectName("item56")
        self.kda5 = QtWidgets.QLabel(self.centralwidget)
        self.kda5.setGeometry(QtCore.QRect(810, 480, 51, 41))
        self.kda5.setObjectName("kda5")
        self.descreption5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.descreption5.setGeometry(QtCore.QRect(880, 480, 201, 51))
        self.descreption5.setAutoFillBackground(False)
        self.descreption5.setStyleSheet("border-color: rgb(85, 255, 0);")
        self.descreption5.setObjectName("descreption5")
        self.picitem51 = QtWidgets.QLabel(self.centralwidget)
        self.picitem51.setGeometry(QtCore.QRect(200, 490, 81, 41))
        self.picitem51.setText("")
        self.picitem51.setPixmap(QtGui.QPixmap("item/2033.png"))
        self.picitem51.setScaledContents(True)
        self.picitem51.setObjectName("picitem51")
        self.picitem52 = QtWidgets.QLabel(self.centralwidget)
        self.picitem52.setGeometry(QtCore.QRect(300, 490, 81, 41))
        self.picitem52.setText("")
        self.picitem52.setPixmap(QtGui.QPixmap("item/3001.png"))
        self.picitem52.setScaledContents(True)
        self.picitem52.setObjectName("picitem52")
        self.champ_pic4 = QtWidgets.QLabel(self.centralwidget)
        self.champ_pic4.setGeometry(QtCore.QRect(10, 410, 71, 41))
        self.champ_pic4.setText("")
        self.champ_pic4.setPixmap(QtGui.QPixmap("champion/tiles/Aatrox_0.jpg"))
        self.champ_pic4.setScaledContents(True)
        self.champ_pic4.setObjectName("champ_pic4")
        self.champ_pic3 = QtWidgets.QLabel(self.centralwidget)
        self.champ_pic3.setGeometry(QtCore.QRect(10, 340, 71, 41))
        self.champ_pic3.setText("")
        self.champ_pic3.setPixmap(QtGui.QPixmap("champion/tiles/Aatrox_0.jpg"))
        self.champ_pic3.setScaledContents(True)
        self.champ_pic3.setObjectName("champ_pic3")
        self.champ_pic2 = QtWidgets.QLabel(self.centralwidget)
        self.champ_pic2.setGeometry(QtCore.QRect(10, 270, 71, 41))
        self.champ_pic2.setText("")
        self.champ_pic2.setPixmap(QtGui.QPixmap("champion/tiles/Aatrox_0.jpg"))
        self.champ_pic2.setScaledContents(True)
        self.champ_pic2.setObjectName("champ_pic2")
        self.champ_pic1 = QtWidgets.QLabel(self.centralwidget)
        self.champ_pic1.setGeometry(QtCore.QRect(10, 210, 71, 41))
        self.champ_pic1.setText("")
        self.champ_pic1.setPixmap(QtGui.QPixmap("champion/tiles/Aatrox_0.jpg"))
        self.champ_pic1.setScaledContents(True)
        self.champ_pic1.setObjectName("champ_pic1")
        self.picitem53 = QtWidgets.QLabel(self.centralwidget)
        self.picitem53.setGeometry(QtCore.QRect(400, 490, 81, 41))
        self.picitem53.setText("")
        self.picitem53.setPixmap(QtGui.QPixmap("item/1053.png"))
        self.picitem53.setScaledContents(True)
        self.picitem53.setObjectName("picitem53")
        self.picitem54 = QtWidgets.QLabel(self.centralwidget)
        self.picitem54.setGeometry(QtCore.QRect(500, 490, 81, 41))
        self.picitem54.setText("")
        self.picitem54.setPixmap(QtGui.QPixmap("item/1058.png"))
        self.picitem54.setScaledContents(True)
        self.picitem54.setObjectName("picitem54")
        self.picitem55 = QtWidgets.QLabel(self.centralwidget)
        self.picitem55.setGeometry(QtCore.QRect(600, 490, 81, 41))
        self.picitem55.setText("")
        self.picitem55.setPixmap(QtGui.QPixmap("item/1006.png"))
        self.picitem55.setScaledContents(True)
        self.picitem55.setObjectName("picitem55")
        self.picitem56 = QtWidgets.QLabel(self.centralwidget)
        self.picitem56.setGeometry(QtCore.QRect(700, 490, 81, 41))
        self.picitem56.setText("")
        self.picitem56.setPixmap(QtGui.QPixmap("item/1033.png"))
        self.picitem56.setScaledContents(True)
        self.picitem56.setObjectName("picitem56")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(10, 600, 1071, 16))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.champ_pic6 = QtWidgets.QLabel(self.centralwidget)
        self.champ_pic6.setGeometry(QtCore.QRect(10, 550, 71, 41))
        self.champ_pic6.setText("")
        self.champ_pic6.setPixmap(QtGui.QPixmap("champion/tiles/Aatrox_0.jpg"))
        self.champ_pic6.setScaledContents(True)
        self.champ_pic6.setObjectName("champ_pic6")
        self.winlose6 = QtWidgets.QLabel(self.centralwidget)
        self.winlose6.setGeometry(QtCore.QRect(100, 550, 81, 41))
        self.winlose6.setObjectName("winlose6")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(10, 670, 1071, 16))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(10, 740, 1071, 16))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.item61 = QtWidgets.QLabel(self.centralwidget)
        self.item61.setGeometry(QtCore.QRect(190, 540, 101, 20))
        self.item61.setObjectName("item61")
        self.picitem61 = QtWidgets.QLabel(self.centralwidget)
        self.picitem61.setGeometry(QtCore.QRect(200, 560, 81, 41))
        self.picitem61.setText("")
        self.picitem61.setPixmap(QtGui.QPixmap("item/1036.png"))
        self.picitem61.setScaledContents(True)
        self.picitem61.setObjectName("picitem61")
        self.item62 = QtWidgets.QLabel(self.centralwidget)
        self.item62.setGeometry(QtCore.QRect(290, 540, 101, 20))
        self.item62.setObjectName("item62")
        self.picitem62 = QtWidgets.QLabel(self.centralwidget)
        self.picitem62.setGeometry(QtCore.QRect(300, 560, 81, 41))
        self.picitem62.setText("")
        self.picitem62.setPixmap(QtGui.QPixmap("item/2424.png"))
        self.picitem62.setScaledContents(True)
        self.picitem62.setObjectName("picitem62")
        self.item63 = QtWidgets.QLabel(self.centralwidget)
        self.item63.setGeometry(QtCore.QRect(390, 540, 101, 20))
        self.item63.setObjectName("item63")
        self.item64 = QtWidgets.QLabel(self.centralwidget)
        self.item64.setGeometry(QtCore.QRect(490, 540, 101, 20))
        self.item64.setObjectName("item64")
        self.item65 = QtWidgets.QLabel(self.centralwidget)
        self.item65.setGeometry(QtCore.QRect(590, 540, 101, 20))
        self.item65.setObjectName("item65")
        self.item66 = QtWidgets.QLabel(self.centralwidget)
        self.item66.setGeometry(QtCore.QRect(690, 540, 101, 20))
        self.item66.setObjectName("item66")
        self.kda6 = QtWidgets.QLabel(self.centralwidget)
        self.kda6.setGeometry(QtCore.QRect(810, 550, 51, 41))
        self.kda6.setObjectName("kda6")
        self.descreption6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.descreption6.setGeometry(QtCore.QRect(880, 550, 201, 51))
        self.descreption6.setAutoFillBackground(False)
        self.descreption6.setStyleSheet("border-color: rgb(85, 255, 0);")
        self.descreption6.setObjectName("descreption6")
        self.picitem63 = QtWidgets.QLabel(self.centralwidget)
        self.picitem63.setGeometry(QtCore.QRect(400, 560, 81, 41))
        self.picitem63.setText("")
        self.picitem63.setPixmap(QtGui.QPixmap("item/1042.png"))
        self.picitem63.setScaledContents(True)
        self.picitem63.setObjectName("picitem63")
        self.picitem64 = QtWidgets.QLabel(self.centralwidget)
        self.picitem64.setGeometry(QtCore.QRect(500, 560, 81, 41))
        self.picitem64.setText("")
        self.picitem64.setPixmap(QtGui.QPixmap("item/3024.png"))
        self.picitem64.setScaledContents(True)
        self.picitem64.setObjectName("picitem64")
        self.picitem65 = QtWidgets.QLabel(self.centralwidget)
        self.picitem65.setGeometry(QtCore.QRect(600, 560, 81, 41))
        self.picitem65.setText("")
        self.picitem65.setPixmap(QtGui.QPixmap("item/2140.png"))
        self.picitem65.setScaledContents(True)
        self.picitem65.setObjectName("picitem65")
        self.picitem66 = QtWidgets.QLabel(self.centralwidget)
        self.picitem66.setGeometry(QtCore.QRect(700, 560, 81, 41))
        self.picitem66.setText("")
        self.picitem66.setPixmap(QtGui.QPixmap("item/2403.png"))
        self.picitem66.setScaledContents(True)
        self.picitem66.setObjectName("picitem66")
        self.champ_pic7 = QtWidgets.QLabel(self.centralwidget)
        self.champ_pic7.setGeometry(QtCore.QRect(10, 620, 71, 41))
        self.champ_pic7.setText("")
        self.champ_pic7.setPixmap(QtGui.QPixmap("champion/tiles/Alistar_0.jpg"))
        self.champ_pic7.setScaledContents(True)
        self.champ_pic7.setObjectName("champ_pic7")
        self.winlose7 = QtWidgets.QLabel(self.centralwidget)
        self.winlose7.setGeometry(QtCore.QRect(100, 620, 81, 41))
        self.winlose7.setObjectName("winlose7")
        self.item71 = QtWidgets.QLabel(self.centralwidget)
        self.item71.setGeometry(QtCore.QRect(190, 610, 101, 20))
        self.item71.setObjectName("item71")
        self.item72 = QtWidgets.QLabel(self.centralwidget)
        self.item72.setGeometry(QtCore.QRect(290, 610, 101, 20))
        self.item72.setObjectName("item72")
        self.item73 = QtWidgets.QLabel(self.centralwidget)
        self.item73.setGeometry(QtCore.QRect(390, 610, 101, 20))
        self.item73.setObjectName("item73")
        self.item74 = QtWidgets.QLabel(self.centralwidget)
        self.item74.setGeometry(QtCore.QRect(490, 610, 101, 20))
        self.item74.setObjectName("item74")
        self.item75 = QtWidgets.QLabel(self.centralwidget)
        self.item75.setGeometry(QtCore.QRect(590, 610, 101, 20))
        self.item75.setObjectName("item75")
        self.item76 = QtWidgets.QLabel(self.centralwidget)
        self.item76.setGeometry(QtCore.QRect(690, 610, 101, 20))
        self.item76.setObjectName("item76")
        self.kda7 = QtWidgets.QLabel(self.centralwidget)
        self.kda7.setGeometry(QtCore.QRect(810, 620, 51, 41))
        self.kda7.setObjectName("kda7")
        self.picitem71 = QtWidgets.QLabel(self.centralwidget)
        self.picitem71.setGeometry(QtCore.QRect(200, 630, 81, 41))
        self.picitem71.setText("")
        self.picitem71.setPixmap(QtGui.QPixmap("item/2055.png"))
        self.picitem71.setScaledContents(True)
        self.picitem71.setObjectName("picitem71")
        self.picitem72 = QtWidgets.QLabel(self.centralwidget)
        self.picitem72.setGeometry(QtCore.QRect(300, 630, 81, 41))
        self.picitem72.setText("")
        self.picitem72.setPixmap(QtGui.QPixmap("item/3026.png"))
        self.picitem72.setScaledContents(True)
        self.picitem72.setObjectName("picitem72")
        self.picitem73 = QtWidgets.QLabel(self.centralwidget)
        self.picitem73.setGeometry(QtCore.QRect(400, 630, 81, 41))
        self.picitem73.setText("")
        self.picitem73.setPixmap(QtGui.QPixmap("item/3050.png"))
        self.picitem73.setScaledContents(True)
        self.picitem73.setObjectName("picitem73")
        self.picitem74 = QtWidgets.QLabel(self.centralwidget)
        self.picitem74.setGeometry(QtCore.QRect(500, 630, 81, 41))
        self.picitem74.setText("")
        self.picitem74.setPixmap(QtGui.QPixmap("item/2031.png"))
        self.picitem74.setScaledContents(True)
        self.picitem74.setObjectName("picitem74")
        self.picitem75 = QtWidgets.QLabel(self.centralwidget)
        self.picitem75.setGeometry(QtCore.QRect(600, 630, 81, 41))
        self.picitem75.setText("")
        self.picitem75.setPixmap(QtGui.QPixmap("item/2139.png"))
        self.picitem75.setScaledContents(True)
        self.picitem75.setObjectName("picitem75")
        self.picitem76 = QtWidgets.QLabel(self.centralwidget)
        self.picitem76.setGeometry(QtCore.QRect(700, 630, 81, 41))
        self.picitem76.setText("")
        self.picitem76.setPixmap(QtGui.QPixmap("item/3001.png"))
        self.picitem76.setScaledContents(True)
        self.picitem76.setObjectName("picitem76")
        self.descreption7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.descreption7.setGeometry(QtCore.QRect(880, 620, 201, 51))
        self.descreption7.setAutoFillBackground(False)
        self.descreption7.setStyleSheet("border-color: rgb(85, 255, 0);")
        self.descreption7.setObjectName("descreption7")
        self.champ_pic8 = QtWidgets.QLabel(self.centralwidget)
        self.champ_pic8.setGeometry(QtCore.QRect(10, 690, 71, 41))
        self.champ_pic8.setText("")
        self.champ_pic8.setPixmap(QtGui.QPixmap("champion/tiles/Syndra_0.jpg"))
        self.champ_pic8.setScaledContents(True)
        self.champ_pic8.setObjectName("champ_pic8")
        self.winlose8 = QtWidgets.QLabel(self.centralwidget)
        self.winlose8.setGeometry(QtCore.QRect(100, 690, 81, 41))
        self.winlose8.setObjectName("winlose8")
        self.item81 = QtWidgets.QLabel(self.centralwidget)
        self.item81.setGeometry(QtCore.QRect(190, 680, 101, 20))
        self.item81.setObjectName("item81")
        self.item82 = QtWidgets.QLabel(self.centralwidget)
        self.item82.setGeometry(QtCore.QRect(290, 680, 101, 20))
        self.item82.setObjectName("item82")
        self.item83 = QtWidgets.QLabel(self.centralwidget)
        self.item83.setGeometry(QtCore.QRect(390, 680, 101, 20))
        self.item83.setObjectName("item83")
        self.item84 = QtWidgets.QLabel(self.centralwidget)
        self.item84.setGeometry(QtCore.QRect(490, 680, 101, 20))
        self.item84.setObjectName("item84")
        self.item85 = QtWidgets.QLabel(self.centralwidget)
        self.item85.setGeometry(QtCore.QRect(590, 680, 101, 20))
        self.item85.setObjectName("item85")
        self.item86 = QtWidgets.QLabel(self.centralwidget)
        self.item86.setGeometry(QtCore.QRect(690, 680, 101, 20))
        self.item86.setObjectName("item86")
        self.picitem81 = QtWidgets.QLabel(self.centralwidget)
        self.picitem81.setGeometry(QtCore.QRect(200, 700, 81, 41))
        self.picitem81.setText("")
        self.picitem81.setPixmap(QtGui.QPixmap("item/3091.png"))
        self.picitem81.setScaledContents(True)
        self.picitem81.setObjectName("picitem81")
        self.picitem82 = QtWidgets.QLabel(self.centralwidget)
        self.picitem82.setGeometry(QtCore.QRect(300, 700, 81, 41))
        self.picitem82.setText("")
        self.picitem82.setPixmap(QtGui.QPixmap("item/3003.png"))
        self.picitem82.setScaledContents(True)
        self.picitem82.setObjectName("picitem82")
        self.picitem83 = QtWidgets.QLabel(self.centralwidget)
        self.picitem83.setGeometry(QtCore.QRect(400, 700, 81, 41))
        self.picitem83.setText("")
        self.picitem83.setPixmap(QtGui.QPixmap("item/3094.png"))
        self.picitem83.setScaledContents(True)
        self.picitem83.setObjectName("picitem83")
        self.picitem84 = QtWidgets.QLabel(self.centralwidget)
        self.picitem84.setGeometry(QtCore.QRect(500, 700, 81, 41))
        self.picitem84.setText("")
        self.picitem84.setPixmap(QtGui.QPixmap("item/2139.png"))
        self.picitem84.setScaledContents(True)
        self.picitem84.setObjectName("picitem84")
        self.picitem85 = QtWidgets.QLabel(self.centralwidget)
        self.picitem85.setGeometry(QtCore.QRect(600, 700, 81, 41))
        self.picitem85.setText("")
        self.picitem85.setPixmap(QtGui.QPixmap("item/2140.png"))
        self.picitem85.setScaledContents(True)
        self.picitem85.setObjectName("picitem85")
        self.picitem86 = QtWidgets.QLabel(self.centralwidget)
        self.picitem86.setGeometry(QtCore.QRect(700, 700, 81, 41))
        self.picitem86.setText("")
        self.picitem86.setPixmap(QtGui.QPixmap("item/3053.png"))
        self.picitem86.setScaledContents(True)
        self.picitem86.setObjectName("picitem86")
        self.kda8 = QtWidgets.QLabel(self.centralwidget)
        self.kda8.setGeometry(QtCore.QRect(810, 690, 51, 41))
        self.kda8.setObjectName("kda8")
        self.descreption8 = QtWidgets.QTextBrowser(self.centralwidget)
        self.descreption8.setGeometry(QtCore.QRect(880, 690, 201, 51))
        self.descreption8.setAutoFillBackground(False)
        self.descreption8.setStyleSheet("border-color: rgb(85, 255, 0);")
        self.descreption8.setObjectName("descreption8")
        self.champ_pic9 = QtWidgets.QLabel(self.centralwidget)
        self.champ_pic9.setGeometry(QtCore.QRect(10, 760, 71, 41))
        self.champ_pic9.setText("")
        self.champ_pic9.setPixmap(QtGui.QPixmap("champion/tiles/Zyra_0.jpg"))
        self.champ_pic9.setScaledContents(True)
        self.champ_pic9.setObjectName("champ_pic9")
        self.winlose9 = QtWidgets.QLabel(self.centralwidget)
        self.winlose9.setGeometry(QtCore.QRect(100, 760, 81, 41))
        self.winlose9.setObjectName("winlose9")
        self.item91 = QtWidgets.QLabel(self.centralwidget)
        self.item91.setGeometry(QtCore.QRect(190, 750, 101, 20))
        self.item91.setObjectName("item91")
        self.item92 = QtWidgets.QLabel(self.centralwidget)
        self.item92.setGeometry(QtCore.QRect(290, 750, 101, 20))
        self.item92.setObjectName("item92")
        self.item93 = QtWidgets.QLabel(self.centralwidget)
        self.item93.setGeometry(QtCore.QRect(390, 750, 101, 20))
        self.item93.setObjectName("item93")
        self.item94 = QtWidgets.QLabel(self.centralwidget)
        self.item94.setGeometry(QtCore.QRect(490, 750, 101, 20))
        self.item94.setObjectName("item94")
        self.item95 = QtWidgets.QLabel(self.centralwidget)
        self.item95.setGeometry(QtCore.QRect(590, 750, 101, 20))
        self.item95.setObjectName("item95")
        self.item96 = QtWidgets.QLabel(self.centralwidget)
        self.item96.setGeometry(QtCore.QRect(690, 750, 101, 20))
        self.item96.setObjectName("item96")
        self.kda9 = QtWidgets.QLabel(self.centralwidget)
        self.kda9.setGeometry(QtCore.QRect(810, 760, 51, 41))
        self.kda9.setObjectName("kda9")
        self.descreption9 = QtWidgets.QTextBrowser(self.centralwidget)
        self.descreption9.setGeometry(QtCore.QRect(880, 760, 201, 51))
        self.descreption9.setAutoFillBackground(False)
        self.descreption9.setStyleSheet("border-color: rgb(85, 255, 0);")
        self.descreption9.setObjectName("descreption9")
        self.picitem91 = QtWidgets.QLabel(self.centralwidget)
        self.picitem91.setGeometry(QtCore.QRect(200, 770, 81, 41))
        self.picitem91.setText("")
        self.picitem91.setPixmap(QtGui.QPixmap("item/2015.png"))
        self.picitem91.setScaledContents(True)
        self.picitem91.setObjectName("picitem91")
        self.picitem92 = QtWidgets.QLabel(self.centralwidget)
        self.picitem92.setGeometry(QtCore.QRect(300, 770, 81, 41))
        self.picitem92.setText("")
        self.picitem92.setPixmap(QtGui.QPixmap("item/1039.png"))
        self.picitem92.setScaledContents(True)
        self.picitem92.setObjectName("picitem92")
        self.picitem93 = QtWidgets.QLabel(self.centralwidget)
        self.picitem93.setGeometry(QtCore.QRect(400, 770, 81, 41))
        self.picitem93.setText("")
        self.picitem93.setPixmap(QtGui.QPixmap("item/3035.png"))
        self.picitem93.setScaledContents(True)
        self.picitem93.setObjectName("picitem93")
        self.picitem94 = QtWidgets.QLabel(self.centralwidget)
        self.picitem94.setGeometry(QtCore.QRect(500, 770, 81, 41))
        self.picitem94.setText("")
        self.picitem94.setPixmap(QtGui.QPixmap("item/1035.png"))
        self.picitem94.setScaledContents(True)
        self.picitem94.setObjectName("picitem94")
        self.picitem95 = QtWidgets.QLabel(self.centralwidget)
        self.picitem95.setGeometry(QtCore.QRect(600, 770, 81, 41))
        self.picitem95.setText("")
        self.picitem95.setPixmap(QtGui.QPixmap("item/3076.png"))
        self.picitem95.setScaledContents(True)
        self.picitem95.setObjectName("picitem95")
        self.picitem96 = QtWidgets.QLabel(self.centralwidget)
        self.picitem96.setGeometry(QtCore.QRect(700, 770, 81, 41))
        self.picitem96.setText("")
        self.picitem96.setPixmap(QtGui.QPixmap("item/3040.png"))
        self.picitem96.setScaledContents(True)
        self.picitem96.setObjectName("picitem96")
        self.descreption1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.descreption1.setGeometry(QtCore.QRect(880, 200, 191, 51))
        self.descreption1.setAutoFillBackground(False)
        self.descreption1.setStyleSheet("border-color: rgb(85, 255, 0);")
        self.descreption1.setObjectName("descreption1")
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setGeometry(QtCore.QRect(0, 805, 1071, 16))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.champ_pic10 = QtWidgets.QLabel(self.centralwidget)
        self.champ_pic10.setGeometry(QtCore.QRect(10, 830, 71, 41))
        self.champ_pic10.setText("")
        self.champ_pic10.setPixmap(QtGui.QPixmap("champion/tiles/Nidalee_11.jpg"))
        self.champ_pic10.setScaledContents(True)
        self.champ_pic10.setObjectName("champ_pic10")
        self.winlose10 = QtWidgets.QLabel(self.centralwidget)
        self.winlose10.setGeometry(QtCore.QRect(100, 830, 81, 41))
        self.winlose10.setObjectName("winlose10")
        self.item101 = QtWidgets.QLabel(self.centralwidget)
        self.item101.setGeometry(QtCore.QRect(190, 815, 101, 20))
        self.item101.setObjectName("item101")
        self.picitem101 = QtWidgets.QLabel(self.centralwidget)
        self.picitem101.setGeometry(QtCore.QRect(200, 835, 81, 41))
        self.picitem101.setText("")
        self.picitem101.setPixmap(QtGui.QPixmap("item/3078.png"))
        self.picitem101.setScaledContents(True)
        self.picitem101.setObjectName("picitem101")
        self.item102 = QtWidgets.QLabel(self.centralwidget)
        self.item102.setGeometry(QtCore.QRect(290, 815, 101, 20))
        self.item102.setObjectName("item102")
        self.item103 = QtWidgets.QLabel(self.centralwidget)
        self.item103.setGeometry(QtCore.QRect(390, 815, 101, 20))
        self.item103.setObjectName("item103")
        self.item104 = QtWidgets.QLabel(self.centralwidget)
        self.item104.setGeometry(QtCore.QRect(490, 815, 101, 20))
        self.item104.setObjectName("item104")
        self.item105 = QtWidgets.QLabel(self.centralwidget)
        self.item105.setGeometry(QtCore.QRect(590, 815, 101, 20))
        self.item105.setObjectName("item105")
        self.item106 = QtWidgets.QLabel(self.centralwidget)
        self.item106.setGeometry(QtCore.QRect(690, 815, 101, 20))
        self.item106.setObjectName("item106")
        self.picitem102 = QtWidgets.QLabel(self.centralwidget)
        self.picitem102.setGeometry(QtCore.QRect(300, 835, 81, 41))
        self.picitem102.setText("")
        self.picitem102.setPixmap(QtGui.QPixmap("item/3091.png"))
        self.picitem102.setScaledContents(True)
        self.picitem102.setObjectName("picitem102")
        self.picitem103 = QtWidgets.QLabel(self.centralwidget)
        self.picitem103.setGeometry(QtCore.QRect(400, 835, 81, 41))
        self.picitem103.setText("")
        self.picitem103.setPixmap(QtGui.QPixmap("item/3009.png"))
        self.picitem103.setScaledContents(True)
        self.picitem103.setObjectName("picitem103")
        self.picitem104 = QtWidgets.QLabel(self.centralwidget)
        self.picitem104.setGeometry(QtCore.QRect(500, 835, 81, 41))
        self.picitem104.setText("")
        self.picitem104.setPixmap(QtGui.QPixmap("item/3041.png"))
        self.picitem104.setScaledContents(True)
        self.picitem104.setObjectName("picitem104")
        self.picitem105 = QtWidgets.QLabel(self.centralwidget)
        self.picitem105.setGeometry(QtCore.QRect(600, 835, 81, 41))
        self.picitem105.setText("")
        self.picitem105.setPixmap(QtGui.QPixmap("item/3036.png"))
        self.picitem105.setScaledContents(True)
        self.picitem105.setObjectName("picitem105")
        self.picitem106 = QtWidgets.QLabel(self.centralwidget)
        self.picitem106.setGeometry(QtCore.QRect(700, 835, 81, 41))
        self.picitem106.setText("")
        self.picitem106.setPixmap(QtGui.QPixmap("item/2422.png"))
        self.picitem106.setScaledContents(True)
        self.picitem106.setObjectName("picitem106")
        self.kda10 = QtWidgets.QLabel(self.centralwidget)
        self.kda10.setGeometry(QtCore.QRect(810, 830, 51, 41))
        self.kda10.setObjectName("kda10")
        self.descreption10 = QtWidgets.QTextBrowser(self.centralwidget)
        self.descreption10.setGeometry(QtCore.QRect(880, 820, 201, 51))
        self.descreption10.setAutoFillBackground(False)
        self.descreption10.setStyleSheet("border-color: rgb(85, 255, 0);")
        self.descreption10.setObjectName("descreption10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        self.setgame(name)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def setgame(self,name):
        history=gethistory(name)
        df=read_csv("goldstats.csv")
        game1=datafrommatc(history[0])
        self.champ_pic1.setPixmap(QtGui.QPixmap("champion/tiles/{0}_0.jpg".format(champion_keys[str(history[0]['champion'])])))

        try:
            self.picitem11.setPixmap(QtGui.QPixmap("item/{0}.png".format(game1['Items'][0])))
            self.item11.setText(Item(str(game1['Items'][0])).name)
        except:
             self.picitem11.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item11.setText("Empty Item Slot")
        try:
            self.picitem12.setPixmap(QtGui.QPixmap("item/{0}.png".format(game1['Items'][1])))
            self.item12.setText(Item(str(game1['Items'][1])).name)
        except:
             self.picitem12.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item12.setText("Empty Item Slot")
        try:
            self.picitem13.setPixmap(QtGui.QPixmap("item/{0}.png".format(game1['Items'][2])))
            self.item13.setText(Item(str(game1['Items'][2])).name)
        except:
             self.picitem13.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item13.setText("Empty Item Slot")
        try:
            self.picitem14.setPixmap(QtGui.QPixmap("item/{0}.png".format(game1['Items'][3])))
            self.item14.setText(Item(str(game1['Items'][3])).name)
        except:
             self.picitem14.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item14.setText("Empty Item Slot")
        try:
            self.picitem15.setPixmap(QtGui.QPixmap("item/{0}.png".format(game1['Items'][4])))
            self.item15.setText(Item(str(game1['Items'][4])).name)
        except:
             self.picitem15.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item15.setText("Empty Item Slot")
        try:
            self.picitem16.setPixmap(QtGui.QPixmap("item/{0}.png".format(game1['Items'][5])))
            self.item16.setText(Item(str(game1['Items'][5])).name)
        except:
             self.picitem16.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item16.setText("Empty Item Slot")
                
        self.kda1.setText("KDA:"+str(game1['KDA']))
        championstats=df[df['id']==history[0]['champion']]
        avragekda=championstats["KDA"].values.tolist()[0]
        comperkda="KDA below avrage"
        if(avragekda<game1['KDA']):
            comperkda="KDA above average"
        avragevision=championstats["Vision"].values.tolist()[0]
        compervision="Vision below avrage"
        if(avragevision<game1['Vision']-2):
            compervision="KDA above average"
        avragecs=championstats["CS"].values.tolist()[0]
        compercs="CS below avrage"
        if(avragecs<game1['Cs']):
            compercs="CS above average"
        self.descreption1.setText(comperkda+"\n" + compervision+"\n" + compercs)
        self.winlose1.setText(game1['win/lose'])
        
        
        game2=datafrommatc(history[1])
        self.champ_pic2.setPixmap(QtGui.QPixmap("champion/tiles/{0}_0.jpg".format(champion_keys[str(history[1]['champion'])])))

        try:
            self.picitem21.setPixmap(QtGui.QPixmap("item/{0}.png".format(game2['Items'][0])))
            self.item21.setText(Item(str(game2['Items'][0])).name)
        except:
             self.picitem21.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item21.setText("Empty Item Slot")
        try:
            self.picitem22.setPixmap(QtGui.QPixmap("item/{0}.png".format(game2['Items'][1])))
            self.item22.setText(Item(str(game2['Items'][1])).name)
        except:
             self.picitem22.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item22.setText("Empty Item Slot")
        try:
            self.picitem23.setPixmap(QtGui.QPixmap("item/{0}.png".format(game2['Items'][2])))
            self.item23.setText(Item(str(game2['Items'][2])).name)
        except:
             self.picitem23.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item23.setText("Empty Item Slot")
        try:
            self.picitem24.setPixmap(QtGui.QPixmap("item/{0}.png".format(game2['Items'][3])))
            self.item24.setText(Item(str(game2['Items'][3])).name)
        except:
             self.picitem24.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item24.setText("Empty Item Slot")
        try:
            self.picitem25.setPixmap(QtGui.QPixmap("item/{0}.png".format(game2['Items'][4])))
            self.item25.setText(Item(str(game2['Items'][4])).name)
        except:
             self.picitem25.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item25.setText("Empty Item Slot")
        try:
            self.picitem26.setPixmap(QtGui.QPixmap("item/{0}.png".format(game2['Items'][5])))
            self.item26.setText(Item(str(game2['Items'][5])).name)
        except:
             self.picitem26.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item26.setText("Empty Item Slot")

        self.kda2.setText("KDA:"+str(game2['KDA']))
        championstats=df[df['id']==history[1]['champion']]
        avragekda=championstats["KDA"].values.tolist()[0]
        comperkda="KDA below avrage"
        if(avragekda<game2['KDA']):
            comperkda="KDA above average"
        avragevision=championstats["Vision"].values.tolist()[0]
        compervision="Vision below avrage"
        if(avragevision<game2['Vision']-2):
            compervision="Vision above average"
        avragecs=championstats["CS"].values.tolist()[0]
        compercs="CS below avrage"
        if(avragecs<game2['Cs']):
            compercs="CS above average"
        self.descreption2.setText(comperkda+"\n" + compervision+"\n" + compercs)
        self.winlose2.setText(game2['win/lose'])



        time.sleep(0.5)
        
        game3=datafrommatc(history[2])
        self.champ_pic3.setPixmap(QtGui.QPixmap("champion/tiles/{0}_0.jpg".format(champion_keys[str(history[2]['champion'])])))

        try:
            self.picitem31.setPixmap(QtGui.QPixmap("item/{0}.png".format(game3['Items'][0])))
            self.item31.setText(Item(str(game3['Items'][0])).name)
        except:
             self.picitem31.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item31.setText("Empty Item Slot")
        try:
            self.picitem32.setPixmap(QtGui.QPixmap("item/{0}.png".format(game3['Items'][1])))
            self.item32.setText(Item(str(game3['Items'][1])).name)
        except:
             self.picitem32.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item32.setText("Empty Item Slot")
        try:
            self.picitem33.setPixmap(QtGui.QPixmap("item/{0}.png".format(game3['Items'][2])))
            self.item33.setText(Item(str(game3['Items'][2])).name)
        except:
             self.picitem33.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item33.setText("Empty Item Slot")
        try:
            self.picitem34.setPixmap(QtGui.QPixmap("item/{0}.png".format(game3['Items'][3])))
            self.item34.setText(Item(str(game3['Items'][3])).name)
        except:
             self.picitem34.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item34.setText("Empty Item Slot")
        try:
            self.picitem35.setPixmap(QtGui.QPixmap("item/{0}.png".format(game3['Items'][4])))
            self.item35.setText(Item(str(game3['Items'][4])).name)
        except:
             self.picitem35.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item35.setText("Empty Item Slot")
        try:
            self.picitem36.setPixmap(QtGui.QPixmap("item/{0}.png".format(game3['Items'][5])))
            self.item36.setText(Item(str(game3['Items'][5])).name)
        except:
             self.picitem36.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item36.setText("Empty Item Slot")

        self.kda3.setText("KDA:"+str(game3['KDA']))
        championstats=df[df['id']==history[2]['champion']]
        avragekda=championstats["KDA"].values.tolist()[0]
        comperkda="KDA below avrage"
        if(avragekda<game3['KDA']):
            comperkda="KDA above average"
        avragevision=championstats["Vision"].values.tolist()[0]
        compervision="Vision below avrage"
        if(avragevision<game3['Vision']-2):
            compervision="Vision above average"
        avragecs=championstats["CS"].values.tolist()[0]
        compercs="CS below avrage"
        if(avragecs<game3['Cs']):
            compercs="CS above average"
        self.descreption3.setText(comperkda+"\n" + compervision+"\n" + compercs)
        self.winlose3.setText(game3['win/lose'])
        

        game4=datafrommatc(history[3])
        self.champ_pic4.setPixmap(QtGui.QPixmap("champion/tiles/{0}_0.jpg".format(champion_keys[str(history[3]['champion'])])))
        try:
            self.picitem41.setPixmap(QtGui.QPixmap("item/{0}.png".format(game4['Items'][0])))
            self.item41.setText(Item(str(game4['Items'][0])).name)
        except:
             self.picitem41.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item41.setText("Empty Item Slot")
        try:
            self.picitem42.setPixmap(QtGui.QPixmap("item/{0}.png".format(game4['Items'][1])))
            self.item42.setText(Item(str(game4['Items'][1])).name)
        except:
             self.picitem42.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item42.setText("Empty Item Slot")
        try:
            self.picitem43.setPixmap(QtGui.QPixmap("item/{0}.png".format(game4['Items'][2])))
            self.item43.setText(Item(str(game4['Items'][2])).name)
        except:
             self.picitem43.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item43.setText("Empty Item Slot")
        try:
            self.picitem44.setPixmap(QtGui.QPixmap("item/{0}.png".format(game4['Items'][3])))
            self.item44.setText(Item(str(game4['Items'][3])).name)
        except:
             self.picitem44.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item44.setText("Empty Item Slot")
        try:
            self.picitem45.setPixmap(QtGui.QPixmap("item/{0}.png".format(game4['Items'][4])))
            self.item45.setText(Item(str(game4['Items'][4])).name)
        except:
             self.picitem45.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item45.setText("Empty Item Slot")
        try:
            self.picitem46.setPixmap(QtGui.QPixmap("item/{0}.png".format(game4['Items'][5])))
            self.item46.setText(Item(str(game4['Items'][5])).name)
        except:
             self.picitem46.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item46.setText("Empty Item Slot")

        self.kda4.setText("KDA:"+str(game4['KDA']))
        championstats=df[df['id']==history[3]['champion']]
        avragekda=championstats["KDA"].values.tolist()[0]
        comperkda="KDA below avrage"
        if(avragekda<game4['KDA']):
            comperkda="KDA above average"
        avragevision=championstats["Vision"].values.tolist()[0]
        compervision="Vision below avrage"
        if(avragevision<game4['Vision']-2):
            compervision="Vision above average"
        avragecs=championstats["CS"].values.tolist()[0]
        compercs="CS below avrage"
        if(avragecs<game4['Cs']):
            compercs="CS above average"
        self.descreption4.setText(comperkda+"\n" + compervision+"\n" + compercs)
        self.winlose4.setText(game4['win/lose'])

        time.sleep(0.5)
        


        game5=datafrommatc(history[4])
        self.champ_pic5.setPixmap(QtGui.QPixmap("champion/tiles/{0}_0.jpg".format(champion_keys[str(history[4]['champion'])])))
        try:
            self.picitem51.setPixmap(QtGui.QPixmap("item/{0}.png".format(game5['Items'][0])))
            self.item51.setText(Item(str(game5['Items'][0])).name)
        except:
             self.picitem51.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item51.setText("Empty Item Slot")
        try:
            self.picitem52.setPixmap(QtGui.QPixmap("item/{0}.png".format(game5['Items'][1])))
            self.item52.setText(Item(str(game5['Items'][1])).name)
        except:
             self.picitem52.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item52.setText("Empty Item Slot")
        try:
            self.picitem53.setPixmap(QtGui.QPixmap("item/{0}.png".format(game5['Items'][2])))
            self.item53.setText(Item(str(game5['Items'][2])).name)
        except:
             self.picitem53.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item53.setText("Empty Item Slot")
        try:
            self.picitem54.setPixmap(QtGui.QPixmap("item/{0}.png".format(game5['Items'][3])))
            self.item54.setText(Item(str(game5['Items'][3])).name)
        except:
             self.picitem54.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item54.setText("Empty Item Slot")
        try:
            self.picitem55.setPixmap(QtGui.QPixmap("item/{0}.png".format(game5['Items'][4])))
            self.item55.setText(Item(str(game5['Items'][4])).name)
        except:
             self.picitem55.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item55.setText("Empty Item Slot")
        try:
            self.picitem56.setPixmap(QtGui.QPixmap("item/{0}.png".format(game5['Items'][5])))
            self.item56.setText(Item(str(game5['Items'][5])).name)
        except:
             self.picitem56.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item56.setText("Empty Item Slot")        

        self.kda5.setText("KDA:"+str(game5['KDA']))
        championstats=df[df['id']==history[4]['champion']]
        avragekda=championstats["KDA"].values.tolist()[0]
        comperkda="KDA below avrage"
        if(avragekda<game5['KDA']):
            comperkda="KDA above average"
        avragevision=championstats["Vision"].values.tolist()[0]
        compervision="Vision below avrage"
        if(avragevision<game5['Vision']-2):
            compervision="Vision above average"
        avragecs=championstats["CS"].values.tolist()[0]
        compercs="CS below avrage"
        if(avragecs<game5['Cs']):
            compercs="CS above average"
        self.descreption5.setText(comperkda+"\n" + compervision+"\n" + compercs)
        self.winlose5.setText(game5['win/lose'])

        game6=datafrommatc(history[5])
        self.champ_pic6.setPixmap(QtGui.QPixmap("champion/tiles/{0}_0.jpg".format(champion_keys[str(history[5]['champion'])])))
        try:
            self.picitem61.setPixmap(QtGui.QPixmap("item/{0}.png".format(game6['Items'][0])))
            self.item61.setText(Item(str(game6['Items'][0])).name)
        except:
             self.picitem61.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item61.setText("Empty Item Slot")
        try:
            self.picitem62.setPixmap(QtGui.QPixmap("item/{0}.png".format(game6['Items'][1])))
            self.item62.setText(Item(str(game6['Items'][1])).name)
        except:
             self.picitem62.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item62.setText("Empty Item Slot")
        try:
            self.picitem63.setPixmap(QtGui.QPixmap("item/{0}.png".format(game6['Items'][2])))
            self.item63.setText(Item(str(game6['Items'][2])).name)
        except:
             self.picitem63.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item63.setText("Empty Item Slot")
        try:
            self.picitem64.setPixmap(QtGui.QPixmap("item/{0}.png".format(game6['Items'][3])))
            self.item64.setText(Item(str(game6['Items'][3])).name)
        except:
             self.picitem64.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item64.setText("Empty Item Slot")
        try:
            self.picitem65.setPixmap(QtGui.QPixmap("item/{0}.png".format(game6['Items'][4])))
            self.item65.setText(Item(str(game6['Items'][4])).name)
        except:
             self.picitem65.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item65.setText("Empty Item Slot")
        try:
            self.picitem66.setPixmap(QtGui.QPixmap("item/{0}.png".format(game6['Items'][5])))
            self.item66.setText(Item(str(game6['Items'][5])).name)
        except:
             self.picitem66.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item66.setText("Empty Item Slot")        

        self.kda6.setText("KDA:"+str(game6['KDA']))
        championstats=df[df['id']==history[5]['champion']]
        avragekda=championstats["KDA"].values.tolist()[0]
        comperkda="KDA below avrage"
        if(avragekda<game6['KDA']):
            comperkda="KDA above average"
        avragevision=championstats["Vision"].values.tolist()[0]
        compervision="Vision below avrage"
        if(avragevision<game6['Vision']-2):
            compervision="Vision above average"
        avragecs=championstats["CS"].values.tolist()[0]
        compercs="CS below avrage"
        if(avragecs<game6['Cs']):
            compercs="CS above average"
        self.descreption6.setText(comperkda+"\n" + compervision+"\n" + compercs)
        self.winlose6.setText(game6['win/lose'])


            
        
        game7=datafrommatc(history[6])
        self.champ_pic7.setPixmap(QtGui.QPixmap("champion/tiles/{0}_0.jpg".format(champion_keys[str(history[6]['champion'])])))
        try:
            self.picitem71.setPixmap(QtGui.QPixmap("item/{0}.png".format(game7['Items'][0])))
            self.item71.setText(Item(str(game7['Items'][0])).name)
        except:
             self.picitem71.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item71.setText("Empty Item Slot")
        try:
            self.picitem72.setPixmap(QtGui.QPixmap("item/{0}.png".format(game7['Items'][1])))
            self.item72.setText(Item(str(game7['Items'][1])).name)
        except:
             self.picitem72.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item72.setText("Empty Item Slot")
        try:
            self.picitem73.setPixmap(QtGui.QPixmap("item/{0}.png".format(game7['Items'][2])))
            self.item73.setText(Item(str(game7['Items'][2])).name)
        except:
             self.picitem73.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item73.setText("Empty Item Slot")
        try:
            self.picitem74.setPixmap(QtGui.QPixmap("item/{0}.png".format(game7['Items'][3])))
            self.item74.setText(Item(str(game7['Items'][3])).name)
        except:
             self.picitem74.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item74.setText("Empty Item Slot")
        try:
            self.picitem75.setPixmap(QtGui.QPixmap("item/{0}.png".format(game7['Items'][4])))
            self.item75.setText(Item(str(game7['Items'][4])).name)
        except:
             self.picitem75.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item75.setText("Empty Item Slot")
        try:
            self.picitem76.setPixmap(QtGui.QPixmap("item/{0}.png".format(game7['Items'][5])))
            self.item76.setText(Item(str(game7['Items'][5])).name)
        except:
             self.picitem76.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item76.setText("Empty Item Slot")

        self.kda7.setText("KDA:"+str(game7['KDA']))
        championstats=df[df['id']==history[6]['champion']]
        avragekda=championstats["KDA"].values.tolist()[0]
        comperkda="KDA below avrage"
        if(avragekda<game7['KDA']):
            comperkda="KDA above average"
        avragevision=championstats["Vision"].values.tolist()[0]
        compervision="Vision below avrage"
        if(avragevision<game7['Vision']-2):
            compervision="Vision above average"
        avragecs=championstats["CS"].values.tolist()[0]
        compercs="CS below avrage"
        if(avragecs<game7['Cs']):
            compercs="CS above average"
        self.descreption7.setText(comperkda+"\n" + compervision+"\n" + compercs)
        self.winlose7.setText(game7['win/lose'])

        game8=datafrommatc(history[7])
        self.champ_pic8.setPixmap(QtGui.QPixmap("champion/tiles/{0}_0.jpg".format(champion_keys[str(history[7]['champion'])])))
        try:
            self.picitem81.setPixmap(QtGui.QPixmap("item/{0}.png".format(game8['Items'][0])))
            self.item81.setText(Item(str(game8['Items'][0])).name)
        except:
             self.picitem81.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item81.setText("Empty Item Slot")
        try:
            self.picitem82.setPixmap(QtGui.QPixmap("item/{0}.png".format(game8['Items'][1])))
            self.item82.setText(Item(str(game8['Items'][1])).name)
        except:
             self.picitem82.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item82.setText("Empty Item Slot")
        try:
            self.picitem83.setPixmap(QtGui.QPixmap("item/{0}.png".format(game8['Items'][2])))
            self.item83.setText(Item(str(game8['Items'][2])).name)
        except:
             self.picitem83.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item83.setText("Empty Item Slot")
        try:
            self.picitem84.setPixmap(QtGui.QPixmap("item/{0}.png".format(game8['Items'][3])))
            self.item84.setText(Item(str(game8['Items'][3])).name)
        except:
             self.picitem84.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item84.setText("Empty Item Slot")
        try:
            self.picitem85.setPixmap(QtGui.QPixmap("item/{0}.png".format(game8['Items'][4])))
            self.item85.setText(Item(str(game8['Items'][4])).name)
        except:
             self.picitem85.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item85.setText("Empty Item Slot")
        try:
            self.picitem86.setPixmap(QtGui.QPixmap("item/{0}.png".format(game8['Items'][5])))
            self.item86.setText(Item(str(game8['Items'][5])).name)
        except:
             self.picitem86.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item86.setText("Empty Item Slot")

        self.kda8.setText("KDA:"+str(game8['KDA']))
        championstats=df[df['id']==history[7]['champion']]
        avragekda=championstats["KDA"].values.tolist()[0]
        comperkda="KDA below avrage"
        if(avragekda<game8['KDA']):
            comperkda="KDA above average"
        avragevision=championstats["Vision"].values.tolist()[0]
        compervision="Vision below avrage"
        if(avragevision<game8['Vision']-2):
            compervision="Vision above average"
        avragecs=championstats["CS"].values.tolist()[0]
        compercs="CS below avrage"
        if(avragecs<game8['Cs']):
            compercs="CS above average"
        self.descreption8.setText(comperkda+"\n" + compervision+"\n" + compercs)
        self.winlose8.setText(game8['win/lose'])
        
        game9=datafrommatc(history[8])
        self.champ_pic9.setPixmap(QtGui.QPixmap("champion/tiles/{0}_0.jpg".format(champion_keys[str(history[8]['champion'])])))
        try:
            self.picitem91.setPixmap(QtGui.QPixmap("item/{0}.png".format(game9['Items'][0])))
            self.item91.setText(Item(str(game9['Items'][0])).name)
        except:
             self.picitem91.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item91.setText("Empty Item Slot")
        try:
            self.picitem92.setPixmap(QtGui.QPixmap("item/{0}.png".format(game9['Items'][1])))
            self.item92.setText(Item(str(game9['Items'][1])).name)
        except:
             self.picitem92.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item92.setText("Empty Item Slot")
        try:
            self.picitem93.setPixmap(QtGui.QPixmap("item/{0}.png".format(game9['Items'][2])))
            self.item93.setText(Item(str(game9['Items'][2])).name)
        except:
             self.picitem93.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item93.setText("Empty Item Slot")
        try:
            self.picitem94.setPixmap(QtGui.QPixmap("item/{0}.png".format(game9['Items'][3])))
            self.item94.setText(Item(str(game9['Items'][3])).name)
        except:
             self.picitem94.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item94.setText("Empty Item Slot")
        try:
            self.picitem95.setPixmap(QtGui.QPixmap("item/{0}.png".format(game9['Items'][4])))
            self.item95.setText(Item(str(game9['Items'][4])).name)
        except:
             self.picitem95.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item95.setText("Empty Item Slot")
        try:
            self.picitem96.setPixmap(QtGui.QPixmap("item/{0}.png".format(game9['Items'][5])))
            self.item96.setText(Item(str(game9['Items'][5])).name)
        except:
             self.picitem96.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item96.setText("Empty Item Slot")

        self.kda9.setText("KDA:"+str(game9['KDA']))
        championstats=df[df['id']==history[8]['champion']]
        avragekda=championstats["KDA"].values.tolist()[0]
        comperkda="KDA below avrage"
        if(avragekda<game9['KDA']):
            comperkda="KDA above average"
        avragevision=championstats["Vision"].values.tolist()[0]
        compervision="Vision below avrage"
        if(avragevision<game9['Vision']-2):
            compervision="Vision above average"
        avragecs=championstats["CS"].values.tolist()[0]
        compercs="CS below avrage"
        if(avragecs<game9['Cs']):
            compercs="CS above average"
        self.descreption9.setText(comperkda+"\n" + compervision+"\n" + compercs)
        self.winlose9.setText(game9['win/lose'])
        time.sleep(0.5)
        game10=datafrommatc(history[9])
        self.champ_pic10.setPixmap(QtGui.QPixmap("champion/tiles/{0}_0.jpg".format(champion_keys[str(history[9]['champion'])])))
        try:
            self.picitem101.setPixmap(QtGui.QPixmap("item/{0}.png".format(game10['Items'][0])))
            self.item101.setText(Item(str(game10['Items'][0])).name)
        except:
             self.picitem101.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item101.setText("Empty Item Slot")
        try:
            self.picitem102.setPixmap(QtGui.QPixmap("item/{0}.png".format(game10['Items'][1])))
            self.item102.setText(Item(str(game10['Items'][1])).name)
        except:
             self.picitem102.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item102.setText("Empty Item Slot")
        try:
            self.picitem103.setPixmap(QtGui.QPixmap("item/{0}.png".format(game10['Items'][2])))
            self.item103.setText(Item(str(game10['Items'][2])).name)
        except:
             self.picitem103.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item103.setText("Empty Item Slot")
        try:
            self.picitem104.setPixmap(QtGui.QPixmap("item/{0}.png".format(game10['Items'][3])))
            self.item104.setText(Item(str(game10['Items'][3])).name)
        except:
             self.picitem104.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item104.setText("Empty Item Slot")
        try:
            self.picitem105.setPixmap(QtGui.QPixmap("item/{0}.png".format(game10['Items'][4])))
            self.item105.setText(Item(str(game10['Items'][4])).name)
        except:
             self.picitem105.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item105.setText("Empty Item Slot")
        try:
            self.picitem106.setPixmap(QtGui.QPixmap("item/{0}.png".format(game10['Items'][5])))
            self.item106.setText(Item(str(game10['Items'][5])).name)
        except:
             self.picitem106.setPixmap(QtGui.QPixmap("item/3400.png"))
             self.item106.setText("Empty Item Slot")

        self.kda10.setText("KDA:"+str(game10['KDA']))
        championstats=df[df['id']==history[9]['champion']]
        avragekda=championstats["KDA"].values.tolist()[0]
        comperkda="KDA below avrage"
        if(avragekda<game10['KDA']):
            comperkda="KDA above average"
        avragevision=championstats["Vision"].values.tolist()[0]
        compervision="Vision below avrage"
        if(avragevision<game10['Vision']-2):
            compervision="Vision above average"
        avragecs=championstats["CS"].values.tolist()[0]
        compercs="CS below avrage"
        if(avragecs<game10['Cs']):
            compercs="CS above average"
        self.descreption10.setText(comperkda+"\n" + compervision+"\n" + compercs)
        self.winlose10.setText(game9['win/lose'])
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">match history</span></p></body></html>"))
        self.title.setText(_translate("MainWindow", "match history"))
        self.kda2.setText(_translate("MainWindow", "KDA"))
        self.item11.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item12.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item13.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item14.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item15.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item16.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.winlose1.setText(_translate("MainWindow", "WIN/LOSE"))
        self.winlose2.setText(_translate("MainWindow", "WIN/LOSE"))
        self.item21.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item22.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item23.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item24.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item25.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item26.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.kda1.setText(_translate("MainWindow", "KDA"))
        self.descreption2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p></body></html>"))
        self.winlose3.setText(_translate("MainWindow", "WIN/LOSE"))
        self.item31.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item32.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item33.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item34.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item35.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item36.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.kda3.setText(_translate("MainWindow", "KDA"))
        self.descreption3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p></body></html>"))
        self.winlose4.setText(_translate("MainWindow", "WIN/LOSE"))
        self.item41.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item42.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item43.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item44.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item45.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item46.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.kda4.setText(_translate("MainWindow", "KDA"))
        self.descreption4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p></body></html>"))
        self.winlose5.setText(_translate("MainWindow", "WIN/LOSE"))
        self.item51.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item52.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item53.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item54.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item55.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item56.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.kda5.setText(_translate("MainWindow", "KDA"))
        self.descreption5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p></body></html>"))
        self.winlose6.setText(_translate("MainWindow", "WIN/LOSE"))
        self.item61.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item62.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item63.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item64.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item65.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item66.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.kda6.setText(_translate("MainWindow", "KDA"))
        self.descreption6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p></body></html>"))
        self.winlose7.setText(_translate("MainWindow", "WIN/LOSE"))
        self.item71.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item72.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item73.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item74.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item75.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item76.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.kda7.setText(_translate("MainWindow", "KDA"))
        self.descreption7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p></body></html>"))
        self.winlose8.setText(_translate("MainWindow", "WIN/LOSE"))
        self.item81.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item82.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item83.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item84.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item85.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item86.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.kda8.setText(_translate("MainWindow", "KDA"))
        self.descreption8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p></body></html>"))
        self.winlose9.setText(_translate("MainWindow", "WIN/LOSE"))
        self.item91.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item92.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item93.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item94.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item95.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item96.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.kda9.setText(_translate("MainWindow", "KDA"))
        self.descreption9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p></body></html>"))
        self.descreption1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p></body></html>"))
        self.winlose10.setText(_translate("MainWindow", "WIN/LOSE"))
        self.item101.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item102.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item103.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item104.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item105.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.item106.setText(_translate("MainWindow", "shurlyes battlesong"))
        self.kda10.setText(_translate("MainWindow", "KDA"))
        self.descreption10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">player descripsion ,player descripsion</p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = matchHistory()
    ui.setupUi(MainWindow,"simpslayer69")
    MainWindow.show()
    sys.exit(app.exec())

    
    
 

