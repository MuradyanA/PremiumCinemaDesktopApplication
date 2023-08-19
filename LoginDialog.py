from PySide6.QtCore import QRect
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QCheckBox, QGroupBox, QRadioButton, QVBoxLayout, \
    QButtonGroup

from Ui_LoginDialog import Ui_LoginDialog

class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.buttonBox.buttons()[0].setText("Log In")

    def setupUi(self):
        super().setupUi(self)