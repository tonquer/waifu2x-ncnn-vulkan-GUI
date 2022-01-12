# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QGridLayout, QLabel, QSizePolicy, QWidget)

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
        self.label_8 = QLabel(Setting)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)

        self.encodeSelect = QComboBox(Setting)
        self.encodeSelect.setObjectName(u"encodeSelect")

        self.gridLayout_3.addWidget(self.encodeSelect, 0, 2, 1, 1)

        self.threadSelect = QComboBox(Setting)
        self.threadSelect.addItem("")
        self.threadSelect.setObjectName(u"threadSelect")

        self.gridLayout_3.addWidget(self.threadSelect, 1, 2, 1, 1)

        self.label_3 = QLabel(Setting)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label = QLabel(Setting)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.languageSelect = QComboBox(Setting)
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.languageSelect.setObjectName(u"languageSelect")

        self.gridLayout_3.addWidget(self.languageSelect, 2, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Setting)
        self.buttonBox.accepted.connect(Setting.SaveSetting)
        self.buttonBox.rejected.connect(Setting.close)

        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"\u8bbe\u7f6e", None))
        self.label_8.setText(QCoreApplication.translate("Setting", u"CPU\u6570\u91cf\uff08CPU\u6a21\u5f0f\u53ef\u7528\uff09", None))
        self.threadSelect.setItemText(0, QCoreApplication.translate("Setting", u"Auto", None))

        self.label_3.setText(QCoreApplication.translate("Setting", u"CPU/GPU", None))
        self.label.setText(QCoreApplication.translate("Setting", u"Language", None))
        self.languageSelect.setItemText(0, QCoreApplication.translate("Setting", u"Auto", None))
        self.languageSelect.setItemText(1, QCoreApplication.translate("Setting", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.languageSelect.setItemText(2, QCoreApplication.translate("Setting", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.languageSelect.setItemText(3, QCoreApplication.translate("Setting", u"English", None))

    # retranslateUi

