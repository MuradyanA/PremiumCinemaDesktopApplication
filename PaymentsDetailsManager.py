from PySide6.QtCore import Signal
from PySide6.QtNetwork import QNetworkReply

from CustomNetworkAccessManager import CustomNetworkAccessManager

class PaymentsDetailsManager(CustomNetworkAccessManager):
    paymentsDetailsProcessed = Signal(QNetworkReply)

    def __init__(self, url):
        print(url)
        super().__init__(url)

    def getPaymentsDetails(self):
        print(super()._data)

    def getPaymentsList(self):
        pass
