# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\Documents\HARSH\clg_project\tracker\ui\tracker-window-17012024.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class Ui_ActiveTracker(object):
    def setupUi(self, ActiveTracker):
        ActiveTracker.setObjectName("ActiveTracker")
        ActiveTracker.resize(700, 529)
        ActiveTracker.setStyleSheet("QMainWindow{\n"
                                    "    background-color: #eaf1f4\n"
                                    "}")
        self.centralwidget = QtWidgets.QWidget(ActiveTracker)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(20, 10, 678, 79))
        self.frame_1.setStyleSheet("")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_13 = QtWidgets.QLabel(self.frame_1)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("C:\\Users\\Admin\\Documents\\HARSH\\clg_project\\tracker\\ui\\../ui-icons/icons8-menu-64.png"))
        self.label_13.setScaledContents(False)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        spacerItem = QtWidgets.QSpacerItem(508, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.frame_1)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.widget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 100, 481, 211))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color: #fff;\n"
"    border-radius:20px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.widget_2 = QtWidgets.QWidget(self.frame_2)
        self.widget_2.setGeometry(QtCore.QRect(10, 9, 451, 183))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"    color:rgb(167, 167, 167);\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"    border-bottom: 1px solid rgb(167, 167, 167);;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget_4)
        self.comboBox.setPlaceholderText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 3)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 2)
        self.gridLayout_2.addWidget(self.widget_4, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 320, 671, 161))
        self.frame_3.setStyleSheet("QFrame{\n"
"    background-color: #fff;\n"
"    border-radius:20px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.widget_8 = QtWidgets.QWidget(self.frame_3)
        self.widget_8.setGeometry(QtCore.QRect(10, 10, 651, 141))
        self.widget_8.setObjectName("widget_8")
        self.label_6 = QtWidgets.QLabel(self.widget_8)
        self.label_6.setGeometry(QtCore.QRect(9, 9, 631, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"    color:rgb(167, 167, 167);\n"
"}")
        self.label_6.setObjectName("label_6")
        self.widget_5 = QtWidgets.QWidget(self.widget_8)
        self.widget_5.setGeometry(QtCore.QRect(9, 31, 631, 101))
        self.widget_5.setObjectName("widget_5")
        self.widget_11 = QtWidgets.QWidget(self.widget_5)
        self.widget_11.setGeometry(QtCore.QRect(29, 10, 591, 71))
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget_11)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:\\Users\\Admin\\Documents\\HARSH\\clg_project\\tracker\\ui\\../ui-icons/icons8-pause-48.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.widget_11)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget_11)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(510, 99, 181, 211))
        self.frame_4.setStyleSheet("QFrame{\n"
"    background-color: #fff;\n"
"    border-radius:20px;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_6 = QtWidgets.QWidget(self.frame_4)
        self.widget_6.setObjectName("widget_6")
        self.layoutWidget = QtWidgets.QWidget(self.widget_6)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 141, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.verticalLayout_6.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.frame_4)
        self.widget_7.setObjectName("widget_7")
        self.layoutWidget1 = QtWidgets.QWidget(self.widget_7)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 141, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_22 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_22.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_5.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.verticalLayout_6.addWidget(self.widget_7)
        ActiveTracker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ActiveTracker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        ActiveTracker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ActiveTracker)
        self.statusbar.setObjectName("statusbar")
        ActiveTracker.setStatusBar(self.statusbar)

        self.retranslateUi(ActiveTracker)
        QtCore.QMetaObject.connectSlotsByName(ActiveTracker)

    def retranslateUi(self, ActiveTracker):
        _translate = QtCore.QCoreApplication.translate
        ActiveTracker.setWindowTitle(_translate("ActiveTracker", "ActiveTracker"))
        self.label.setText(_translate("ActiveTracker", "Employee"))
        self.label_2.setText(_translate("ActiveTracker", "Developer"))
        self.label_3.setText(_translate("ActiveTracker", "Current Session"))
        self.label_4.setText(_translate("ActiveTracker", "06:30:00"))
        self.comboBox.setItemText(0, _translate("ActiveTracker", "Project"))
        self.comboBox.setItemText(1, _translate("ActiveTracker", "Project_2"))
        self.comboBox.setItemText(2, _translate("ActiveTracker", "Project_3"))
        self.comboBox_2.setItemText(0, _translate("ActiveTracker", "Task"))
        self.comboBox_2.setItemText(1, _translate("ActiveTracker", "Task_1"))
        self.comboBox_2.setItemText(2, _translate("ActiveTracker", "Task_2"))
        self.pushButton.setText(_translate("ActiveTracker", "+"))
        self.pushButton_2.setText(_translate("ActiveTracker", "Sync"))
        self.pushButton_3.setText(_translate("ActiveTracker", "Start/Stop"))
        self.label_6.setText(_translate("ActiveTracker", "Recent Tasks"))
        self.label_7.setText(_translate("ActiveTracker", "Task 1"))
        self.label_8.setText(_translate("ActiveTracker", "Active Time"))
        self.label_9.setText(_translate("ActiveTracker", "06:30:00"))
        self.label_10.setText(_translate("ActiveTracker", "Today\'s Total"))
        self.label_22.setText(_translate("ActiveTracker", "54:30:00"))
        self.label_23.setText(_translate("ActiveTracker", "Week Total"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tracker = QMainWindow()  # Change QWidget to QMainWindow here
    ui = Ui_ActiveTracker()
    ui.setupUi(tracker)
    tracker.show()
    sys.exit(app.exec_())