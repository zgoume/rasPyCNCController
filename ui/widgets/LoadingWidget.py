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

from PySide2 import QtCore, QtGui, QtWidgets

import sys

class LoadingWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, Splash):
        Splash.setObjectName("Splash")
        Splash.resize(480, 320)

        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addStretch()

        # Define a label for displaying GIF
        self.label = QtWidgets.QLabel(Splash)
        self.label.setObjectName("label")
        self.movie = QtGui.QMovie("images/loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        layout.addWidget(self.label)

        self.AbortButton = QtWidgets.QPushButton(Splash)
        self.AbortButton.resize(250, 50)
        self.AbortButton.setStyleSheet('QPushButton {background-color: black; color: #4af626; border:2px solid #4af626;}')
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(27)
        font.setWeight(50)
        font.setBold(False)
        self.AbortButton.setFont(font)
        self.AbortButton.setObjectName("AbortButton")
        self.AbortButton.clicked.connect(self.destroy)

        layout.addWidget(self.AbortButton)

        layout.addStretch()
        self.setLayout(layout)

        self.retranslateUi(Splash)
        QtCore.QMetaObject.connectSlotsByName(Splash)

    def retranslateUi(self, Splash):
        Splash.setWindowTitle(QtWidgets.QApplication.translate("Splash", "Form", None, -1))
        #self.label.setText(QtWidgets.QApplication.translate("Splash", "Some text here", None, -1))
        self.AbortButton.setText(QtWidgets.QApplication.translate("Splash", "Abort", None, -1))

    def destroy(self):
        sys.exit(0)