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

    steps = [0.1, 0.5, 1, 2, 5, 10]

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
        self.XSlider.joyChanged.connect(self.start_sending_commands)
        self.XSlider.joyReleased.connect(self.stop_sending_commands_and_reset)
        self.XSlider.setGeometry(QtCore.QRect(50, 50, 202, 202))
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

    async def send_command(self, x, y):
        # Simulate async behavior (e.g., network call)
        if (x != 0):
            multipX = 1 if x > 0 else -1
            stepX = self.steps[abs(x) - 1]
        else:
            multipX = 1
            stepX = 0

        if (y != 0):
            multipY = 1 if y > 0 else -1
            stepY = self.steps[abs(y) - 1]
        else:
            multipY = 1
            stepY = 0

        self.relativeMove([(multipX * stepX), (multipY * stepY), 0], pycnc_config.MAX_FEED)

        await asyncio.sleep(0.05)  # Simulated delay (adjust as needed)

    async def handle_commands(self):
        self.is_sending_command = True

        while self.is_sending_command:
            x, y = self.XSlider.value()
            await self.send_command(x, y)

    def start_sending_commands(self):
        asyncio.ensure_future(self.handle_commands())
        

    def stop_sending_commands_and_reset(self):
        self.is_sending_command = False
        #self.XSlider.setValue(0)  # Reset slider to middle position

