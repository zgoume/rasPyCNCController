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
from ui.widgets.MainWidget import MainWidget

import sys
import time
import argparse
from utils.string_format import config_string_format




class AppWindow(QStackedWidget):

    def __init__(self, parent=None):
        QStackedWidget.__init__(self,parent)
        self.resize(480, 320)
        self.setStyleSheet('background: black;')

    def start_app(self, dummy = False):
        self.loadWidget = LoadingWidget(self)
        self.addWidget(self.loadWidget)
        self.setCurrentWidget(self.loadWidget)
        QApplication.processEvents()

        if dummy:
            self.grblWriter = GrblWriterBasic()
            time.sleep(2)
        else:
            self.grblWriter = GrblWriter()
            self.grblWriter.grbl_error.connect(self.ask_perform_reset)

        # here wait for GRBL and show splash screen
        while not self.grblWriter.open():
            QApplication.processEvents()

        self.mainWidget = MainWidget(self)
        self.addWidget(self.mainWidget)
        self.setCurrentWidget(self.mainWidget)
        QApplication.processEvents()

    def ask_perform_reset(self, errorLine):
        print("DEBUG | ask_perform_reset")
        if self.grblWriter.resetting:
            return
        
        if self.runWidget.running: # the run widget deals with errors on its own
            return
        res = QMessageBox.critical(self, "Grbl Error", "%s\nPerform reset?" % (errorLine),
                                      QMessageBox.Yes | QMessageBox.No)
        if res == QMessageBox.Yes:
            self.grblWriter.reset()
