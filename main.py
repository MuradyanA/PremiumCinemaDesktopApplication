import json
import sys

from PySide6 import QtWidgets

from CustomNetworkAccessManager import CustomNetworkAccessManager
from LoginDialog import LoginDialog
from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication, QWidget
from AppSetings import AppSetting
settings = AppSetting()


def run_main_window():
    window = MainWindow(app, settings)
    window.show()


app = QtWidgets.QApplication(sys.argv)
login_net_manager = CustomNetworkAccessManager(settings.get_param('servicePath'))
login_net_manager.completed.connect(run_main_window)
login_dialog = LoginDialog()
login_dialog.exec()

data = {'email': login_dialog.lLogin.text(), 'password': login_dialog.lPassword.text()}

login_net_manager.post(json.dumps(data).encode(), 'login')

app.exec()



