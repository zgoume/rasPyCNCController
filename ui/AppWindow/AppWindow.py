#!/usr/bin/env python

# rasPyCNCController
# Copyright 2024 zgoume <zgoume[arobase]gmail.com>
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

from PySide2.QtGui import *
from PySide2.QtWidgets import *

from gcode.GrblWriterBasic import GrblWriterBasic
from gcode.GrblWriter import GrblWriter
from ui.widgets.LoadingWidget import LoadingWidget

import sys
import time
import argparse
from utils.string_format import config_string_format
from qasync import QEventLoop
import asyncio




class AppWindow(QStackedWidget):

    def __init__(self, parent=None):
        QStackedWidget.__init__(self,parent)
        self.resize(480, 320)
        self.setStyleSheet('background: black; QPushButton {background-color: black; color: #4af626; border:2px solid #4af626;}')

    def start_app(self, dummy = False):
        self.loadwidget = LoadingWidget(self)
        self.addWidget(self.loadwidget)
        self.setCurrentWidget(self.loadwidget)
