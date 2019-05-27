import sys
sys.path.append('../')
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QPixmap, QPen, QBrush, QCursor
from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from ui.Ui_paintWidget import Ui_Form
import numpy as np
import images
class paintWidget(QWidget,  Ui_Form):
    
    #value_changed = pyqtSignal()
    
    
    def __init__(self, parent = None):
        super(paintWidget, self).__init__(parent)
        self.draw_model = True
        self.setupUi(self)
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.eraser_pos = QPoint()
        self.datalist = []
        self.resultWidget = QLabel()
        self.mypen = QPen(Qt.black, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.eraser = QPixmap(":/src/curosr/eraser.png")

    def showResult(self):
        self.resultWidget.setText("hello")

    def resizeEvent(self, event):
        self.pix = QPixmap(self.width(), self.height())
        self.pix.fill(Qt.white)
        
    def paintEvent(self,  event):
        pp = QPainter(self.pix)
        if(self.draw_model):
            mypen = QPen(Qt.black, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            pp.setPen(mypen)
            pp.drawLine(self.lastPoint,  self.endPoint)
            self.lastPoint = self.endPoint
        else:
            mybrush = QBrush(Qt.white)
            pp.fillRect(self.eraser_pos.x()-20, self.eraser_pos.y()-20, 40, 40, mybrush)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draw_model = True
            self.lastPoint = event.pos()
            self.datalist.append([self.lastPoint.x(), self.lastPoint.y()])
            self.endPoint = self.lastPoint + QPoint(0, 1)
            self.update()
        elif event.button() == Qt.RightButton:
            self.setCursor(QCursor(self.eraser, -1, -1))
            self.draw_model = False
            self.eraser_pos = event.pos()
            self.update()
            
    def mouseMoveEvent(self, event):
        if event.buttons() and event.buttons() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.datalist.append([self.endPoint.x(), self.endPoint.y()])
            self.update()
        elif event.buttons() and event.buttons() == Qt.RightButton:
            self.eraser_pos = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        self.setCursor(QCursor(Qt.CrossCursor))
        
    def save_image(self):
        if(self.datalist):
            data = np.array(self.datalist)
            maxx = max(data[:, 0])+5
            maxy = max(data[:, 1])+5
            minx = min(data[:, 0])-5
            miny = min(data[:, 1])-5
            image = self.pix.copy(minx, miny, maxx-minx, maxy-miny)
            image.save("tmp.png")
            return True
        else:
            return False
        #return [minx, miny]
        
    '''def set_label(self, list):
        for i in list:
            if(isinstance(i, dict) and len(i["char"]) >= 5):
                label = imageLabel(self)
                label.set_label(i)
                label.value_changed.connect(self.value_changed)
    '''           
    def clear(self):
        self.datalist.clear()
        self.pix.fill(Qt.white)
        self.update()
