from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QToolButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from mdi.ui_mdi_fmmacro_widget import Ui_FMMacro


class FMMacroController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FMMacro()
        self.ui.setupUi(self)
        self.resize(800, 600)
        self.setWindowTitle("팩토리 모델러 매크로")