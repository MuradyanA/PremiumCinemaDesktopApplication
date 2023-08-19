import json
import time

from PySide6 import QtWidgets
from PySide6.QtCore import QUrl, Signal, QEventLoop, QObject, QUrlQuery, QByteArray, QBuffer
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtWidgets import QLabel

from Exceptions.TokenIsMissingException import TokenIsMissingException
from Exceptions.NetworkException import NetworkException


class CustomNetworkAccessManager(QNetworkAccessManager, QObject):
    token = "32|6VRNNg9iUVXJf133WVU1YXd8SQgto1T5eIn9UpAC"
    finished = Signal(QNetworkReply)
    completed = Signal(str)

    def __init__(self, url, auth=True):
        super().__init__()
        self._url = url
        self._request = None
        self._reply = None
        self._query = None
        self._data = None
        self._auth = auth
        self.queryString = ""

    def _request_with_body(self, suffix, body, request_type):
        method = getattr(super(), request_type)
        self._prepareRequest(suffix)
        self._addHeader()
        self._reply = method(self._request, QByteArray(body))
        self._reply.finished.connect(self.handleResponse)

    def get(self, suffix=None, return_type='col'):
        if suffix is not None:
            self._prepareRequest(suffix)
        else:
            self._prepareRequest()
        self._addHeader()
        self._reply = super().get(self._request)
        # loop = QEventLoop()
        self._reply.finished.connect(self.handleResponse)
        # loop.exec_()

    def post(self, suffix, body):
        self._request_with_body(suffix, body, 'post')

    def put(self, suffix, body):
        self._request_with_body(suffix, body, 'put')

    def _addHeader(self):
        if self._auth and self.token is None:
            raise TokenIsMissingException()

        if self.token:
            bearertoken = f"Bearer {self.token}"
            self._request.setRawHeader(b"Authorization", bearertoken.encode('utf-8'))

        # self._request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        self._request.setRawHeader(b"Accept", b"application/json")
        self._request.setRawHeader(b"Content-Type", b"application/json")

    def handleResponse(self):
        try:
            if self._reply.error() == QNetworkReply.NoError:
                data = self._reply.readAll()
                response = data.data().decode()
                if "token" in response:
                    CustomNetworkAccessManager.token = json.loads(response)['token']
                else:
                    if response.strip():
                        try:
                            self._data = json.loads(response)
                        except json.JSONDecodeError as e:
                            print(f"Error decoding JSON response: {e}")
                            return
            else:
                raise NetworkException(self._reply.readAll().toStdString())
            self.completed.emit(self._reply.url().toString())
        except NetworkException as e:
            errors = json.loads(e.message)
            err_message = ''
            for key in errors['errors']:
                err_message += "".join(errors['errors'][key]) + '\n'
            message_box = QtWidgets.QMessageBox()
            message_box.setWindowTitle("Error Response")
            message_box.setText(err_message)
            message_box.setIcon(QtWidgets.QMessageBox.Critical)
            message_box.exec()

    def getTabularData(self, external_table=None):
        tabularData = []
        obj = None
        if external_table is not None:
            obj = external_table
        else:
            obj = self._data['data']
        if len(obj) == 0:
            return tabularData

        for dict in obj:
            row = []
            for key, value in dict.items():
                row.append(value)
            tabularData.append(row)

        return tabularData

    def get_data(self):
        return self._data['data']

    def setQueryParams(self, params):
        self._query = QUrlQuery()
        for key, (oper, value) in params.items():
            self._query.addQueryItem(f"{key}[{oper}]", f"{value}")

    def _prepareRequest(self, suffix=None):
        if suffix is not None:
            url = QUrl(self._url + f"/{suffix}")
        else:
            url = QUrl(self._url)

        if self._query is not None:
            url.setQuery(self._query)

        self._request = QNetworkRequest(url)
