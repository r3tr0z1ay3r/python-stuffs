import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog,QMainWindow,QProgressBar,QPushButton
from PyQt5.uic import loadUi
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #Importing thE GUI
        loadUi("F:\Python projects(Pycharm)\GUI\QT5\Student_Form.ui",self)
        #Creating a browse file button which points to the function to browse file dialog box
        self.Submit.clicked.connect(self.fileopen)
        self.nub = QPushButton("Make the bar go brr",self)
        self.nub.move(40,70)
        self.nub.clicked.connect(self.gobrr)
        self.pbar = QProgressBar(self)
        self.pbar.move(40,40)
        self.pbar.setFixedWidth(400)
        self.show()
    def gobrr(self):
        for i in range(1,101):
            self.pbar.setValue(i)
            time.sleep(0.1)
    #Function for the File browse dialogue box
    def fileopen(self):
        #
        fname = QFileDialog.getOpenFileName(self,"OpenFile","F:\Python projects(Pycharm)\GUI\QT5")
        self.lineEdit.setText(fname[0])

app = QApplication(sys.argv)
main = MainWindow()
#widget = QtWidgets.QStackedWidget()
#idget.addWidget(main)
#widget.show()
sys.exit(app.exec_())