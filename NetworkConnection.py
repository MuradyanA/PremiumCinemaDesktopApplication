import json
import time

from PySide6 import QtCore

from Exceptions.TokenIsMissingException import TokenIsMissingException
from PySide6.QtCore import QUrl, QByteArray, QThread, QEventLoop, Signal, QObject
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply


class NetworkConnection(QObject):
    _token = "32|6VRNNg9iUVXJf133WVU1YXd8SQgto1T5eIn9UpAC"

    def __init__(self, loop):
        self.finished = Signal(str)
        self._manager = QNetworkAccessManager()
        self._manager.finished.connect(
            self.requestFinished)
        self._reply = None
        self._data = None
        self._request = None
        self._loop = loop

    def get(self, url, query_params=[], auth=True):
        self._request = QNetworkRequest(QUrl(url))
        if auth:
            # Create the network request
            self._addHeader(self._request)
            # Make the POST request
        print("GET")
        if len(query_params) > 0:
            for key, value in query_params:
                self._request.addQueryItem(key, value)

        self._reply = self._manager.get(self._request)

        self._reply.finished.connect(self.requestFinished)

    def post(self, url, data, auth=True):

        self._request = QNetworkRequest(QUrl(url))
        if auth:
            # Create the network request
            self._addHeader(self._request)
            # Make the POST request
        json_data = json.dumps(data).encode('utf-8')

        self._reply = self._manager.post(self._request, json_data)
        self._reply.finished.connect(self.requestFinished)

