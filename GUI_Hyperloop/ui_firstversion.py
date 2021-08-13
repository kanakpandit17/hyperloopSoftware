# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'firstversionPqjMff.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Side2extn.RoundProgressBar import roundProgressBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(762, 365)
        MainWindow.setMaximumSize(QSize(851, 519))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setStyleSheet(u"QFrame{\n"
"background-font: 75 11pt \"URW Bookman L\";\n"
"background-color: rgb(0, 10, 44);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.VELOCITY = QFrame(self.frame)
        self.VELOCITY.setObjectName(u"VELOCITY")
        self.VELOCITY.setGeometry(QRect(10, 60, 190, 241))
        self.VELOCITY.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 0, 0, 100);\n"
"}")
        self.VELOCITY.setFrameShape(QFrame.StyledPanel)
        self.VELOCITY.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.VELOCITY)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 69, 17))
        self.label.setStyleSheet(u"QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.widget_2 = roundProgressBar(self.VELOCITY)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(23, 77, 138, 138))
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 310, 190, 60))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 0, 101, 16))
        self.label_3.setStyleSheet(u"QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(207, 310, 91, 72))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(26, 6, 43, 21))
        self.label_4.setStyleSheet(u"QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.textEdit_4 = QTextEdit(self.frame_5)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(7, 36, 36, 31))
        self.textEdit_4.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}\n"
"")
        self.textEdit_5 = QTextEdit(self.frame_5)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(48, 36, 36, 31))
        self.textEdit_5.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}\n"
"")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(306, 310, 91, 72))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.textEdit_6 = QTextEdit(self.frame_6)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(7, 36, 36, 31))
        self.textEdit_6.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}\n"
"")
        self.textEdit_7 = QTextEdit(self.frame_6)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(48, 36, 36, 31))
        self.textEdit_7.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}\n"
"")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(26, 6, 43, 21))
        self.label_5.setStyleSheet(u"QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(207, 60, 190, 241))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 0, 0, 100);\n"
"filter: blur(5px);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 20, 81, 16))
        self.label_2.setStyleSheet(u"QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(23, 77, 138, 138))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 10, 804, 43))
        self.frame_8.setMaximumSize(QSize(804, 43))
        self.frame_8.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 378, 190, 99))
        self.frame_9.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 10, 69, 17))
        self.label_7.setStyleSheet(u"QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.Graph_1 = QFrame(self.frame)
        self.Graph_1.setObjectName(u"Graph_1")
        self.Graph_1.setGeometry(QRect(207, 389, 91, 88))
        self.Graph_1.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.Graph_1.setFrameShape(QFrame.StyledPanel)
        self.Graph_1.setFrameShadow(QFrame.Raised)
        self.Graph_2 = QFrame(self.frame)
        self.Graph_2.setObjectName(u"Graph_2")
        self.Graph_2.setGeometry(QRect(306, 389, 91, 88))
        self.Graph_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.Graph_2.setFrameShape(QFrame.StyledPanel)
        self.Graph_2.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(403, 60, 67, 274))
        self.frame_12.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(478, 60, 67, 274))
        self.frame_13.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(403, 346, 67, 60))
        self.frame_14.setStyleSheet(u"background-color: rgb(255, 0, 0)")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(403, 21, 41, 17))
        self.label_8.setStyleSheet(u"QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.frame_15 = QFrame(self.frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(403, 417, 67, 60))
        self.frame_15.setStyleSheet(u"background-color: rgba(0, 0, 0, 100)")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_16 = QFrame(self.frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(478, 345, 67, 60))
        self.frame_16.setStyleSheet(u"background-color: rgba(0, 0, 0, 100)")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(6, 2, 54, 17))
        self.label_6.setStyleSheet(u"QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(478, 416, 67, 60))
        self.frame_17.setStyleSheet(u"background-color: rgba(0, 0, 0, 100)")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(552, 60, 262, 98))
        self.frame_7.setStyleSheet(u"background-color: rgba(0, 0, 0, 100)")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_18 = QFrame(self.frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(552, 167, 262, 98))
        self.frame_18.setStyleSheet(u"background-color: rgba(0, 0, 0, 100)")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_19 = QFrame(self.frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(552, 433, 262, 43))
        self.frame_19.setStyleSheet(u"background-color: rgba(0, 0, 0, 100)")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_19)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 6, 231, 31))
        self.label_10.setStyleSheet(u"QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_20 = QFrame(self.frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(552, 382, 262, 43))
        self.frame_20.setStyleSheet(u"background-color: rgba(0, 0, 0, 100)")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_20)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 6, 231, 31))
        self.label_9.setStyleSheet(u"QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_21 = QFrame(self.frame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(552, 275, 262, 98))
        self.frame_21.setStyleSheet(u"background-color: rgba(0, 0, 0, 100)")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"VELOCITY", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:6pt; font-weight:600;\">DISTANCE MOVED - 500M</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">MAIN<br/>BATTERY</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">24V<br/>BATTERY</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ACCELERATION", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"PRESSURE", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">ESTOP</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"POD STATE", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11.5pt; font-weight:600;\">LESS IMPORTANT THINGS - 2</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11.5pt; font-weight:600;\">LESS IMPORTANT THINGS - 1</span></p></body></html>", None))
    # retranslateUi

