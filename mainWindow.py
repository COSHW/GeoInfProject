# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1153, 776)
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 720, 531, 22))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pictire = QtWidgets.QLabel(Dialog)
        self.pictire.setGeometry(QtCore.QRect(10, 30, 1131, 661))
        self.pictire.setObjectName("pictire")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(720, 720, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 720, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(980, 720, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.KPFU = QtWidgets.QLabel(Dialog)
        self.KPFU.setGeometry(QtCore.QRect(500, 170, 211, 151))
        self.KPFU.setText("")
        self.KPFU.setObjectName("KPFU")
        self.UNIKS = QtWidgets.QLabel(Dialog)
        self.UNIKS.setGeometry(QtCore.QRect(700, 430, 151, 221))
        self.UNIKS.setText("")
        self.UNIKS.setObjectName("UNIKS")
        self.GLAV_ZD = QtWidgets.QLabel(Dialog)
        self.GLAV_ZD.setGeometry(QtCore.QRect(280, 460, 411, 211))
        self.GLAV_ZD.setText("")
        self.GLAV_ZD.setObjectName("GLAV_ZD")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pictire.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix/jj.png\"/></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Площадь"))
        self.pushButton_2.setText(_translate("Dialog", "Координаты"))
        self.pushButton_3.setText(_translate("Dialog", "Координата"))

