from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout, QLabel
from ui_settings_dialog import settings


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = settings()  # Qt Designer에서 만든 UI 클래스
        self.ui.setupUi(self)  # UI를 현재 다이얼로그에 적용
        self.setWindowTitle("설정 다이얼로그")
        self.resize(400, 300)