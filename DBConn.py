# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DBConn.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess
import sqlite3


class Ui_MainWindow(object):
    conn = sqlite3.connect('DBFile.sqlite3')
    cur = conn.cursor()
    comma = 'sqlite3 DBFile.sqlite3 ".mode box --wrap 30" "SELECT * FROM user;"'
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(552, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gettable = QtWidgets.QPushButton(self.centralwidget)
        self.gettable.setGeometry(QtCore.QRect(10, 340, 101, 41))
        self.gettable.setObjectName("gettable")
        self.setvalues = QtWidgets.QPushButton(self.centralwidget)
        self.setvalues.setGeometry(QtCore.QRect(440, 340, 101, 41))
        self.setvalues.setObjectName("setvalues")
        self.name_f = QtWidgets.QTextEdit(self.centralwidget)
        self.name_f.setGeometry(QtCore.QRect(20, 60, 256, 31))
        self.name_f.setObjectName("name_f")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.age_f = QtWidgets.QTextEdit(self.centralwidget)
        self.age_f.setGeometry(QtCore.QRect(20, 120, 256, 31))
        self.age_f.setObjectName("age_f")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 71, 16))
        self.label_4.setObjectName("label_4")
        self.spec_f = QtWidgets.QTextEdit(self.centralwidget)
        self.spec_f.setGeometry(QtCore.QRect(20, 180, 256, 31))
        self.spec_f.setObjectName("spec_f")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(400, 0, 151, 51))
        self.frame.setStyleSheet("background-color: rgb(229, 255, 241);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 30))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.functionality()
        
    def functionality(self):
        self.gettable.clicked.connect(lambda: self.getVal())
        self.setvalues.clicked.connect(lambda: self.setVal())
        
    def sqlwork(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            specialisation TEXT NOT NULL
            )''')
        
        print("Ввод успешен")
    
    def showsql(self):
        subprocess.run(f'cmd /c start cmd /k "{self.comma}"', shell=True)
        
        
    def setValues(self):
        name = self.name_f.toPlainText()
        age = int(self.age_f.toPlainText())
        spec = self.spec_f.toPlainText()
        
        try:
            self.cur.execute('''
                INSERT INTO user (name, age, specialisation)
                VALUES (?, ?, ?)
            ''', (name, age, spec))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gettable.setText(_translate("MainWindow", "Get table"))
        self.setvalues.setText(_translate("MainWindow", "Set values"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Age"))
        self.label_4.setText(_translate("MainWindow", "Specification"))
        self.label.setText(_translate("MainWindow", "PyQt DB connecter"))  
        
    def getVal(self):
        self.sqlwork()
        self.showsql()
    
    def setVal(self):
        self.setValues()
        
    def createDB(self):
        file = open("DBFile.sqlite3", "w+")
        file.close

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    Ui_MainWindow.conn.close()
    Ui_MainWindow.cur.close()
