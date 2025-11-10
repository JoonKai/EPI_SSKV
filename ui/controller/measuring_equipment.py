from PySide6.QtWidgets import QWidget
from mdi.ui_mdi_measuring_equipment_widget import Ui_measuring_equipment


class MeasuringEquipmentController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_measuring_equipment()
        self.ui.setupUi(self)
        self.resize(800, 600)
        self.setWindowTitle("측정 설비비")

    