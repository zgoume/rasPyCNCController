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
from gcode.GCodeRunner import GCodeRunner
import os.path
import time
from pyJoy.JoyEvdev import JoyEvdevUIEventGenerator

class MoveWidget(Ui_moveWidget, QWidget):

    error_event = Signal(object)
    stop_event = Signal()
    end_event = Signal()
    pause_event = Signal(object)
    move_event = Signal()
    jog_widget = Signal()
    pause_clicked = Signal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.PauseButton.clicked.connect(lambda : self.retEvent())

    def retEvent(self):
        print("kill window")
        self.pause_clicked.emit()
        self.destroy()

    def setGrbl(self, grblWriter):
        self.jogHelper.setGrbl(grblWriter)

