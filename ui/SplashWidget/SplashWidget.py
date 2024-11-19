#!/usr/bin/env python

# rasPyCNCController
# Copyright 2024 zgoume <zgoume[arobase]]gmail.com>
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
from .splash_ui import Ui_Splash


class SplashWidget(QWidget, Ui_Splash):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

    def setText(self, txt):
        self.label.setText(txt)