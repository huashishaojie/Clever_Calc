import sys

from qtpy import QtWidgets, QtCore

sys.path.append('../')
from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit
from ui import Ui_mainWidget
from data.imageList import imageList
from data.posList import posList
from .recognition import recognize
from .calauation import calc
from .regularcheck import re_check
import cv2


class mainWidget(QWidget,  Ui_mainWidget.Ui_Form):
    
    def __init__(self, parent=None):
        super(mainWidget, self).__init__(parent)
        self.setupUi(self)
        #self.basepoint = []
        self.imagelist = imageList()
        self.poslist = posList()
        self.finallist = []
        self.equation = []
        self.strlist = ""
        self.recognizeButton.clicked.connect(self.recognize)
        self.calculateButton.clicked.connect(self.calculate)
        self.clearButton.clicked.connect(self.clear_all)
        #self.paintWidget.value_changed.connect(self.get_result)
    
    def recognize(self):
        if(self.paintWidget.save_image() == False):
            return
        image = cv2.imread("tmp.png", 0)

        if(self.imagelist.deivde_image(image) == False):
            return
        lineimage = self.imagelist.get_lineimage()

        self.poslist.divide_pos(lineimage)
        self.finallist = self.imagelist.set_position(self.poslist)

        #self.set_point(self.finallist)

        #print(self.finallist)
        recognize(self.finallist)

        #print(self.finallist)
        self.get_result()

        #self.paintWidget.set_label(self.finallist)

    def get_result(self):
        self.equation.clear()
        for i in self.finallist:
            if(isinstance(i, dict)):
                self.equation.append(i["char"])
            else:
                self.equation.append(i)
        self.strlist = re_check(self.equation)
        self.textEdit.setPlaceholderText(str(self.strlist))



    def clear_all(self):
        self.imagelist.clear()
        self.poslist.clear()
        self.paintWidget.clear()
        self.finallist.clear()
        self.equation.clear()
        self.strlist = ""
        
    def calculate(self):
        res = calc(self.strlist)
        if(res == "INPUT ERROR"):
            self.textEdit.setPlaceholderText(str(self.strlist) + ": " + str(res))
        else:
            self.textEdit.setPlaceholderText(str(self.strlist) + "=" + str(res))


        
        
