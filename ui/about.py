# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        if not AboutForm.objectName():
            AboutForm.setObjectName(u"AboutForm")
        AboutForm.resize(679, 284)
        self.gridLayout = QGridLayout(AboutForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_4 = QFrame(AboutForm)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 8, 0, 1, 1)

        self.line_3 = QFrame(AboutForm)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 0, 0, 1, 1)

        self.line = QFrame(AboutForm)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)

        self.line_2 = QFrame(AboutForm)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(AboutForm)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 4, 4, 1, 1)

        self.label = QLabel(AboutForm)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(AboutForm)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 4, 1, 1)

        self.label_4 = QLabel(AboutForm)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.line_6 = QFrame(AboutForm)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 3, 1, 1, 1)

        self.label_7 = QLabel(AboutForm)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_6 = QLabel(AboutForm)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 4, 1, 1)

        self.label_5 = QLabel(AboutForm)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.line_5 = QFrame(AboutForm)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 2, 1, 1, 1)

        self.line_7 = QFrame(AboutForm)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 4, 1, 1, 1)

        self.line_9 = QFrame(AboutForm)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_9, 1, 1, 1, 1)

        self.label_3 = QLabel(AboutForm)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 4, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 1)


        self.retranslateUi(AboutForm)

        QMetaObject.connectSlotsByName(AboutForm)
    # setupUi

    def retranslateUi(self, AboutForm):
        AboutForm.setWindowTitle(QCoreApplication.translate("AboutForm", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("AboutForm", u"<a href=\"https://github.com/tonquer/waifu2x-vulkan\"> waifu2x-vulkan</a>", None))
        self.label.setText(QCoreApplication.translate("AboutForm", u"waifu2x-GUI-demo v1.0.1", None))
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("AboutForm", u"\u9879\u76ee\u5f00\u6e90\u5730\u5740\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("AboutForm", u"waifu2x\u5730\u5740", None))
        self.label_6.setText(QCoreApplication.translate("AboutForm", u"1.1.1", None))
        self.label_5.setText(QCoreApplication.translate("AboutForm", u"waifu2x\u7248\u672c\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("AboutForm", u"<a href=\"https://github.com/tonquer/waifu2x-ncnn-vulkan--GUI\"> waifu2x-ncnn-vulkan-GUI</a>", None))
    # retranslateUi

