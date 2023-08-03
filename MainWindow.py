from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QEventLoop
import time
import threading


from PySide6.QtWidgets import QMainWindow, QHeaderView, QPushButton

from CustomNetworkAccessManager import CustomNetworkAccessManager
from PaymentsModel import PaymentsModel
from Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, app):
        super().__init__()
        self.n1 = CustomNetworkAccessManager('http://localhost/api/payments')
        self._paymentsHeaders = ['Id', 'Name', 'Card Number', 'Amount', 'Status', 'Creation Date']
        self.paymentModel = [[]]
        self.n1.completed.connect(self.populatePaymentsTable)
        self.n1.get()

        # horizontal_header = self.paymentsTableView.horizontalHeader()
        self.setupUi(self)
        self.app = app
        self.setWindowTitle("Premium Cinema")



    def populatePaymentsTable(self):
        self.paymentModel = PaymentsModel(self.n1.getTabularData(), self._paymentsHeaders)
        self.paymentsTableView.setModel(self.paymentModel)

    def compl2(self):
        print(2)
        #
        # from PySide6 import QtWidgets
        # from PySide6.QtCore import Qt, QEventLoop
        # import time
        # import threading
        #
        # from PySide6.QtWidgets import QMainWindow, QHeaderView, QPushButton
        #
        # from CustomNetworkAccessManager import CustomNetworkAccessManager
        # from PaymentsModel import PaymentsModel
        # from Ui_MainWindow import Ui_MainWindow
        # from NetworkConnection import NetworkConnection
        #
        # class MainWindow(QMainWindow, Ui_MainWindow):
        #
        #     def __init__(self, app):
        #         super().__init__()
        #         self.n1 = CustomNetworkAccessManager('http://localhost/api/payments')
        #         self._paymentsHeaders = ['Id', 'Name', 'Card Number', 'Amount', 'Status', 'Creation Date']
        #         self.paymentModel = [[]]
        #         self.setupUi(self)
        #         self.app = app
        #         self.setWindowTitle("Premium Cinema")
        #
        #         self.button.clicked.connect(self.buttonPush)
        #
        #     def buttonPush(self):
        #         self.n1.completed.connect(self.populatePaymentsTable)
        #         self.n1.get()
        #
        #     def populatePaymentsTable(self):
        #         self.paymentModel = PaymentsModel(self.n1.getTabularData(), self._paymentsHeaders)
        #         self.paymentsTableView.setModel(self.paymentModel)
        #
        #     def compl2(self):
        #         print(2)





