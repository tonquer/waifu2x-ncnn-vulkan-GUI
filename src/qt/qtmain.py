

from PySide6 import QtWidgets, QtGui  # 导入PySide6部件
from PySide6.QtCore import QTimer, QUrl
from PySide6.QtGui import QIcon, QPixmap, QDesktopServices, QGuiApplication
from PySide6.QtWidgets import QMessageBox

from conf import config
from src.qt.com.qtbubblelabel import QtBubbleLabel
from src.qt.com.qtimg import QtImg
from src.qt.menu.qtabout import QtAbout
from src.qt.menu.qtsetting import QtSetting
from src.util import Log
from ui.main import Ui_MainWindow


class QtMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.userInfo = None
        self.setupUi(self)
        self.setWindowTitle("waifu2x-gui")
        self.msgForm = QtBubbleLabel(self)
        self.settingForm = QtSetting(self)
        self.aboutForm = QtAbout(self)
        self.img = QtImg()
        self.stackedWidget.addWidget(self.img)
        self.resize(1000, 1000)
        self.menusetting.triggered.connect(self.OpenSetting)
        self.menuabout.triggered.connect(self.OpenAbout)
        desktop = QGuiApplication.primaryScreen().geometry()
        self.resize(desktop.width()//4*3, desktop.height()//4*3)
        self.move(desktop.width()//8*1, desktop.height()//8*1)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)
        self.settingForm.ExitSaveSetting(self.size())

    def Init(self):
        if config.CanWaifu2x:
            import waifu2x_vulkan
            stat = waifu2x_vulkan.init()
            if stat < 0:
                self.msgForm.ShowError("waifu2x初始化错误")
            else:
                waifu2x_vulkan.setDebug(True)
                gpuInfo = waifu2x_vulkan.getGpuInfo()
                if gpuInfo:
                    self.settingForm.SetGpuInfos(gpuInfo)
                if gpuInfo and config.Encode < 0:
                    config.Encode = 0

                waifu2x_vulkan.initSet(config.Encode, config.Waifu2xThread)
                Log.Info("waifu2x初始化: " + str(stat) + " encode: " + str(config.Encode) + " version:" + waifu2x_vulkan.getVersion())
                # self.msgForm.ShowMsg("waifu2x初始化成功\n" + waifu2x.getVersion())
        else:
            self.msgForm.ShowError("waifu2x无法启用, "+config.ErrorMsg)
            self.img.checkBox.setEnabled(False)
            self.img.changeJpg.setEnabled(False)
            self.img.changePng.setEnabled(False)
            self.img.comboBox.setEnabled(False)
            self.img.SetStatus(False)
            config.IsOpenWaifu = 0

        return

    def OpenSetting(self):
        self.settingForm.show()
        pass

    def OpenAbout(self, action):
        if action.text() == "about":
            self.aboutForm.show()
        pass