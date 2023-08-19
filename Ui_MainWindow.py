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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QTableView, QToolBar, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1317, 886)
        self.actionCancelPayment = QAction(MainWindow)
        self.actionCancelPayment.setObjectName(u"actionCancelPayment")
        self.actionCancelPayment.setEnabled(True)
        icon = QIcon()
        iconThemeName = u"audio-card"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/toolbar/Icons/cancel.jpg", QSize(), QIcon.Normal, QIcon.Off)

        self.actionCancelPayment.setIcon(icon)
        self.actionCancelPayment.setMenuRole(QAction.NoRole)
        self.actionViewDetails = QAction(MainWindow)
        self.actionViewDetails.setObjectName(u"actionViewDetails")
        icon1 = QIcon()
        icon1.addFile(u":/toolbar/Icons/magnifyerDocument.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/toolbar/Icons/magnifyerDocument.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionViewDetails.setIcon(icon1)
        self.actionViewDetails.setMenuRole(QAction.NoRole)
        self.actionEditUser = QAction(MainWindow)
        self.actionEditUser.setObjectName(u"actionEditUser")
        icon2 = QIcon()
        icon2.addFile(u":/edit/Icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEditUser.setIcon(icon2)
        self.actionEditUser.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(180, 50, 1071, 791))
        self.users = QWidget()
        self.users.setObjectName(u"users")
        self.leUserSearch = QLineEdit(self.users)
        self.leUserSearch.setObjectName(u"leUserSearch")
        self.leUserSearch.setGeometry(QRect(20, 60, 551, 41))
        font = QFont()
        font.setPointSize(12)
        self.leUserSearch.setFont(font)
        self.usersTableView = QTableView(self.users)
        self.usersTableView.setObjectName(u"usersTableView")
        self.usersTableView.setGeometry(QRect(20, 140, 1021, 591))
        self.usersTableView.setBaseSize(QSize(100, 100))
        self.usersTableView.setFont(font)
        self.usersTableView.horizontalHeader().setVisible(True)
        self.usersTableView.horizontalHeader().setCascadingSectionResizes(True)
        self.uSearchButton = QPushButton(self.users)
        self.uSearchButton.setObjectName(u"uSearchButton")
        self.uSearchButton.setGeometry(QRect(600, 60, 61, 41))
        self.uSearchButton.setFont(font)
        self.uSearchButton.setAutoFillBackground(False)
        self.uSearchButton.setStyleSheet(u"background-color: #f3f3f3;\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/magnifier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.uSearchButton.setIcon(icon3)
        self.uSearchButton.setIconSize(QSize(46, 33))
        self.stackedWidget.addWidget(self.users)
        self.payments = QWidget()
        self.payments.setObjectName(u"payments")
        self.paymentsTableView = QTableView(self.payments)
        self.paymentsTableView.setObjectName(u"paymentsTableView")
        self.paymentsTableView.setGeometry(QRect(30, 350, 1021, 431))
        self.paymentsTableView.setBaseSize(QSize(100, 100))
        self.paymentsTableView.setFont(font)
        self.paymentsTableView.horizontalHeader().setVisible(True)
        self.paymentsTableView.horizontalHeader().setCascadingSectionResizes(True)
        self.groupBox_2 = QGroupBox(self.payments)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(19, 219, 1031, 111))
        font1 = QFont()
        font1.setPointSize(14)
        self.groupBox_2.setFont(font1)
        self.lePayerSearch = QLineEdit(self.groupBox_2)
        self.lePayerSearch.setObjectName(u"lePayerSearch")
        self.lePayerSearch.setGeometry(QRect(10, 50, 551, 41))
        self.lePayerSearch.setFont(font)
        self.dtInpStart = QDateEdit(self.groupBox_2)
        self.dtInpStart.setObjectName(u"dtInpStart")
        self.dtInpStart.setGeometry(QRect(600, 50, 151, 41))
        self.dtInpStart.setFont(font)
        self.dtInpEnd = QDateEdit(self.groupBox_2)
        self.dtInpEnd.setObjectName(u"dtInpEnd")
        self.dtInpEnd.setGeometry(QRect(760, 50, 151, 41))
        self.dtInpEnd.setFont(font)
        self.pSearchButton = QPushButton(self.groupBox_2)
        self.pSearchButton.setObjectName(u"pSearchButton")
        self.pSearchButton.setGeometry(QRect(940, 50, 61, 41))
        self.pSearchButton.setFont(font)
        self.pSearchButton.setAutoFillBackground(False)
        self.pSearchButton.setStyleSheet(u"background-color: #f3f3f3;\n"
"\n"
"")
        self.pSearchButton.setIcon(icon3)
        self.pSearchButton.setIconSize(QSize(46, 33))
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
        self.btnTickets = QPushButton(self.groupBox)
        self.btnTickets.setObjectName(u"btnTickets")
        self.btnTickets.setGeometry(QRect(10, 20, 121, 121))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTickets.sizePolicy().hasHeightForWidth())
        self.btnTickets.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u":/tickets/Icons/payments.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnTickets.setIcon(icon4)
        self.btnTickets.setIconSize(QSize(128, 128))
        self.btnUsers = QPushButton(self.groupBox)
        self.btnUsers.setObjectName(u"btnUsers")
        self.btnUsers.setGeometry(QRect(10, 170, 121, 121))
        sizePolicy.setHeightForWidth(self.btnUsers.sizePolicy().hasHeightForWidth())
        self.btnUsers.setSizePolicy(sizePolicy)
        icon5 = QIcon()
        icon5.addFile(u":/users/Icons/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnUsers.setIcon(icon5)
        self.btnUsers.setIconSize(QSize(128, 128))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1317, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font2 = QFont()
        font2.setPointSize(11)
        self.statusbar.setFont(font2)
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setIconSize(QSize(40, 40))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionCancelPayment)
        self.toolBar.addAction(self.actionViewDetails)
        self.toolBar.addAction(self.actionEditUser)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCancelPayment.setText(QCoreApplication.translate("MainWindow", u"Cancel Payment", None))
#if QT_CONFIG(tooltip)
        self.actionCancelPayment.setToolTip(QCoreApplication.translate("MainWindow", u"Cancel Choosen Payment", None))
#endif // QT_CONFIG(tooltip)
        self.actionViewDetails.setText(QCoreApplication.translate("MainWindow", u"View Details", None))
#if QT_CONFIG(tooltip)
        self.actionViewDetails.setToolTip(QCoreApplication.translate("MainWindow", u"View Payment's Details", None))
#endif // QT_CONFIG(tooltip)
        self.actionEditUser.setText(QCoreApplication.translate("MainWindow", u"Edit User", None))
#if QT_CONFIG(tooltip)
        self.actionEditUser.setToolTip(QCoreApplication.translate("MainWindow", u"Edit User", None))
#endif // QT_CONFIG(tooltip)
        self.leUserSearch.setText("")
        self.uSearchButton.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.lePayerSearch.setText("")
        self.pSearchButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Navigator", None))
        self.btnTickets.setText("")
        self.btnUsers.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

