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
from utils import Joystick, ZSlider

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

        globalLayout = QtWidgets.QVBoxLayout()

        # QGroupBox en haut (100px de hauteur et toute la largeur)
        top_group_box = QtWidgets.QGroupBox()
        top_group_box.setFixedHeight(75)
        top_group_layout = QtWidgets.QVBoxLayout()
        top_group_box.setLayout(top_group_layout)
        globalLayout.addWidget(top_group_box)

        layout = QtWidgets.QHBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)

        group = QtWidgets.QGroupBox()
        
        leftLayout = QtWidgets.QVBoxLayout()
        coordLayout = QtWidgets.QGridLayout()

        self.XLbl = QtWidgets.QLabel(parent)
        self.XLbl.setFont(font)
        self.XLbl.setFixedSize(50, 50)
        self.XLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.XLbl.setObjectName("XLbl")

        self.zeroXBtn = QtWidgets.QPushButton(parent)
        self.zeroXBtn.setFixedSize(50, 50)
        self.zeroXBtn.setFont(fontBold)
        self.zeroXBtn.setObjectName("zeroXBtn")
        
        self.zeroXLbl = QtWidgets.QLabel(parent)
        self.zeroXLbl.setFont(font)
        self.zeroXLbl.setFixedHeight(50)
        self.zeroXLbl.setMinimumWidth(200)
        self.zeroXLbl.setAlignment(QtCore.Qt.AlignLeft)
        self.zeroXLbl.setObjectName("zeroXLbl")
        size_policy = self.zeroXLbl.sizePolicy()
        size_policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Expanding)  # Permet de s'étendre verticalement
        self.zeroXLbl.setSizePolicy(size_policy)

        coordLayout.addWidget(self.XLbl, 0, 0)
        coordLayout.addWidget(self.zeroXLbl, 0, 1)
        coordLayout.addWidget(self.zeroXBtn, 0, 2)

        self.YLbl = QtWidgets.QLabel(parent)
        self.YLbl.setFont(font)
        self.YLbl.setFixedSize(50, 50)
        self.YLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.YLbl.setObjectName("YLbl")

        self.zeroYBtn = QtWidgets.QPushButton(parent)
        self.zeroYBtn.setFixedSize(50, 50)
        self.zeroYBtn.setFont(fontBold)
        self.zeroYBtn.setObjectName("zeroYBtn")

        self.zeroYLbl = QtWidgets.QLabel(parent)
        self.zeroYLbl.setFont(font)
        self.zeroYLbl.setFixedHeight(50)
        self.zeroYLbl.setMinimumWidth(200)
        self.zeroYLbl.setAlignment(QtCore.Qt.AlignLeft)
        self.zeroYLbl.setObjectName("zeroYLbl")
        size_policy = self.zeroYLbl.sizePolicy()
        size_policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Expanding)  # Permet de s'étendre verticalement
        self.zeroYLbl.setSizePolicy(size_policy)

        coordLayout.addWidget(self.YLbl, 1, 0)
        coordLayout.addWidget(self.zeroYLbl, 1, 1)
        coordLayout.addWidget(self.zeroYBtn, 1, 2)

        self.ZLbl = QtWidgets.QLabel(parent)
        self.ZLbl.setFont(font)
        self.ZLbl.setFixedSize(50, 50)
        self.ZLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ZLbl.setObjectName("ZLbl")

        self.zeroZBtn = QtWidgets.QPushButton(parent)
        self.zeroZBtn.setFixedSize(50, 50)
        self.zeroZBtn.setFont(fontBold)
        self.zeroZBtn.setObjectName("zeroZBtn")

        self.zeroZLbl = QtWidgets.QLabel(parent)
        self.zeroZLbl.setFont(font)
        self.zeroZLbl.setFixedHeight(50)
        self.zeroZLbl.setMinimumWidth(200)
        self.zeroZLbl.setAlignment(QtCore.Qt.AlignLeft)
        self.zeroZLbl.setObjectName("zeroZLbl")
        size_policy = self.zeroZLbl.sizePolicy()
        size_policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Expanding)  # Permet de s'étendre verticalement
        self.zeroZLbl.setSizePolicy(size_policy)

        coordLayout.addWidget(self.ZLbl, 2, 0)
        coordLayout.addWidget(self.zeroZLbl, 2, 1)
        coordLayout.addWidget(self.zeroZBtn, 2, 2)

        self.zeroAllBtn = QtWidgets.QPushButton(parent)
        self.zeroAllBtn.setFixedWidth(50)
        self.zeroAllBtn.setFont(fontBold)
        self.zeroAllBtn.setObjectName("zeroZBtn")
        size_policy = self.zeroAllBtn.sizePolicy()
        size_policy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)  # Permet de s'étendre verticalement
        self.zeroAllBtn.setSizePolicy(size_policy)

        coordLayout.addWidget(self.zeroAllBtn, 0, 3, 0, 3)

        # Layout principal
        main_layout = QtWidgets.QVBoxLayout()

        # Ligne 2 : Home all (largeur complète)
        btn_home_all = QtWidgets.QPushButton("Home All")
        btn_home_all.setStyleSheet("min-width: 200px;")  # Optionnel pour large bouton
        btn_home_all.setFont(fontBold)
        btn_home_all.setMinimumHeight(50)
        size_policy = btn_home_all.sizePolicy()
        size_policy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)  # Permet de s'étendre verticalement
        btn_home_all.setSizePolicy(size_policy)
        main_layout.addWidget(btn_home_all)

        # Ligne 1 : Home X, Home Y, Home Z
        line1_layout = QtWidgets.QHBoxLayout()
        btn_home_x = QtWidgets.QPushButton("Ω X")
        btn_home_x.setFont(fontBold)
        btn_home_x.setMinimumHeight(50)
        size_policy = btn_home_x.sizePolicy()
        size_policy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)  # Permet de s'étendre verticalement
        btn_home_x.setSizePolicy(size_policy)

        btn_home_y = QtWidgets.QPushButton("Ω Y")
        btn_home_y.setFont(fontBold)
        btn_home_y.setMinimumHeight(50)
        size_policy = btn_home_y.sizePolicy()
        size_policy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)  # Permet de s'étendre verticalement
        btn_home_y.setSizePolicy(size_policy)

        btn_home_z = QtWidgets.QPushButton("Ω Z")
        btn_home_z.setFont(fontBold)
        btn_home_z.setMinimumHeight(50)
        size_policy = btn_home_z.sizePolicy()
        size_policy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)  # Permet de s'étendre verticalement
        btn_home_z.setSizePolicy(size_policy)

        line1_layout.addWidget(btn_home_x)
        line1_layout.addWidget(btn_home_y)
        line1_layout.addWidget(btn_home_z)
        main_layout.addLayout(line1_layout)

        # Ligne 3 : Load File, Run
        line3_layout = QtWidgets.QHBoxLayout()

        btn_load_file = QtWidgets.QPushButton("Load")
        btn_load_file.setFont(fontBold)
        btn_load_file.setMinimumHeight(50)
        size_policy = btn_load_file.sizePolicy()
        size_policy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)  # Permet de s'étendre verticalement
        btn_load_file.setSizePolicy(size_policy)

        btn_run = QtWidgets.QPushButton("Run")
        btn_run.setFont(fontBold)
        btn_run.setMinimumHeight(50)
        size_policy = btn_run.sizePolicy()
        size_policy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)  # Permet de s'étendre verticalement
        btn_run.setSizePolicy(size_policy)

        line3_layout.addWidget(btn_load_file)
        line3_layout.addWidget(btn_run)

        main_layout.addLayout(line3_layout)

        leftLayout.addLayout(coordLayout)
        leftLayout.addLayout(main_layout)
        group.setLayout(leftLayout)
        layout.addWidget(group, stretch=1)

        group2 = QtWidgets.QGroupBox()
        group2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        # Créer un QTabBar
        self.tab_bar = QtWidgets.QTabBar()
        self.tab_bar.setShape(QtWidgets.QTabBar.RoundedWest)  # Orientation verticale
        size_policy = self.tab_bar.sizePolicy()
        size_policy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)  # Permet de s'étendre verticalement
        self.tab_bar.setSizePolicy(size_policy)

        # Ajouter des onglets
        self.tab_bar.addTab("Jog")
        self.tab_bar.addTab("Settings")

        # Connecter le signal de changement d'onglet
        self.tab_bar.currentChanged.connect(self.switch_tab)

        # Créer un QStackedWidget pour afficher différents widgets
        self.stacked_widget = QtWidgets.QStackedWidget()

        # Ajouter des widgets au QStackedWidget
        jogWidget = QtWidgets.QWidget()
        jogLayout = QtWidgets.QGridLayout()

        zSlide = ZSlider.ZSlider()
        zSlide.setFixedWidth(100)

        joy = Joystick.Joystick()
        width = joy.width()
        joy.setFixedHeight(width)

        XYLbl = QtWidgets.QLabel("X / Y")
        XYLbl.setFont(font)
        XYLbl.setFixedHeight(50)
        XYLbl.setAlignment(QtCore.Qt.AlignCenter)

        ZLbl = QtWidgets.QLabel("Z")
        ZLbl.setFont(font)
        ZLbl.setFixedHeight(50)
        ZLbl.setAlignment(QtCore.Qt.AlignCenter)

        jogLayout.addWidget(XYLbl, 0, 0)
        jogLayout.addWidget(ZLbl, 0, 1)
        jogLayout.addWidget(joy, 1, 0)
        jogLayout.addWidget(zSlide, 1, 1)
        # jogLayout.addWidget(joy, 0, 0)
        # jogLayout.addWidget(joy, 0, 1)
        jogWidget.setLayout(jogLayout)
        
        self.stacked_widget.addWidget(jogWidget)
        self.stacked_widget.addWidget(self.create_tab_content("Content for Tab 2"))

        # Layout principal
        rightLayout = QtWidgets.QHBoxLayout()
        rightLayout.addWidget(self.stacked_widget)
        rightLayout.addWidget(self.tab_bar)

        group2.setLayout(rightLayout)
        layout.addWidget(group2, stretch=2)

        globalLayout.addLayout(layout)

        self.setLayout(globalLayout)

        self.retranslateUi(parent)
        # QtCore.QMetaObject.connectSlotsByName(parent)

    def create_tab_content(self, text):
        """Créer un widget pour le contenu de chaque onglet."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel(text)
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)
        widget.setLayout(layout)
        return widget

    def switch_tab(self, index):
        """Changer de widget affiché dans le QStackedWidget."""
        self.stacked_widget.setCurrentIndex(index)

    def retranslateUi(self, parent):
        parent.setWindowTitle(QtWidgets.QApplication.translate("Main", "Form", None, -1))
        self.zeroXLbl.setText(QtWidgets.QApplication.translate("Main", "0.0", None, -1))
        self.zeroYLbl.setText(QtWidgets.QApplication.translate("Main", "0.0", None, -1))
        self.zeroZLbl.setText(QtWidgets.QApplication.translate("Main", "0.0", None, -1))
        self.XLbl.setText(QtWidgets.QApplication.translate("Main", "X", None, -1))
        self.YLbl.setText(QtWidgets.QApplication.translate("Main", "Y", None, -1))
        self.ZLbl.setText(QtWidgets.QApplication.translate("Main", "Z", None, -1))
        self.zeroXBtn.setText(QtWidgets.QApplication.translate("Main", "0", None, -1))
        self.zeroYBtn.setText(QtWidgets.QApplication.translate("Main", "0", None, -1))
        self.zeroZBtn.setText(QtWidgets.QApplication.translate("Main", "0", None, -1))
        self.zeroAllBtn.setText(QtWidgets.QApplication.translate("Main", "0", None, -1))