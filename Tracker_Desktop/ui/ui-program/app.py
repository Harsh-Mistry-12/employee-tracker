from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("Techie Lama")
        self.initUI()
        
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World...")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Punch In")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You successfully Punched In!!!")
        self.updated()
    
    def updated(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
window()