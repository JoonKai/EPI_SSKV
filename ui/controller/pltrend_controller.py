from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QToolButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from mdi.ui_mdi_pltrend_widget import Ui_PLTrend


class PLTrendController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PLTrend()
        self.ui.setupUi(self)
        self.resize(800, 600)
        self.setWindowTitle("측정 설비")

    