from PySide6.QtCore import QRect
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QCheckBox, QGroupBox, QRadioButton, QVBoxLayout, \
    QButtonGroup

from Ui_UpdateUserDialog import Ui_UpdateUserDialog


class UpdateUserDialog(QDialog, Ui_UpdateUserDialog):
        def __init__(self):
            super().__init__()
            self.setupUi()
            self.userRoles = QButtonGroup()
            self.userRoles.addButton(self.rController)
            self.userRoles.addButton(self.rAdmin)

        def setupUi(self):
            super().setupUi(self)
