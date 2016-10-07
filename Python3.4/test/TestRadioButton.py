#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年10月6日
@author: Irony."[讽刺]
@site: alyl.vip, orzorz.vip, irony.coding.me , irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.TestRadioButton
@description: 
'''


from random import randrange
import os
import sys

sys.path.insert(0, os.path.dirname(os.getcwd()))
print(sys.path)

from PyQt5.QtWidgets import QWidget, QApplication, QLabel,\
    QGridLayout, QScrollArea

from QMaterial.Utils import Colors
from QMaterial.Widget.RadioButton import RadioButton


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__(None)
        layout = QGridLayout(self)
        colors = Colors.alls()
        for row, key in enumerate(colors):
            layout.addWidget(QLabel(key, self), row, 0, 1, 1)
            for column, value in enumerate(colors.get(key)):
                b = RadioButton(value._name, self)
                b.borderColor = value
                b.backgroundColor = value
                b.radioSize = randrange(0, 64)
                layout.addWidget(b, row, column + 1, 1, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("RadioButton")
    app.setApplicationName("RadioButton")
    window = QScrollArea()
    window.setWidgetResizable(True)
    window.setWidget(Window())
    window.show()
    sys.exit(app.exec_())
