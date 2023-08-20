# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        if not settingsDialog.objectName():
            settingsDialog.setObjectName(u"settingsDialog")
        settingsDialog.resize(571, 231)
        self.buttonBox = QDialogButtonBox(settingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(190, 190, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(settingsDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 91, 31))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.layoutWidget = QWidget(settingsDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 90, 551, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.lServicePath = QLineEdit(self.layoutWidget)
        self.lServicePath.setObjectName(u"lServicePath")
        self.lServicePath.setFont(font1)

        self.horizontalLayout.addWidget(self.lServicePath)


        self.retranslateUi(settingsDialog)
        self.buttonBox.accepted.connect(settingsDialog.accept)
        self.buttonBox.rejected.connect(settingsDialog.reject)

        QMetaObject.connectSlotsByName(settingsDialog)
    # setupUi

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QCoreApplication.translate("settingsDialog", u"Application Settings", None))
        self.label.setText(QCoreApplication.translate("settingsDialog", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("settingsDialog", u"Service Path", None))
    # retranslateUi

