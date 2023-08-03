import json
import time

from PySide6.QtCore import QUrl, Signal, QEventLoop, QObject
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

from Exceptions.TokenIsMissingException import TokenIsMissingException


class CustomNetworkAccessManager(QNetworkAccessManager, QObject):
    _token = "32|6VRNNg9iUVXJf133WVU1YXd8SQgto1T5eIn9UpAC"
    finished = Signal(QNetworkReply)
    completed = Signal(str)

    def __init__(self, url, auth=True):
        super().__init__()
        self._request = QNetworkRequest(QUrl(url))
        self._reply = None
        self._data = None
        self._auth = auth

    def get(self):
        self._addHeader()
        self._reply = super().get(self._request)
        loop = QEventLoop()
        self._reply.finished.connect(self.handleResponse)
        loop.exec_()

    def post(self):
        pass

    def _addHeader(self):
        if self._auth and self._token is None:
            raise TokenIsMissingException()

        if self._token:
            bearer_token = f"Bearer {self._token}"
            self._request.setRawHeader(b"Authorization", bearer_token.encode('utf-8'))

        # self._request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        self._request.setRawHeader(b"Accept", b"application/json")
        self._request.setRawHeader(b"Content-Type", b"application/json")

    def handleResponse(self):
        if self._reply.error() == QNetworkReply.NoError:
            data = self._reply.readAll()
            response = data.data().decode()

            if "token" in response:
                self._token = json.loads(response)['token']
            else:

                if response.strip():
                    try:
                        self._data = json.loads(response)
                        self.completed.emit('Response ready')
                        # return self._data

                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON response: {e}")
                        return
        else:
            # Handle the error
            print("Error:", self._reply.errorString())

    def getTabularData(self):
        # print(self._data)
        tabularData = []
        for dict in self._data['data']:
            row = []
            for key, value in dict.items():
                row.append(value)
            tabularData.append(row)

        return tabularData