# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(482, 231)
        self.gridLayout_2 = QGridLayout(Setting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Setting)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(Setting)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_8 = QLabel(Setting)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.logBox = QComboBox(Setting)
        self.logBox.addItem("")
        self.logBox.addItem("")
        self.logBox.addItem("")
        self.logBox.setObjectName(u"logBox")

        self.gridLayout_3.addWidget(self.logBox, 0, 2, 1, 1)

        self.encodeSelect = QComboBox(Setting)
        self.encodeSelect.setObjectName(u"encodeSelect")

        self.gridLayout_3.addWidget(self.encodeSelect, 1, 2, 1, 1)

        self.threadSelect = QComboBox(Setting)
        self.threadSelect.addItem("")
        self.threadSelect.setObjectName(u"threadSelect")

        self.gridLayout_3.addWidget(self.threadSelect, 2, 2, 1, 1)

        self.label_10 = QLabel(Setting)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Setting)
        self.buttonBox.accepted.connect(Setting.SaveSetting)
        self.buttonBox.rejected.connect(Setting.close)

        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Setting", u"\u89e3\u7801\u5668\uff08\u9700\u91cd\u542f\uff09", None))
        self.label_8.setText(QCoreApplication.translate("Setting", u"\u7ebf\u7a0b\u6570", None))
        self.logBox.setItemText(0, QCoreApplication.translate("Setting", u"WARN", None))
        self.logBox.setItemText(1, QCoreApplication.translate("Setting", u"INFO", None))
        self.logBox.setItemText(2, QCoreApplication.translate("Setting", u"DEBUG", None))

        self.threadSelect.setItemText(0, QCoreApplication.translate("Setting", u"2", None))

        self.label_10.setText(QCoreApplication.translate("Setting", u"\u65e5\u5fd7\u7b49\u7ea7", None))
    # retranslateUi

