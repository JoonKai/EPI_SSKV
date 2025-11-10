from PySide6.QtWidgets import QWidget
from mdi.ui_mdi_pltrend_widget import PLTrend


class PLTrendController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = PLTrend()
        self.ui.setupUi(self)
        self.resize(800, 600)
        self.setWindowTitle("측정 설비비")

    