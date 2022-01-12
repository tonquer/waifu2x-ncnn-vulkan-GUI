

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
        self.setWindowTitle("Waifu2x-Gui")
        self.msgForm = QtBubbleLabel(self)
        self.settingForm = QtSetting(self)
        self.settingForm.hide()
        self.settingForm.LoadSetting()

        self.aboutForm = QtAbout(self)
        self.img = QtImg()
        self.stackedWidget.addWidget(self.img)
        # self.resize(1000, 1000)
        self.menuabout.triggered.connect(self.OpenAbout)
        desktop = QGuiApplication.primaryScreen().geometry()
        # self.resize(desktop.width()//4*3, desktop.height()//4*3)
        # self.move(desktop.width()//8*1, desktop.height()//8*1)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)
        self.settingForm.ExitSaveSetting(self.size())

    def RetranslateUi(self):
        self.settingForm.retranslateUi(self.settingForm)
        self.img.retranslateUi(self.img)
        self.aboutForm.retranslateUi(self.aboutForm)
        self.retranslateUi(self)

    def Init(self, app):
        self.settingForm.SetLanguage(app, self)
        if config.CanWaifu2x:
            from waifu2x_vulkan import waifu2x_vulkan
            stat = waifu2x_vulkan.init()
            if stat < 0:
                self.msgForm.ShowError("Waifu2x CPU Model")
            waifu2x_vulkan.setDebug(True)
            
            gpuInfo = waifu2x_vulkan.getGpuInfo()
            cpuNum = waifu2x_vulkan.getCpuCoreNum()
            self.settingForm.SetGpuInfos(gpuInfo, cpuNum)

            self.settingForm.exec()
            self.settingForm.SetLanguage(app, self)
            waifu2x_vulkan.initSet(config.Encode, config.UseCpuNum)

            self.img.gpuName.setText(config.EncodeGpu)
            Log.Info("waifu2x init: " + str(stat) + " encode: " + str(config.Encode) + " version:" + waifu2x_vulkan.getVersion())
            # self.msgForm.ShowMsg("waifu2x初始化成功\n" + waifu2x.getVersion())
        else:
            self.msgForm.ShowError("Waifu2x can not use, " + config.ErrorMsg)
            self.img.checkBox.setEnabled(False)
            self.img.changeJpg.setEnabled(False)
            self.img.changePng.setEnabled(False)
            self.img.comboBox.setEnabled(False)
            self.img.SetStatus(False)
            config.IsOpenWaifu = 0

        return

    def OpenAbout(self, action):
        if action.text() == "about":
            self.aboutForm.show()
        pass