# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
    QStatusBar, QTableView, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1317, 886)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(180, 50, 1071, 791))
        self.users = QWidget()
        self.users.setObjectName(u"users")
        self.radioButton = QRadioButton(self.users)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(160, 80, 89, 20))
        self.stackedWidget.addWidget(self.users)
        self.payments = QWidget()
        self.payments.setObjectName(u"payments")
        self.paymentsTableView = QTableView(self.payments)
        self.paymentsTableView.setObjectName(u"paymentsTableView")
        self.paymentsTableView.setGeometry(QRect(30, 350, 1021, 431))
        self.paymentsTableView.setBaseSize(QSize(100, 100))
        font = QFont()
        font.setPointSize(12)
        self.paymentsTableView.setFont(font)
        self.paymentsTableView.horizontalHeader().setVisible(True)
        self.paymentsTableView.horizontalHeader().setCascadingSectionResizes(True)
        self.button = QPushButton(self.payments)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(430, 80, 221, 51))
        self.groupBox_2 = QGroupBox(self.payments)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(19, 219, 1031, 111))
        font1 = QFont()
        font1.setPointSize(16)
        self.groupBox_2.setFont(font1)
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 50, 551, 41))
        self.lineEdit.setFont(font)
        self.dateEdit = QDateEdit(self.groupBox_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(600, 50, 151, 41))
        self.dateEdit.setFont(font)
        self.dateEdit_2 = QDateEdit(self.groupBox_2)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(760, 50, 151, 41))
        self.dateEdit_2.setFont(font)
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(940, 50, 61, 41))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"background-color: #f3f3f3;\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/magnifier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(46, 33))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(600, 20, 71, 16))
        self.label.setFont(font)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(760, 20, 71, 16))
        self.label_2.setFont(font)
        self.stackedWidget.addWidget(self.payments)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 80, 141, 311))
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 170, 121, 121))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/tickets/Icons/payments.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(128, 128))
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 40, 121, 121))
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u":/users/Icons/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(128, 128))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1317, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.lineEdit.setText("")
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Navigator", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
    # retranslateUi

