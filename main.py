import json
import sys

from PySide6 import QtWidgets

from CustomNetworkAccessManager import CustomNetworkAccessManager
from LoginDialog import LoginDialog
from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication, QWidget


def run_main_window():
    window = MainWindow(app)
    window.show()


app = QtWidgets.QApplication(sys.argv)
login_net_manager = CustomNetworkAccessManager('http://localhost/api')
login_net_manager.completed.connect(run_main_window)
login_dialog = LoginDialog()
login_dialog.exec()

data = {'email': login_dialog.lLogin.text(), 'password': login_dialog.lPassword.text()}

login_net_manager.post('login', json.dumps(data).encode())

app.exec()



