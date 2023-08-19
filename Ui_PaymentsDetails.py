# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paymentsDetails.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QSizePolicy,
    QTableView, QTimeEdit, QWidget)

class Ui_PaymentsDetails(object):
    def setupUi(self, PaymentsDetails):
        if not PaymentsDetails.objectName():
            PaymentsDetails.setObjectName(u"PaymentsDetails")
        PaymentsDetails.resize(410, 303)
        self.paymentsDetailsTableView = QTableView(PaymentsDetails)
        self.paymentsDetailsTableView.setObjectName(u"paymentsDetailsTableView")
        self.paymentsDetailsTableView.setGeometry(QRect(0, 120, 411, 191))
        self.layoutWidget = QWidget(PaymentsDetails)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 301, 80))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lMovieName = QLineEdit(self.layoutWidget)
        self.lMovieName.setObjectName(u"lMovieName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lMovieName)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.tSeanceTime = QTimeEdit(self.layoutWidget)
        self.tSeanceTime.setObjectName(u"tSeanceTime")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.tSeanceTime)

        self.seanceDate = QDateEdit(self.layoutWidget)
        self.seanceDate.setObjectName(u"seanceDate")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.seanceDate)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)


        self.retranslateUi(PaymentsDetails)

        QMetaObject.connectSlotsByName(PaymentsDetails)
    # setupUi

    def retranslateUi(self, PaymentsDetails):
        PaymentsDetails.setWindowTitle(QCoreApplication.translate("PaymentsDetails", u"Payments Dialog", None))
        self.label.setText(QCoreApplication.translate("PaymentsDetails", u"Movie Name", None))
        self.label_3.setText(QCoreApplication.translate("PaymentsDetails", u"Seance Time", None))
        self.label_2.setText(QCoreApplication.translate("PaymentsDetails", u"Seance Date", None))
    # retranslateUi

