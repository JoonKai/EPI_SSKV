# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mdi_pltrend_widgetraVDKx.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QScrollArea,
    QSizePolicy, QSplitter, QVBoxLayout, QWidget)

class Ui_PLTrend(object):
    def setupUi(self, PLTrend):
        if not PLTrend.objectName():
            PLTrend.setObjectName(u"PLTrend")
        PLTrend.resize(683, 530)
        self.gridLayout = QGridLayout(PLTrend)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(PLTrend)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.splitter.addWidget(self.frame)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.frame_2)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.chart_widget = QWidget(self.splitter_2)
        self.chart_widget.setObjectName(u"chart_widget")
        self.splitter_2.addWidget(self.chart_widget)
        self.scrollArea = QScrollArea(self.splitter_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 54, 286))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter_2.addWidget(self.scrollArea)

        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.frame_2)
        self.frame_3 = QFrame(self.splitter)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.splitter.addWidget(self.frame_3)

        self.verticalLayout.addWidget(self.splitter)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(PLTrend)

        QMetaObject.connectSlotsByName(PLTrend)
    # setupUi

    def retranslateUi(self, PLTrend):
        PLTrend.setWindowTitle(QCoreApplication.translate("PLTrend", u"Form", None))
    # retranslateUi

