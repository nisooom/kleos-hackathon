import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 200))    
        self.setWindowTitle("PyQt button example - pythonprogramminglanguage.com") 

        pybutton = QPushButton('Click me', self)
        pybutton.setObjectName('evil')
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(50, 50)       
        pybutton = QPushButton('Click me', self)
        # pybutton.setObjectName('evil')
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(150, 50)  

    def clickMethod(self):
        print('Clicked Pyqt button.')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    qss_stylesheet = open('index.css').read()
    mainWin.setStyleSheet(qss_stylesheet)
    mainWin.show()
    sys.exit( app.exec() )