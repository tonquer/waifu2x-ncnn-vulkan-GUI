from PySide6 import QtWidgets
from PySide6.QtCore import QSettings, Qt, QSize, QLocale, QTranslator
from PySide6.QtWidgets import QFileDialog

from conf import config
from src.qt.com.qtbubblelabel import QtBubbleLabel
from src.util import Log
from ui.setting import Ui_Setting


class QtSetting(QtWidgets.QDialog, Ui_Setting):
    def __init__(self, owner):
        super(self.__class__, self).__init__()
        Ui_Setting.__init__(self)
        self.setupUi(self)
        self.settings = QSettings('config.ini', QSettings.IniFormat)
        # self.setWindowModality(Qt.ApplicationModal)
        self.mainSize = QSize(1500, 1100)
        self.bookSize = QSize(900, 1020)
        self.readSize = QSize(1120, 1020)
        self.userId = ""
        self.passwd = ""
        self.gpuInfos = []
        self.translate = QTranslator()

    def show(self):
        self.LoadSetting()
        super(self.__class__, self).show()

    def exec(self):
        self.LoadSetting()
        super(self.__class__, self).exec()

    def GetSettingV(self, key, defV=None):
        v = self.settings.value(key)
        try:
            if v:
                if isinstance(defV, int):
                    if v == "true" or v == "True":
                        return 1
                    elif v == "false" or v == "False":
                        return 0
                    return int(v)
                elif isinstance(defV, float):
                    return float(v)
                else:
                    return v
            return defV
        except Exception as es:
            Log.Error(es)
        return v

    def LoadSetting(self):
        x = self.settings.value("MainSize_x")
        y = self.settings.value("MainSize_y")
        if x and y:
            self.mainSize = QSize(int(x), int(y))

        v = self.settings.value("Waifu2x/Encode")
        if v:
            config.Encode = int(v)

        # v = self.settings.value("Waifu2x/LogIndex")
        # if v:
        #     config.LogIndex = int(v)
        # self.logBox.setCurrentIndex(config.LogIndex)
        Log.UpdateLoggingLevel()
        v = self.settings.value("Waifu2x/Open")

        config.SelectEncodeGpu = self.GetSettingV("Waifu2x/SelectEncodeGpu", "")
        config.UseCpuNum = self.GetSettingV("Waifu2x/UseCpuNum", 0)
        config.Language = self.GetSettingV("Waifu2x/Language", 0)
        self.encodeSelect.setCurrentIndex(0)
        self.languageSelect.setCurrentIndex(config.Language)
        for index in range(self.encodeSelect.count()):
            if config.SelectEncodeGpu == self.encodeSelect.itemText(index):
                self.encodeSelect.setCurrentIndex(index)
        return

    def ExitSaveSetting(self, mainQsize):
        self.settings.setValue("MainSize_x", mainQsize.width())
        self.settings.setValue("MainSize_y", mainQsize.height())

    def SaveSetting(self):
        config.Encode = self.encodeSelect.currentIndex()
        config.UseCpuNum = int(self.threadSelect.currentIndex())
        # config.LogIndex = int(self.logBox.currentIndex())
        config.Language = int(self.languageSelect.currentIndex())
        config.SelectEncodeGpu = self.encodeSelect.currentText()

        self.settings.setValue("Waifu2x/Encode", config.Encode)
        # self.settings.setValue("Waifu2x/Thread", config.Waifu2xThread)
        # self.settings.setValue("Waifu2x/Scale", config.Scale)
        # self.settings.setValue("Waifu2x/Model", config.Model)
        self.settings.setValue("Waifu2x/SelectEncodeGpu", config.SelectEncodeGpu)
        self.settings.setValue("Waifu2x/UseCpuNum", config.UseCpuNum)
        # self.settings.setValue("Waifu2x/LogIndex", config.LogIndex)
        self.settings.setValue("Waifu2x/Language", config.Language)
        Log.UpdateLoggingLevel()
        # QtWidgets.QMessageBox.information(self, '保存成功', "成功", QtWidgets.QMessageBox.Yes)
        QtBubbleLabel.ShowMsgEx(self, "Save Success")
        self.close()

    def SetGpuInfos(self, gpuInfo, cpuNum):
        self.gpuInfos = gpuInfo
        config.EncodeGpu = config.SelectEncodeGpu

        if not self.gpuInfos:
            config.EncodeGpu = "CPU"
            config.Encode = -1
            self.encodeSelect.addItem(config.EncodeGpu)
            self.encodeSelect.setCurrentIndex(0)
            return

        if not config.EncodeGpu or (config.EncodeGpu != "CPU" and config.EncodeGpu not in self.gpuInfos):
            config.EncodeGpu = self.gpuInfos[0]
            config.Encode = 0

        index = 0
        for info in self.gpuInfos:
            self.encodeSelect.addItem(info)
            if info == config.EncodeGpu:
                self.encodeSelect.setCurrentIndex(index)
                config.Encode = index
            index += 1

        self.encodeSelect.addItem("CPU")
        if config.EncodeGpu == "CPU":
            config.Encode = -1
            self.encodeSelect.setCurrentIndex(index)

        if config.UseCpuNum > cpuNum:
            config.UseCpuNum = cpuNum
        for i in range(cpuNum):
            self.threadSelect.addItem(str(i + 1))
        self.threadSelect.setCurrentIndex(config.UseCpuNum)
        Log.Info("waifu2x GPU: " + str(self.gpuInfos) + ",select: " + str(config.EncodeGpu) + ",use cpu num: " + str(config.UseCpuNum))
        return

    def GetGpuName(self):
        return config.EncodeGpu
        # index = config.Encode
        # if index >= len(self.gpuInfos) or index < 0:
        #     return "GPU"
        # return self.gpuInfos[index]

    def SetLanguage(self, app, owner):
        language = config.Language

        # Auto
        if language == 0:
            locale = QLocale.system().name()
            Log.Info("Init translate {}".format(locale))
            if locale[:3].lower() == "zh_":
                if locale.lower() == "zh_cn":
                    language = 1
                else:
                    language = 2
            else:
                language = 3

        if language == 1:
            app.removeTranslator(self.translate)
        elif language == 2:
            self.translate.load(":/tr_hk.qm")
            app.installTranslator(self.translate)
        else:
            self.translate.load(":/tr_en.qm")
            app.installTranslator(self.translate)
        owner.RetranslateUi()