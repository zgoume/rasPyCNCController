# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash.ui'
#
# Created: Wed Mar 14 07:27:30 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Splash(object):
    def setupUi(self, Splash):
        Splash.setObjectName("Splash")
        Splash.resize(480, 320)
        self.label = QtWidgets.QLabel(Splash)
        self.label.setGeometry(QtCore.QRect(0, 110, 480, 71))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.AbortButton = QtWidgets.QPushButton(Splash)
        self.AbortButton.setGeometry(QtCore.QRect(154, 189, 181, 71))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(27)
        font.setWeight(50)
        font.setBold(False)
        self.AbortButton.setFont(font)
        self.AbortButton.setObjectName("AbortButton")

        self.retranslateUi(Splash)
        QtCore.QMetaObject.connectSlotsByName(Splash)

    def retranslateUi(self, Splash):
        Splash.setWindowTitle(QtWidgets.QApplication.translate("Splash", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Splash", "Some text here", None, -1))
        self.AbortButton.setText(QtWidgets.QApplication.translate("Splash", "Abort", None, -1))

