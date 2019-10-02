import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import mainWindow
import info
import label
import psycopg2
from functools import partial
import io
from scipy.ndimage import imread
# coding: utf-8


class AppStart(QtWidgets.QMainWindow, mainWindow.Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.informationWindow = infoWindow()
        self.labelWindow = labelWindow()

        self.coordinates = False

        input_image = imread('jj.png')
        height, width, channels = input_image.shape
        bytesPerLine = channels * width
        qImg = QtGui.QImage(input_image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        pixmap01 = QtGui.QPixmap.fromImage(qImg)
        pixmap_image = QtGui.QPixmap(pixmap01)
        self.pictire.setPixmap(pixmap_image)
        self.pictire.setAlignment(QtCore.Qt.AlignCenter)
        self.pictire.setScaledContents(True)
        self.pictire.setMinimumSize(1, 1)
        self.pictire.show()

        self.conn = psycopg2.connect("dbname='GeoInf' user='postgres' password='Lovunod2302' host='localhost' port='5432'")
        self.cur = self.conn.cursor()
        self.KPFU.mousePressEvent = lambda x: self.information("KPFU")
        self.UNIKS.mousePressEvent = lambda x: self.information("UNIKS")
        self.GLAV_ZD.mousePressEvent = lambda x: self.information("GLAV_ZD")
        self.pushButton_3.clicked.connect(self.switch)
        self.pictire.mousePressEvent = self.click
        self.horizontalSlider.valueChanged.connect(self.pic_resize)

    def click(self, event):
        if self.coordinates == False:
            pass
        elif self.coordinates == True:
            x = event.pos().x()
            y = event.pos().y()
            self.labelWindow.show()
            self.labelWindow.label.setText("x: "+str(x)+", y:"+str(y))
            self.coordinates = False
            self.KPFU.mousePressEvent = lambda x: self.information("KPFU")
            self.UNIKS.mousePressEvent = lambda x: self.information("UNIKS")
            self.GLAV_ZD.mousePressEvent = lambda x: self.information("GLAV_ZD")

    def information(self, place):
        if place == "KPFU":
            place = 1
        elif place == "GLAV_ZD":
            place = 2
        else:
            place = 3
        self.cur.execute("select * from info where id = "+str(place))
        to_show = self.cur.fetchall()
        self.informationWindow.show()
        for i in range(len(to_show[0])):
            self.informationWindow.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(str(to_show[0][i])))

    def switch(self):
        self.coordinates = True
        self.KPFU.mousePressEvent = None
        self.UNIKS.mousePressEvent = None
        self.GLAV_ZD.mousePressEvent = None

    def pic_resize(self):
        self.pictire.setGeometry(QtCore.QRect(10, 30, 1131*(self.horizontalSlider.value()/50), 661*(self.horizontalSlider.value()/50)))


class infoWindow(QtWidgets.QMainWindow, info.Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)


class labelWindow(QtWidgets.QMainWindow, label.Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AppStart()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
