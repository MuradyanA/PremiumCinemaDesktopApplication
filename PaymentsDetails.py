from PySide6.QtCore import QRect
from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QCheckBox, QGroupBox, QRadioButton, QVBoxLayout, \
    QButtonGroup, QApplication, QWidget, QTableView, QTableWidgetItem

from Ui_PaymentsDetails import Ui_PaymentsDetails


class PaymentsDetails(QDialog, Ui_PaymentsDetails):
        def __init__(self):
            super().__init__()
            self.setupUi()
            widget = QWidget()
            widget.setWindowTitle("Payments Details")
            table_view = QTableView(widget)

        def setupUi(self):
            super().setupUi(self)
