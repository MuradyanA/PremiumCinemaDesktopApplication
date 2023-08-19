# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateUserDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGroupBox, QLabel, QRadioButton,
    QSizePolicy, QWidget)

class Ui_UpdateUserDialog(object):
    def setupUi(self, UpdateUserDialog):
        if not UpdateUserDialog.objectName():
            UpdateUserDialog.setObjectName(u"UpdateUserDialog")
        UpdateUserDialog.resize(395, 300)
        self.buttonBox = QDialogButtonBox(UpdateUserDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.lbTitle = QLabel(UpdateUserDialog)
        self.lbTitle.setObjectName(u"lbTitle")
        self.lbTitle.setGeometry(QRect(20, 20, 141, 31))
        font = QFont()
        font.setPointSize(18)
        self.lbTitle.setFont(font)
        self.chStatus = QCheckBox(UpdateUserDialog)
        self.chStatus.setObjectName(u"chStatus")
        self.chStatus.setGeometry(QRect(30, 90, 91, 20))
        font1 = QFont()
        font1.setPointSize(12)
        self.chStatus.setFont(font1)
        self.groupBox = QGroupBox(UpdateUserDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 130, 121, 101))
        self.groupBox.setFont(font1)
        self.rController = QRadioButton(self.groupBox)
        self.rController.setObjectName(u"rController")
        self.rController.setGeometry(QRect(10, 70, 89, 20))
        self.rAdmin = QRadioButton(self.groupBox)
        self.rAdmin.setObjectName(u"rAdmin")
        self.rAdmin.setGeometry(QRect(10, 30, 89, 20))

        self.retranslateUi(UpdateUserDialog)
        self.buttonBox.accepted.connect(UpdateUserDialog.accept)
        self.buttonBox.rejected.connect(UpdateUserDialog.reject)

        QMetaObject.connectSlotsByName(UpdateUserDialog)
    # setupUi

    def retranslateUi(self, UpdateUserDialog):
        UpdateUserDialog.setWindowTitle(QCoreApplication.translate("UpdateUserDialog", u"Update User", None))
        self.lbTitle.setText(QCoreApplication.translate("UpdateUserDialog", u"Update User:", None))
        self.chStatus.setText(QCoreApplication.translate("UpdateUserDialog", u"Disabled", None))
        self.groupBox.setTitle(QCoreApplication.translate("UpdateUserDialog", u"User Role", None))
        self.rController.setText(QCoreApplication.translate("UpdateUserDialog", u"Controller", None))
        self.rAdmin.setText(QCoreApplication.translate("UpdateUserDialog", u"Admin", None))
    # retranslateUi

