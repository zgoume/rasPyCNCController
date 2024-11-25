# rasPyCNCController
# Copyright 2016 Francesco Santini <francesco.santini@gmail.com>
#
# This file is part of rasPyCNCController.
#
# rasPyCNCController is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rasPyCNCController is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rasPyCNCController.  If not, see <http://www.gnu.org/licenses/>.

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from .moveWidget_ui import Ui_moveWidget
import pycnc_config
from gcode.GCodeRunner import GCodeRunner
import os.path
import time
import math
from pyJoy.JoyEvdev import JoyEvdevUIEventGenerator

class MoveWidget(Ui_moveWidget, QWidget):

    error_event = Signal(object)
    stop_event = Signal()
    end_event = Signal()
    pause_event = Signal(object)
    move_event = Signal()
    jog_widget = Signal()
    pause_clicked = Signal()

    steps = [0.1, 0.5, 1, 2, 5, 10, 50]

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.PauseButton.clicked.connect(lambda : self.retEvent())
        self.joyPad = self.getJoyWidget()
        self.accumulatedMove = None
        self.eventTimer = QTimer(self)
        self.eventTimer.timeout.connect(self.sendMoveEvent)
        self.joyPad.joyChanged.connect(self.start_sending_commands)
        self.joyPad.joyReleased.connect(self.stop_sending_commands_and_reset)

    def retEvent(self):
        print("kill window")
        self.pause_clicked.emit()
        self.destroy()

    def setGrbl(self, grblWriter):
        self.jogHelper.setGrbl(grblWriter)

    def sendMoveEvent(self):
        self.processMoves()
        xyz = self.accumulatedMove

        # go slower in Z moves
        if xyz[2] != 0:  # Z axis
            minFeed = pycnc_config.MIN_FEED_Z
            maxFeed = pycnc_config.MAX_FEED_Z
        else:
            minFeed = pycnc_config.MIN_FEED
            maxFeed = pycnc_config.MAX_FEED

        feed = minFeed + int(math.sqrt(xyz[0] ** 2 + xyz[1] ** 2 + xyz[2] ** 2) * (maxFeed - minFeed) / 10)
        # feed = int(math.sqrt(xyz[0]**2 + xyz[1]**2 + xyz[2]**2)*maxFeed)
        if feed < minFeed: feed = minFeed
        if feed > maxFeed: feed = maxFeed

        self.relativeMove(xyz, feed)
        # print cmd

    def processMoves(self):

        x, y = self.joyPad.value()

        # Simulate async behavior (e.g., network call)
        multipX = 1 if x > 0 else -1
        if (x != 0):
            stepX = self.steps[abs(x) - 1]
        else:
            stepX = 0
        
        multipY = 1 if y > 0 else -1
        if (y != 0):
            stepY = self.steps[abs(y) - 1]
        else:
            stepY = 0

        self.accumulatedMove = [(multipX * stepX), (multipY * stepY), 0]
        
    def start_sending_commands(self):
        self.eventTimer.start(100)

    def stop_sending_commands_and_reset(self):
        self.eventTimer.stop()
        #self.XSlider.setValue(0)  # Reset slider to middle position

