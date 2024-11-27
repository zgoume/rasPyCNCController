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

class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, parent):
        parent.setObjectName("Main")
        parent.resize(480, 320)

        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(27)
        font.setWeight(50)
        font.setBold(False)

        fontBold = QtGui.QFont()
        fontBold.setFamily("FreeSans")
        fontBold.setPointSize(27)
        fontBold.setWeight(50)
        fontBold.setBold(True)

        layout = QtWidgets.QHBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)

        group = QtWidgets.QGroupBox()
        group.setStyleSheet("QGroupBox { border: 2px solid #4af626;  border-radius: 10px;} ")

        leftLayout = QtWidgets.QVBoxLayout()
        coordLayout = QtWidgets.QGridLayout()

        self.zeroXBtn = QtWidgets.QPushButton(parent)
        self.zeroXBtn.setFixedSize(150, 50)
        self.zeroXBtn.setStyleSheet('QPushButton {background-color: black; color: #4af626; border:2px solid #4af626;}')
        self.zeroXBtn.setFont(fontBold)
        self.zeroXBtn.setObjectName("zeroXBtn")
        
        self.zeroXLbl = QtWidgets.QLabel(parent)
        self.zeroXLbl.setFont(font)
        self.zeroXLbl.setFixedSize(250, 50)
        self.zeroXLbl.setAlignment(QtCore.Qt.AlignLeft)
        self.zeroXLbl.setStyleSheet('color: #4af626; border:2px solid #4af626;')
        self.zeroXLbl.setObjectName("zeroXLbl")

        coordLayout.addWidget(self.zeroXBtn, 0, 0)
        coordLayout.addWidget(self.zeroXLbl, 0, 1)

        self.zeroYBtn = QtWidgets.QPushButton(parent)
        self.zeroYBtn.setFixedSize(150, 50)
        self.zeroYBtn.setStyleSheet('QPushButton {background-color: black; color: #4af626; border:2px solid #4af626;}')
        self.zeroYBtn.setFont(fontBold)
        self.zeroYBtn.setObjectName("zeroYBtn")

        self.zeroYLbl = QtWidgets.QLabel(parent)
        self.zeroYLbl.setFont(font)
        self.zeroYLbl.setFixedSize(250, 50)
        self.zeroYLbl.setAlignment(QtCore.Qt.AlignLeft)
        self.zeroYLbl.setStyleSheet('color: #4af626; border:2px solid #4af626;')
        self.zeroYLbl.setObjectName("zeroYLbl")

        coordLayout.addWidget(self.zeroYBtn, 1, 0)
        coordLayout.addWidget(self.zeroYLbl, 1, 1)

        self.zeroZBtn = QtWidgets.QPushButton(parent)
        self.zeroZBtn.setFixedSize(150, 50)
        self.zeroZBtn.setStyleSheet('QPushButton {background-color: black; color: #4af626; border:2px solid #4af626;}')
        self.zeroZBtn.setFont(fontBold)
        self.zeroZBtn.setObjectName("zeroZBtn")

        self.zeroZLbl = QtWidgets.QLabel(parent)
        self.zeroZLbl.setFont(font)
        self.zeroZLbl.setFixedSize(250, 50)
        self.zeroZLbl.setAlignment(QtCore.Qt.AlignLeft)
        self.zeroZLbl.setStyleSheet('color: #4af626; border:2px solid #4af626;')
        self.zeroZLbl.setObjectName("zeroZLbl")

        coordLayout.addWidget(self.zeroZBtn, 2, 0)
        coordLayout.addWidget(self.zeroZLbl, 2, 1)

        self.zeroAllBtn = QtWidgets.QPushButton(parent)
        self.zeroAllBtn.setFixedHeight(50)
        self.zeroAllBtn.setStyleSheet('QPushButton {background-color: black; color: #4af626; border:2px solid #4af626;}')
        self.zeroAllBtn.setFont(fontBold)
        self.zeroAllBtn.setObjectName("zeroZBtn")

        coordLayout.addWidget(self.zeroAllBtn, 3, 0, 2, 0)



        leftLayout.addLayout(coordLayout)
        group.setLayout(leftLayout)
        layout.addWidget(group)
        self.setLayout(layout)

        self.retranslateUi(parent)
        # QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, parent):
        parent.setWindowTitle(QtWidgets.QApplication.translate("Main", "Form", None, -1))
        self.zeroXLbl.setText(QtWidgets.QApplication.translate("Main", "0.0", None, -1))
        self.zeroYLbl.setText(QtWidgets.QApplication.translate("Main", "0.0", None, -1))
        self.zeroZLbl.setText(QtWidgets.QApplication.translate("Main", "0.0", None, -1))
        self.zeroXBtn.setText(QtWidgets.QApplication.translate("Main", "Zero X", None, -1))
        self.zeroYBtn.setText(QtWidgets.QApplication.translate("Main", "Zero Y", None, -1))
        self.zeroZBtn.setText(QtWidgets.QApplication.translate("Main", "Zero Z", None, -1))
        self.zeroAllBtn.setText(QtWidgets.QApplication.translate("Main", "Zero All", None, -1))