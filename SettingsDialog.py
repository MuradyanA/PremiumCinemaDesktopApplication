from PySide6.QtCore import QRect
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QCheckBox, QGroupBox, QRadioButton, QVBoxLayout, \
    QButtonGroup

from Ui_SettingsDialog import Ui_settingsDialog


class SettingsDialog(QDialog, Ui_settingsDialog):
        def __init__(self):
            super().__init__()
            self.setupUi()

        def setupUi(self):
            super().setupUi(self)
