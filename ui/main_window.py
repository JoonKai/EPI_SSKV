import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressDialog, QMdiSubWindow
from PySide6.QtCore import Qt
from ui_main_window import Ui_MainWindow
from controller.measuring_equipment import MeasuringEquipmentController
from ui_settings_window import SettingWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.resize(1000, 700)
        self.mn_settings_window.triggered.connect(self.open_settings_window)
        self.mn_measurement_equipment.triggered.connect(self.open_sub_measuring_equipment)


    def open_settings_window(self):
        dlg = SettingWindow(self)
        dlg.exec()

    def open_sub_measuring_equipment(self): 
        for sub in self.mdiArea.subWindowList(): 
            if isinstance(sub.widget(), MeasuringEquipmentController):
                sub.activateWindow() 
                self.mdiArea.setActiveSubWindow(sub) 
                return
        
        sub_widget = MeasuringEquipmentController(self) 
        sub = QMdiSubWindow() 
        sub.setWidget(sub_widget) 
        sub.setWindowTitle("측정 설비")  
        sub.resize(700, 500) 
        sub.setAttribute(Qt.WA_DeleteOnClose, True) 
        self.mdiArea.addSubWindow(sub) 
        sub.show()








app = QApplication(sys.argv)
with open("./styles/darkstyle.qss", "r", encoding="utf-8") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
window.show()
sys.exit(app.exec())