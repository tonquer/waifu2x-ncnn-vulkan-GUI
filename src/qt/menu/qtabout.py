import weakref

from PySide6 import QtWidgets
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

from conf import config
from ui.about import Ui_AboutForm


class QtAbout(QtWidgets.QWidget, Ui_AboutForm):
    def __init__(self, owner):
        super(self.__class__, self).__init__()
        Ui_AboutForm.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("about")
        self.owner = weakref.ref(owner)
        self.label_3.linkActivated.connect(self.OpenUrl)
        self.label_8.linkActivated.connect(self.OpenUrl2)

    def OpenUrl(self):
        QDesktopServices.openUrl(QUrl("https://github.com/tonquer/waifu2x-ncnn-vulkan-GUI"))

    def OpenUrl2(self):
        QDesktopServices.openUrl(QUrl("https://github.com/tonquer/waifu2x-vulkan"))