# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstversion.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 519)
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame.setStyleSheet("QFrame{\n"
"background-font: 75 11pt \"URW Bookman L\";\n"
"background-color: rgb(0, 10, 44);\n"
"background-radius: 10px;\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.VELOCITY = QtWidgets.QFrame(self.frame)
        self.VELOCITY.setGeometry(QtCore.QRect(10, 60, 190, 131))
        self.VELOCITY.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 0, 100);\n"
"}")
        self.VELOCITY.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VELOCITY.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VELOCITY.setObjectName("VELOCITY")
        self.label = QtWidgets.QLabel(self.VELOCITY)
        self.label.setGeometry(QtCore.QRect(60, 20, 69, 17))
        self.label.setStyleSheet("QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.velocity_t = QtWidgets.QTextEdit(self.VELOCITY)
        self.velocity_t.setGeometry(QtCore.QRect(10, 70, 161, 41))
        self.velocity_t.setStyleSheet("QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}")
        self.velocity_t.setReadOnly(True)
        self.velocity_t.setObjectName("velocity_t")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 200, 381, 81))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet("QFrame{\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 131, 20))
        self.label_3.setStyleSheet("QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.dist_t = QtWidgets.QTextEdit(self.frame_4)
        self.dist_t.setGeometry(QtCore.QRect(180, 20, 171, 41))
        self.dist_t.setStyleSheet("QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}")
        self.dist_t.setReadOnly(True)
        self.dist_t.setObjectName("dist_t")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(207, 310, 91, 171))
        self.frame_5.setStyleSheet("QFrame{\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(16, 6, 61, 21))
        self.label_4.setStyleSheet("QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.main_battery_v = QtWidgets.QTextEdit(self.frame_5)
        self.main_battery_v.setGeometry(QtCore.QRect(20, 40, 50, 50))
        self.main_battery_v.setStyleSheet("QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}\n"
"")
        self.main_battery_v.setReadOnly(True)
        self.main_battery_v.setObjectName("main_battery_v")
        self.main_battery_c = QtWidgets.QTextEdit(self.frame_5)
        self.main_battery_c.setGeometry(QtCore.QRect(20, 100, 50, 50))
        self.main_battery_c.setStyleSheet("QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}\n"
"")
        self.main_battery_c.setReadOnly(True)
        self.main_battery_c.setObjectName("main_battery_c")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(306, 310, 91, 171))
        self.frame_6.setStyleSheet("QFrame{\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.second_batttery_v = QtWidgets.QTextEdit(self.frame_6)
        self.second_batttery_v.setGeometry(QtCore.QRect(20, 40, 50, 50))
        self.second_batttery_v.setStyleSheet("QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}\n"
"")
        self.second_batttery_v.setReadOnly(True)
        self.second_batttery_v.setObjectName("second_batttery_v")
        self.second_battery_c = QtWidgets.QTextEdit(self.frame_6)
        self.second_battery_c.setGeometry(QtCore.QRect(20, 100, 50, 50))
        self.second_battery_c.setStyleSheet("QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}\n"
"")
        self.second_battery_c.setReadOnly(True)
        self.second_battery_c.setObjectName("second_battery_c")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setGeometry(QtCore.QRect(26, 6, 43, 21))
        self.label_5.setStyleSheet("QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_5.setObjectName("label_5")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(207, 60, 181, 131))
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 0, 100);\n"
"filter: blur(5px);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 111, 20))
        self.label_2.setStyleSheet("QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(220, 130, 47, 13))
        self.label_14.setObjectName("label_14")
        self.acc_t = QtWidgets.QTextEdit(self.frame_3)
        self.acc_t.setGeometry(QtCore.QRect(10, 70, 161, 41))
        self.acc_t.setStyleSheet("QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}")
        self.acc_t.setReadOnly(True)
        self.acc_t.setObjectName("acc_t")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setGeometry(QtCore.QRect(10, 10, 804, 43))
        self.frame_8.setMaximumSize(QtCore.QSize(804, 43))
        self.frame_8.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(10, 310, 190, 81))
        self.frame_9.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setGeometry(QtCore.QRect(60, 10, 69, 17))
        self.label_7.setStyleSheet("QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.dist_t_2 = QtWidgets.QTextEdit(self.frame_9)
        self.dist_t_2.setGeometry(QtCore.QRect(10, 40, 161, 31))
        self.dist_t_2.setStyleSheet("QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}")
        self.dist_t_2.setReadOnly(True)
        self.dist_t_2.setObjectName("dist_t_2")
        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setGeometry(QtCore.QRect(400, 60, 67, 274))
        self.frame_12.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_23 = QtWidgets.QLabel(self.frame_12)
        self.label_23.setGeometry(QtCore.QRect(30, 270, 51, 16))
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_12)
        self.label_24.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.frame_13 = QtWidgets.QFrame(self.frame)
        self.frame_13.setGeometry(QtCore.QRect(480, 60, 67, 274))
        self.frame_13.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_26 = QtWidgets.QLabel(self.frame_13)
        self.label_26.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.label_26.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_26.setObjectName("label_26")
        self.frame_18 = QtWidgets.QFrame(self.frame)
        self.frame_18.setGeometry(QtCore.QRect(560, 60, 262, 98))
        self.frame_18.setStyleSheet("background-color: rgba(0, 0, 0, 100)")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label_6 = QtWidgets.QLabel(self.frame_18)
        self.label_6.setGeometry(QtCore.QRect(90, 0, 81, 41))
        self.label_6.setStyleSheet("QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_6.setObjectName("label_6")
        self.state_t = QtWidgets.QTextEdit(self.frame_18)
        self.state_t.setGeometry(QtCore.QRect(40, 40, 181, 41))
        self.state_t.setStyleSheet("QTextEdit{\n"
"background-color: rgb(0, 240, 255);\n"
"}")
        self.state_t.setReadOnly(True)
        self.state_t.setObjectName("state_t")
        self.frame_19 = QtWidgets.QFrame(self.frame)
        self.frame_19.setGeometry(QtCore.QRect(552, 433, 262, 43))
        self.frame_19.setStyleSheet("background-color: rgba(0, 0, 0, 100)")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.label_10 = QtWidgets.QLabel(self.frame_19)
        self.label_10.setGeometry(QtCore.QRect(10, 6, 231, 31))
        self.label_10.setStyleSheet("QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.frame_20 = QtWidgets.QFrame(self.frame)
        self.frame_20.setGeometry(QtCore.QRect(552, 382, 262, 43))
        self.frame_20.setStyleSheet("background-color: rgba(0, 0, 0, 100)")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.label_9 = QtWidgets.QLabel(self.frame_20)
        self.label_9.setGeometry(QtCore.QRect(10, 6, 231, 31))
        self.label_9.setStyleSheet("QLabel{\n"
"background-color: rgb(rgba(0, 0, 0, 100));\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.frame_21 = QtWidgets.QFrame(self.frame)
        self.frame_21.setGeometry(QtCore.QRect(560, 170, 262, 98))
        self.frame_21.setStyleSheet("background-color: rgba(0, 0, 0, 100)")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.start_b = QtWidgets.QPushButton(self.frame)
        self.start_b.setGeometry(QtCore.QRect(410, 420, 61, 51))
        self.start_b.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 240, 255);\n"
"}")
        self.start_b.setObjectName("start_b")
        self.stop_b = QtWidgets.QPushButton(self.frame)
        self.stop_b.setGeometry(QtCore.QRect(480, 420, 61, 51))
        self.stop_b.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 240, 255);\n"
"}")
        self.stop_b.setObjectName("stop_b")
        self.estop_b = QtWidgets.QPushButton(self.frame)
        self.estop_b.setGeometry(QtCore.QRect(410, 360, 131, 51))
        self.estop_b.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(238, 238, 236);\n"
"}")
        self.estop_b.setObjectName("estop_b")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(560, 280, 262, 91))
        self.frame_7.setStyleSheet("background-color: rgba(0, 0, 0, 100)")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "VELOCITY"))
        self.label_3.setText(_translate("MainWindow", "DISTANCE MOVED"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">MAIN<br/>BATTERY</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">24V<br/>BATTERY</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "ACCELERATION"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "PRESSURE"))
        self.label_23.setText(_translate("MainWindow", "Battery :"))
        self.label_24.setText(_translate("MainWindow", "MAIN"))
        self.label_26.setText(_translate("MainWindow", "BREAK"))
        self.label_6.setText(_translate("MainWindow", "POD STATE"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11.5pt; font-weight:600;\">LESS IMPORTANT THINGS - 2</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11.5pt; font-weight:600;\">LESS IMPORTANT THINGS - 1</span></p></body></html>"))
        self.start_b.setText(_translate("MainWindow", "START"))
        self.stop_b.setText(_translate("MainWindow", "STOP"))
        self.estop_b.setText(_translate("MainWindow", "ESTOP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

