from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QEventLoop, QUrl
import time
import threading

from PySide6.QtWidgets import QMainWindow, QHeaderView, QPushButton

from CustomNetworkAccessManager import CustomNetworkAccessManager
from PaymentsModel import PaymentsModel
from Ui_MainWindow import Ui_MainWindow
from datetime import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.baseUrl = 'http://localhost/api/'
        self.n1 = CustomNetworkAccessManager(self.baseUrl + "payments")
        self.dtInpStart.setDate(datetime(datetime.today().year, 1, 1))
        self.dtInpEnd.setDate(datetime.today().date())

        self._paymentsHeaders = ['Id', 'Name', 'Card Number', 'Amount', 'Status', 'Creation Date']
        self.paymentModel = [[]]

        header = self.paymentsTableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.n1.completed.connect(self.populatePaymentsTable)
        self.n1.get()

        self.app = app
        self.setWindowTitle("Premium Cinema")
        self.pSearchButton.clicked.connect(self.searchPayers)

    def populatePaymentsTable(self):
        self.paymentModel = PaymentsModel(self.n1.getTabularData(), self._paymentsHeaders)
        self.paymentsTableView.setModel(self.paymentModel)

    def searchPayers(self):
        payers_filter = {
            'name': ('like', self.lePayerSearch.text()),
            'start': ("gte", self.dtInpStart.date().toString("yyyy-M-d")),
            'end': ("lte", self.dtInpEnd.date().toString("yyyy-M-d"))
        }
        self.n1.setQueryParams(payers_filter)
        self.n1.get()
        # self.n2.post('http://localhost/api/payments?', self.payerInfo)
