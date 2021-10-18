import os
import time

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt, QRectF, QPointF, QSizeF, QEvent
from PySide6.QtGui import QColor, QPainter, QPixmap, QDoubleValidator, \
    QIntValidator
from PySide6.QtWidgets import QFrame, QGraphicsPixmapItem, QGraphicsScene, QApplication, QFileDialog

from conf import config
from src.qt.com.qtbubblelabel import QtBubbleLabel
from src.qt.util.qttask import QtTask
from src.util import Singleton, ToolUtil, Log
from ui.img import Ui_Img

class QtImg(QtWidgets.QWidget, Ui_Img):
    def __init__(self):
        super(self.__class__, self).__init__()
        Ui_Img.__init__(self)
        self.setupUi(self)
        self.bookId = ""
        self.epsId = 0
        self.curIndex = 0
        self.setWindowTitle("图片查看")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(800, 900)
        self.checkBox.setChecked(True)
        self.index = 0
        self.comboBox.setCurrentIndex(self.index)
        validator = QIntValidator(0, 9999999)
        self.heighEdit.setValidator(validator)
        self.widthEdit.setValidator(validator)
        exp = QDoubleValidator(0.1, 64, 1)
        exp.setNotation(exp.StandardNotation)
        self.scaleEdit.setValidator(exp)
        # self.setWindowFlags(Qt.FramelessWindowHint)

        self.graphicsView.setFrameStyle(QFrame.NoFrame)
        self.graphicsView.setObjectName("graphicsView")

        self.graphicsView.setBackgroundBrush(QColor(Qt.white))
        self.graphicsView.setCursor(Qt.OpenHandCursor)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setRenderHints(QPainter.Antialiasing |
                                         QPainter.SmoothPixmapTransform)
        self.graphicsView.setCacheMode(self.graphicsView.CacheBackground)
        self.graphicsView.setViewportUpdateMode(self.graphicsView.SmartViewportUpdate)

        self.graphicsItem = QGraphicsPixmapItem()
        self.graphicsItem.setFlags(QGraphicsPixmapItem.ItemIsFocusable |
                                   QGraphicsPixmapItem.ItemIsMovable)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.CopyPicture)

        self.graphicsScene = QGraphicsScene(self)  # 场景
        self.graphicsView.setScene(self.graphicsScene)
        self.graphicsScene.addItem(self.graphicsItem)
        self.graphicsView.setMinimumSize(10, 10)
        self.pixMap = QPixmap("加载中")
        self.graphicsItem.setPixmap(self.pixMap)
        # self.radioButton.setChecked(True)
        self.isStripModel = False

        # self.radioButton.installEventFilter(self)
        # self.radioButton_2.installEventFilter(self)
        self.graphicsView.installEventFilter(self)
        self.graphicsView.setWindowFlag(Qt.FramelessWindowHint)
        # tta有BUG，暂时屏蔽 TODO
        self.ttaModel.setEnabled(False)
        self.data = b""
        self.waifu2xData = b""

        self._delta = 0.1
        self.scaleCnt = 0

        self.backStatus = ""
        self.format = ""

    def ShowImg(self, data):
        if data:
            self.data = data
            self.waifu2xData = b""
            QtTask().CancelConver("QtImg")
            self._ShowImg(data)
        elif self.data:
            self._ShowImg(self.data)
        else:
            pass

    def _ShowImg(self, data):
        self.scaleCnt = 0
        self.pixMap = QPixmap()
        self.pixMap.loadFromData(data)
        self.show()
        self.graphicsItem.setPixmap(self.pixMap)
        self.graphicsView.setSceneRect(QRectF(QPointF(0, 0), QPointF(self.pixMap.width(), self.pixMap.height())))
        size = ToolUtil.GetDownloadSize(len(data))
        self.sizeLabel.setText(size)
        weight, height = ToolUtil.GetPictureSize(data)
        self.resolutionLabel.setText(str(weight) + "x" + str(height))
        self.ScalePicture()

    def ScalePicture(self):
        rect = QRectF(self.graphicsItem.pos(), QSizeF(
            self.pixMap.size()))
        unity = self.graphicsView.transform().mapRect(QRectF(0, 0, 1, 1))
        width = unity.width()
        height = unity.height()
        if width <= 0 or height <= 0:
            return
        self.graphicsView.scale(1 / width, 1 / height)
        viewRect = self.graphicsView.viewport().rect()
        sceneRect = self.graphicsView.transform().mapRect(rect)
        if sceneRect.width() <= 0 or sceneRect.height() <= 0:
            return
        x_ratio = viewRect.width() / sceneRect.width()
        y_ratio = viewRect.height() / sceneRect.height()
        x_ratio = y_ratio = min(x_ratio, y_ratio)

        self.graphicsView.scale(x_ratio, y_ratio)
        # if self.readImg.isStripModel:
        #     height2 = self.pixMap.size().height() / 2
        #     height3 = self.graphicsView.size().height()/2
        #     height3 = height3/x_ratio
        #     p = self.graphicsItem.pos()
        #     self.graphicsItem.setPos(p.x(), p.y()+height2-height3)
        self.graphicsView.centerOn(rect.center())

        for _ in range(abs(self.scaleCnt)):
            if self.scaleCnt > 0:
                self.graphicsView.scale(1.1, 1.1)
            else:
                self.graphicsView.scale(1/1.1, 1/1.1)

    def resizeEvent(self, event) -> None:
        super(self.__class__, self).resizeEvent(event)
        self.ScalePicture()

    def eventFilter(self, obj, ev):
        if ev.type() == QEvent.KeyPress:
            return True
        else:
            return super(self.__class__, self).eventFilter(obj, ev)

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoomIn()
        else:
            self.zoomOut()

    def zoomIn(self):
        """放大"""
        self.zoom(1.1)

    def zoomOut(self):
        """缩小"""
        self.zoom(1/1.1)

    def zoom(self, factor):
        """缩放
        :param factor: 缩放的比例因子
        """
        _factor = self.graphicsView.transform().scale(
            factor, factor).mapRect(QRectF(0, 0, 1, 1)).width()
        if _factor < 0.07 or _factor > 100:
            # 防止过大过小
            return
        if factor >= 1:
            self.scaleCnt += 1
        else:
            self.scaleCnt -= 1
        self.graphicsView.scale(factor, factor)

    def CopyPicture(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(self.pixMap)
        QtBubbleLabel.ShowMsgEx(self, "复制成功")
        return

    def ReduceScalePic(self):
        self.zoom(1/1.1)
        return

    def AddScalePic(self):
        self.zoom(1.1)
        return

    def OpenPicture(self):
        try:
            filename = QFileDialog.getOpenFileName(self, "Open Image", ".", "Image Files(*.jpg *.png)")
            if filename and len(filename) >= 1:
                name = filename[0]
                if os.path.isfile(name):
                    f = open(name, "rb")
                    data = f.read()
                    f.close()
                    self.ShowImg(data)
        except Exception as ex:
            Log.Error(ex)
        return

    def StartWaifu2xPng(self):
        if self.StartWaifu2x("png"):
            self.format = "png"
            self.changeJpg.setEnabled(False)
            self.changePng.setEnabled(False)
        return

    def StartWaifu2xJPG(self):
        if self.StartWaifu2x("jpg"):
            self.format = "jpg"
            self.changeJpg.setEnabled(False)
            self.changePng.setEnabled(False)
        return

    def StartWaifu2x(self, format):
        if not self.data:
            return False
        if not config.CanWaifu2x:
            return False
        import waifu2x_vulkan
        self.SetStatus(False)
        self.index = self.comboBox.currentIndex()
        index = self.comboBox.currentIndex()
        noise = int(self.noiseCombox.currentText())
        if index == 0:
            modelName = "CUNET"
        elif index == 1:
            modelName = "PHOTO"
        elif index == 2:
            modelName = "ANIME_STYLE_ART_RGB"
        else:
            return False
        if noise == -1:
            noiseName = "NO_NOISE"
        else:
            noiseName = "NOISE"+str(noise)
        if modelName == "CUNET" and self.scaleRadio.isChecked() and round(float(self.scaleEdit.text()), 1) <= 1:
            modelInsence = "MODEL_{}_NO_SCALE_{}".format(modelName, noiseName)
        else:
            modelInsence = "MODEL_{}_{}".format(modelName, noiseName)
        if self.ttaModel.isChecked():
            modelInsence += "_TTA"

        model = {
            "model":  getattr(waifu2x_vulkan, modelInsence),
        }
        if self.scaleRadio.isChecked():
            model['scale'] = round(float(self.scaleEdit.text()), 1)
        else:
            model['width'] = int(self.widthEdit.text())
            model['high'] = int(self.heighEdit.text())
        model['format'] = format
        self.backStatus = self.GetStatus()
        QtTask().AddConvertTask(self.data, model, self.AddConvertBack,
                                cleanFlag="QtImg")
        self.changeLabel.setText("正在转换")
        return True

    def AddConvertBack(self, data, waifuId, backParam, tick):
        if data:
            self.waifu2xData = data
            if self.checkBox.isChecked():
                self._ShowImg(data)
            self.changeLabel.setText("已转换")
            self.tickLabel.setText(str(round(tick, 3)) + "s")

        else:
            self.changeLabel.setText("失败")
        self.SetStatus(True)
        return

    def CheckHideButton(self):
        if self.format == "":
            self.changePng.setEnabled(True)
            self.changeJpg.setEnabled(True)
        elif self.format == "png":
            self.changePng.setEnabled(False)
            self.changeJpg.setEnabled(True)
        else:
            self.changePng.setEnabled(True)
            self.changeJpg.setEnabled(False)

    def SavePicture(self):
        data = self.waifu2xData if self.waifu2xData else self.data
        if not data:
            return
        try:
            today = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            picFormat = self.format if self.format else "jpg"
            filepath = QFileDialog.getSaveFileName(self, "保存", "{}.{}".format(today, picFormat))
            if filepath and len(filepath) >= 1 and filepath[0]:
                name = filepath[0]
                f = open(name, "wb")
                f.write(data)
                f.close()
        except Exception as es:
            Log.Error(es)
        return

    def SwithPicture(self):
        if self.checkBox.isChecked() and self.waifu2xData:
            self._ShowImg(self.waifu2xData)
        else:
            self._ShowImg(self.data)
        return

    def ChangeModel(self, index):
        # self.index = self.comboBox.currentIndex()
        self.CheckScaleRadio()
        return

    def GetStatus(self):
        data = str(self.noiseCombox.currentText()) + \
            str(self.buttonGroup_2.checkedId()) + \
            str(self.scaleEdit.text()) + \
            str(self.heighEdit.text()) + \
            str(int(self.ttaModel.isChecked())) + \
            str(self.widthEdit.text()) + \
            str(self.comboBox.currentIndex())
        return data

    def SetStatus(self, status):
        self.scaleRadio.setEnabled(status)
        self.heighRadio.setEnabled(status)
        self.scaleEdit.setEnabled(status)
        self.widthEdit.setEnabled(status)
        self.heighEdit.setEnabled(status)
        self.noiseCombox.setEnabled(status)
        self.comboBox.setEnabled(status)
        # self.radioButton_4.setEnabled(status)
        # self.radioButton_5.setEnabled(status)
        # self.radioButton_6.setEnabled(status)
        # self.radioButton_7.setEnabled(status)
        # self.radioButton_8.setEnabled(status)
        # self.ttaModel.setEnabled(status)
        self.CheckScaleRadio()

    def SetEnable(self):
        self.SetStatus(True)

    def SetDisEnable(self):
        self.SetStatus(False)

    def CheckScaleRadio(self):
        if self.scaleRadio.isChecked() and self.scaleRadio.isEnabled():
            self.scaleEdit.setEnabled(True)
            self.widthEdit.setEnabled(False)
            self.heighEdit.setEnabled(False)
        elif self.heighRadio.isChecked() and self.heighRadio.isEnabled():
            self.scaleEdit.setEnabled(False)
            self.widthEdit.setEnabled(True)
            self.heighEdit.setEnabled(True)
        data = self.GetStatus()
        if self.backStatus != data:
            self.changePng.setEnabled(True)
            self.changeJpg.setEnabled(True)
        else:
            self.CheckHideButton()
