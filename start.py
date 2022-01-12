# -*- coding: utf-8 -*-
"""第一个程序"""
import sys

from PySide6.QtGui import QGuiApplication, Qt

from conf import config
try:
    from waifu2x_vulkan import waifu2x_vulkan
    config.CanWaifu2x = True
except Exception as es:
    config.CanWaifu2x = False
    if hasattr(es, "msg"):
        config.ErrorMsg = es.msg

from PySide6 import QtWidgets  # 导入PySide6部件
from src.qt.qtmain import QtMainWindow
from src.util import Log
import images_rc


if __name__ == "__main__":
    # QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Floor)
    # QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    Log.Init()
    app = QtWidgets.QApplication(sys.argv)  # 建立application对象
    # app.addLibraryPath("./resources")
    main = QtMainWindow()

    main.Init(app)
    main.show()  # 显示窗体
    sts = app.exec()
    if config.CanWaifu2x:
        waifu2x_vulkan.stop()
    sys.exit(sts)  # 运行程序
