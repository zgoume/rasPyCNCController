# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moveWidget/moveWidget.ui'
#
# Created: Wed Mar 14 07:27:30 2018
#      by: pyside-uic 0.2.15 running on PySide2.1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from gcode.JogHelper import JogHelper, JogHelper1_1
from utils.Joystick import Joystick
import asyncio
import pycnc_config

class Ui_moveWidget(object):

    

    def setupUi(self, moveWidget):
        moveWidget.setObjectName("moveWidget")
        moveWidget.resize(480, 320)
        self.PauseButton = QtWidgets.QPushButton(moveWidget)
        self.PauseButton.setGeometry(QtCore.QRect(240, 255, 231, 61))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(27)
        font.setWeight(75)
        font.setBold(True)
        self.PauseButton.setFont(font)
        self.PauseButton.setObjectName("PauseButton")

        # self.XSlider = QtWidgets.QSlider(QtCore.Qt.Vertical, moveWidget)
        # self.XSlider.setMinimum(len(self.steps) * -1)
        # self.XSlider.setMaximum(len(self.steps))
        # self.XSlider.setValue(0)
        # self.XSlider.sliderPressed.connect(self.start_sending_commands)
        # self.XSlider.sliderReleased.connect(self.stop_sending_commands_and_reset)
        # self.XSlider.setGeometry(QtCore.QRect(50, 50, 40, 300))
        # self.XSlider.setObjectName("XSlider")
        # self.is_sending_command = False

        self.XSlider = Joystick(moveWidget)
        self.XSlider.setRangeValue(len(self.steps))
        self.XSlider.setGeometry(QtCore.QRect(50, 50, 200, 200))
        self.XSlider.setObjectName("XSlider")
        self.is_sending_command = False

        self.retranslateUi(moveWidget)
        QtCore.QMetaObject.connectSlotsByName(moveWidget)

        self.jogHelper = JogHelper()

    def relativeMove(self, xyz, feed):
        if self.jogHelper.isBusy(): return
        if feed is not None and feed <= 0: feed = None
        self.jogHelper.relative_move(xyz, feed)

    def retranslateUi(self, moveWidget):
        moveWidget.setWindowTitle(QtWidgets.QApplication.translate("moveWidget", "Form", None, -1))
        self.PauseButton.setText(QtWidgets.QApplication.translate("moveWidget", "Back", None, -1))

    def getJoyWidget(self):
        return self.XSlider

