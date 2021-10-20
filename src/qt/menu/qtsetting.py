from PySide6 import QtWidgets
from PySide6.QtCore import QSettings, Qt, QSize
from PySide6.QtWidgets import QFileDialog

from conf import config
from src.qt.com.qtbubblelabel import QtBubbleLabel
from src.util import Log
from ui.setting import Ui_Setting


class QtSetting(QtWidgets.QWidget, Ui_Setting):
    def __init__(self, owner):
        super(self.__class__, self).__init__()
        Ui_Setting.__init__(self)
        self.setupUi(self)
        self.settings = QSettings('config.ini', QSettings.IniFormat)
        self.setWindowModality(Qt.ApplicationModal)
        self.mainSize = QSize(1500, 1100)
        self.bookSize = QSize(900, 1020)
        self.readSize = QSize(1120, 1020)
        self.userId = ""
        self.passwd = ""
        self.gpuInfos = []

    def show(self):
        self.LoadSetting()
        super(self.__class__, self).show()

    def LoadSetting(self):
        x = self.settings.value("MainSize_x")
        y = self.settings.value("MainSize_y")
        if x and y:
            self.mainSize = QSize(int(x), int(y))

        v = self.settings.value("Waifu2x/Encode")
        if v:
            config.Encode = int(v)

        v = self.settings.value("Waifu2x/LogIndex")
        if v:
            config.LogIndex = int(v)
        self.logBox.setCurrentIndex(config.LogIndex)
        Log.UpdateLoggingLevel()
        v = self.settings.value("Waifu2x/Open")
        return

    def ExitSaveSetting(self, mainQsize):
        self.settings.setValue("MainSize_x", mainQsize.width())
        self.settings.setValue("MainSize_y", mainQsize.height())

    def SaveSetting(self):
        config.Encode = self.encodeSelect.currentIndex()
        config.Waifu2xThread = int(self.threadSelect.currentIndex()) + 1
        config.LogIndex = int(self.logBox.currentIndex())

        self.settings.setValue("Waifu2x/Encode", config.Encode)
        # self.settings.setValue("Waifu2x/Thread", config.Waifu2xThread)
        # self.settings.setValue("Waifu2x/Scale", config.Scale)
        # self.settings.setValue("Waifu2x/Model", config.Model)
        self.settings.setValue("Waifu2x/LogIndex", config.LogIndex)
        Log.UpdateLoggingLevel()
        # QtWidgets.QMessageBox.information(self, '保存成功', "成功", QtWidgets.QMessageBox.Yes)
        QtBubbleLabel.ShowMsgEx(self, "保存成功")

    def SetGpuInfos(self, gpuInfo):
        self.gpuInfos = gpuInfo
        if config.Encode >= len(self.gpuInfos):
            config.Encode = 0

        if not self.gpuInfos:
            self.encodeSelect.addItem("CPU")
            self.encodeSelect.setCurrentIndex(0)
            return
        for info in self.gpuInfos:
            self.encodeSelect.addItem(info)
        self.encodeSelect.setCurrentIndex(config.Encode)
        Log.Info("waifu2x GPU: " + str(self.gpuInfos))
        return

    def GetGpuName(self):
        index = config.Encode
        if index >= len(self.gpuInfos) or index < 0:
            return "GPU"
        return self.gpuInfos[index]
