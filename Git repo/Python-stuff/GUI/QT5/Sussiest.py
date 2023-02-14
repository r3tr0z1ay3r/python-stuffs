# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Student_FormmbtmAZ.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Student_Portal = QLabel(self.centralwidget)
        self.Student_Portal.setObjectName(u"Student_Portal")
        self.Student_Portal.setGeometry(QRect(330, 40, 161, 71))
        font1 = QFont()
        font1.setPointSize(18)
        self.Student_Portal.setFont(font1)
        self.Submit = QPushButton(self.centralwidget)
        self.Submit.setObjectName(u"Submit")
        self.Submit.setGeometry(QRect(320, 410, 181, 41))
        self.Submit.setMouseTracking(True)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(187, 146, 461, 211))
        font2 = QFont()
        font2.setPointSize(20)
        self.widget.setFont(font2)
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.Sem = QLabel(self.widget)
        self.Sem.setObjectName(u"Sem")
        self.Sem.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.Sem)

        self.Phone_No = QLabel(self.widget)
        self.Phone_No.setObjectName(u"Phone_No")
        self.Phone_No.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.Phone_No)

        self.Name = QLabel(self.widget)
        self.Name.setObjectName(u"Name")
        self.Name.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Name)

        self.Department = QLabel(self.widget)
        self.Department.setObjectName(u"Department")
        self.Department.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Department)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Student_Portal.setText(QCoreApplication.translate("MainWindow", u"Student Portal", None))
        self.Submit.setText(QCoreApplication.translate("MainWindow", u"SUBMIT", None))
        self.Sem.setText(QCoreApplication.translate("MainWindow", u"Sem", None))
        self.Phone_No.setText(QCoreApplication.translate("MainWindow", u"Phone no", None))
        self.Name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.Department.setText(QCoreApplication.translate("MainWindow", u"Department", None))
    # retranslateUi

main = Ui_MainWindow()
main.setupUi()