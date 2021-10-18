# -*- coding: utf-8 -*-
"""第一个程序"""
import sys

from PySide6.QtGui import QGuiApplication, Qt

from conf import config
try:
    import waifu2x_vulkan
    config.CanWaifu2x = True
except Exception as es:
    config.CanWaifu2x = False
    if hasattr(es, "msg"):
        config.ErrorMsg = es.msg

from PySide6 import QtWidgets  # 导入PySide6部件
from src.qt.qtmain import QtMainWindow
from src.util import Log

if __name__ == "__main__":
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Floor)
    # QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    Log.Init()
    app = QtWidgets.QApplication(sys.argv)  # 建立application对象
    # app.addLibraryPath("./resources")
    main = QtMainWindow()

    main.show()  # 显示窗体
    main.Init()
    sts = app.exec_()
    if config.CanWaifu2x:
        waifu2x_vulkan.stop()
    sys.exit(sts)  # 运行程序
