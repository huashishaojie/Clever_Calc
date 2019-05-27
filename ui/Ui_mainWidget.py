# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\毕业设计\project1.0\ui\mainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTextEdit, QLineEdit

from control.paintWidget import paintWidget
from control.recognition import *
from control.calauation import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.paintWidget = paintWidget(Form)
        self.paintWidget.setObjectName("paintwidget")
        self.paintWidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.paintWidget.setGeometry(QtCore.QRect(0, 0, 1920, 700))
        self.textEdit = QLineEdit(Form)
        self.textEdit.setStyleSheet("background: transparent;border-width:0;border-style:outset")
        self.textEdit.setReadOnly(True)
        self.textEdit.setGeometry(QtCore.QRect(60, 834, 600, 120))

        self.textEdit.setFont(QtGui.QFont("Times New Roman", 50))


        self.recognizeButton = QtWidgets.QPushButton(Form)
        self.recognizeButton.setObjectName("recogizeButton")
       # self.recognizeButton.setMinimumSize(QtCore.QSize(200, 50))
        self.recognizeButton.setGeometry(QtCore.QRect(1662, 790, 120, 60))

        self.calculateButton = QtWidgets.QPushButton(Form)
        self.calculateButton.setObjectName("calculateButton")
      #  self.calculateButton.setMinimumSize(QtCore.QSize(200, 50))
        self.calculateButton.setGeometry(QtCore.QRect(1620, 845, 120, 60))

        self.clearButton = QtWidgets.QPushButton(Form)
     #   self.clearButton.setMinimumSize(QtCore.QSize(200, 50))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.setGeometry(QtCore.QRect(1700, 895, 120, 60))

        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.recognizeButton.setFont(QtGui.QFont("黑体", 35))
        self.recognizeButton.setStyleSheet("background: transparent")
        self.calculateButton.setFont(QtGui.QFont("黑体", 35))
        self.calculateButton.setStyleSheet("background: transparent")
        self.clearButton.setFont(QtGui.QFont("黑体", 35))
        self.clearButton.setStyleSheet("background: transparent")
        self.recognizeButton.setText(_translate("Form", "识别"))
        self.calculateButton.setText(_translate("Form", "计算"))
        self.clearButton.setText(_translate("Form", "清除"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.showMaximized()
    sys.exit(app.exec_())


