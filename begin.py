from control.MainWindow import mainWidget
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import os
import images
import sys
if __name__ == "__main__":
    #os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'
    #app = 0
    app = QtWidgets.QApplication(sys.argv)
    win = mainWidget()
    win.setObjectName("MainWindow")
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap(":/ui/background.jpg")))
    win.setPalette(palette)
    win.showMaximized()

    sys.exit(app.exec_())

