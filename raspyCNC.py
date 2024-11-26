#!/usr/bin/env python

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

from PySide2.QtGui import *
from PySide2.QtWidgets import *

from gcode.GrblWriterBasic import GrblWriterBasic
from gcode.GrblWriter import GrblWriter
from ui.JogWidget.JogWidget import JogWidget
from ui.RunWidget.RunWidget import RunWidget
from ui.MoveWidget.MoveWidget import MoveWidget
from ui.FileListWidget.FileListWidget import FileListWidget
from ui.SplashWidget.SplashWidget import SplashWidget
from ui.MainWindow.MainWindow import MainWindow
from ui.AppWindow.AppWindow import AppWindow

import sys
import time
import argparse
from utils.string_format import config_string_format
from qasync import QEventLoop
import asyncio



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A convenient GUI for CNC control")
    parser.add_argument("-f", "--fullscreen", action="store_true", help="make app fullscreen")
    parser.add_argument("-d", "--dummy", action="store_true", help="use dummy sender (debug)")
    parser.add_argument("-n", "--newgui", action="store_true", help="use new GUI")

    args = parser.parse_args()

    app = QApplication(sys.argv)
    
    # Get screen size for fullscreen
    screen = app.primaryScreen()
    size = screen.size()
    rect = screen.availableGeometry()
    
    app.setStyle(QStyleFactory.create('Breeze'))

    if args.newgui:
        window = AppWindow()
    else:
        window = MainWindow()
    if args.fullscreen:
        window.setGeometry(0, 0, rect.width(), rect.height())
        
    window.show()
    
    window.start_app(args.dummy)

    sys.exit(app.exec_())





