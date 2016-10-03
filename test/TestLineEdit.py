#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月29日
@author: Irony."[讽刺]
@site: alyl.vip, orzorz.vip, irony.coding.me , irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.TestLineEdit
@description: 
'''
import os
import sys

sys.path.insert(0, os.path.dirname(os.getcwd()))
print(sys.path)

from random import randrange
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

from QMaterial.Utils import Colors
from QMaterial.Widget.LineEdit import LineEdit




class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QGridLayout(self)
        colors = Colors.alls()
        for row, key in enumerate(colors):
            layout.addWidget(QLabel(key, self), row, 0, 1, 1)
            for column, value in enumerate(colors.get(key)):
                line = LineEdit(value._name, self)
                line.lineColor = value
                line.setEnabled(randrange(0, 2))
                layout.addWidget(line, row, column + 1, 1, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("LineEdit")
    app.setApplicationName("LineEdit")
    w = Window()
    w.show()
    sys.exit(app.exec_())
