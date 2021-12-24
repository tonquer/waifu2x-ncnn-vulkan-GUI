import hashlib
import os
import threading
import time
import weakref
from queue import Queue

from PySide6.QtCore import Signal, QObject

from conf import config
from src.util import Singleton, Log
from src.util.status import Status
from src.util.tool import time_me, CTime, ToolUtil


class QtTaskQObject(QObject):
    convertBack = Signal(int)

    def __init__(self):
        super(self.__class__, self).__init__()


class QtDownloadTask(object):
    def __init__(self, downloadId=0):
        self.downloadId = downloadId
        self.downloadCompleteBack = None
        self.fileSize = 0
        self.isSaveData = True
        self.saveData = b""
        self.url = ""
        self.path = ""
        self.originalName = ""
        self.backParam = None
        self.cleanFlag = ""
        self.tick = 0

        self.imgData = b""
        self.model = {
            "model": 1,
            "scale": 2,
            "toH": 100,
            "toW": 100,
        }


class QtTask(Singleton, threading.Thread):

    def __init__(self):
        Singleton.__init__(self)
        threading.Thread.__init__(self)
        self._inQueue = Queue()
        self._owner = None
        self.taskObj = QtTaskQObject()
        self.taskObj.convertBack.connect(self.HandlerConvertTask)

        self.convertThread = threading.Thread(target=self.RunLoad)
        self.convertThread.setDaemon(True)
        self.convertThread.start()

        self.convertThread2 = threading.Thread(target=self.RunLoad2)
        self.convertThread2.setDaemon(True)
        self.convertThread2.start()

        self.downloadTask = {}   # id: task
        self.convertLoad = {}  # id: task
        self.convertId = 1000000

        self.taskId = 0
        self.tasks = {}  # id: task

        self.flagToIds = {}  #
        self.convertFlag = {}

    @property
    def convertBack(self):
        return self.taskObj.convertBack

    @property
    def taskBack(self):
        return self.taskObj.taskBack

    @property
    def downloadBack(self):
        return self.taskObj.downloadBack

    @property
    def owner(self):
        from src.qt.qtmain import QtMainWindow
        assert isinstance(self._owner(), QtMainWindow)
        return self._owner()

    def SetOwner(self, owner):
        self._owner = weakref.ref(owner)

    def AddConvertTask(self, imgData, model, completeCallBack, backParam=None, cleanFlag=""):
        info = QtDownloadTask()
        info.downloadCompleteBack = completeCallBack
        info.backParam = backParam
        self.taskId += 1
        self.convertLoad[self.taskId] = info
        info.downloadId = self.taskId
        info.imgData = imgData
        info.model = model
        if cleanFlag:
            info.cleanFlag = cleanFlag
            taskIds = self.convertFlag.setdefault(cleanFlag, set())
            taskIds.add(self.taskId)
        self._inQueue.put(self.taskId)
        return self.taskId

    def HandlerConvertTask(self, taskId):
        if taskId not in self.convertLoad:
            return
        t1 = CTime()
        info = self.convertLoad[taskId]
        assert isinstance(info, QtDownloadTask)

        if info.cleanFlag:
            taskIds = self.convertFlag.get(info.cleanFlag, set())
            taskIds.discard(info.downloadId)
        info.downloadCompleteBack(info.saveData, taskId, info.backParam, info.tick)
        if info.cleanFlag:
            taskIds = self.convertFlag.get(info.cleanFlag, set())
            taskIds.discard(info.downloadId)
        del self.convertLoad[taskId]
        t1.Refresh("RunLoad")

    def LoadData(self):
        if not config.CanWaifu2x:
            return None
        from waifu2x_vulkan import waifu2x_vulkan
        return waifu2x_vulkan.load(0)

    def RunLoad(self):
        while True:
            try:
                taskId = self._inQueue.get(True)
                if taskId not in self.convertLoad:
                    continue
                task = self.convertLoad.get(taskId)
                if config.CanWaifu2x:
                    from waifu2x_vulkan import waifu2x_vulkan
                    if config.EncodeGpu != "CPU":
                        tileSize = 0
                    else:
                        tileSize = 200
                    scale = task.model.get("scale", 0)
                    if scale <= 0:
                        sts = waifu2x_vulkan.add(task.imgData, task.model.get('model', 0), task.downloadId, task.model.get("width", 0),
                                          task.model.get("high", 0), task.model.get("format", "jpg"), tileSize)
                    else:
                        sts = waifu2x_vulkan.add(task.imgData, task.model.get('model', 0), task.downloadId, scale, task.model.get("format", "jpg"), tileSize)

                    # Log.Warn("add convert info, taskId: {}, model:{}, sts:{}".format(str(task.taskId), task.model,
                    #                                                                          str(sts)))
                else:
                    sts = -1
                if sts <= 0:
                    self.convertBack.emit(taskId)
                    continue
            except Exception as es:
                continue

    def RunLoad2(self):
        while True:
            info = self.LoadData()
            if not info:
                continue
            t1 = CTime()
            data, convertId, taskId, tick = info
            if taskId not in self.convertLoad:
                continue
            if not data:
                lenData = 0
            else:
                lenData = len(data)

            Log.Warn("convert suc, taskId: {}, dataLen:{}, sts:{} tick:{}".format(str(taskId), lenData,
                                                                                          str(convertId),
                                                                                          str(tick)))
            info = self.convertLoad[taskId]
            assert isinstance(info, QtDownloadTask)
            info.saveData = data
            info.tick = tick
            self.convertBack.emit(taskId)
            t1.Refresh("RunLoad")

    def CancelConver(self, cleanFlag):
        taskIds = self.convertFlag.get(cleanFlag, set())
        if not taskIds:
            return
        for taskId in taskIds:
            if taskId in self.convertLoad:
                del self.convertLoad[taskId]
        Log.Info("cancel convert taskId, {}".format(taskIds))
        self.convertFlag.pop(cleanFlag)
        if config.CanWaifu2x:
            from waifu2x_vulkan import waifu2x_vulkan
            waifu2x_vulkan.remove(list(taskIds))
