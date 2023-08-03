import sys

from PySide6 import QtWidgets

from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication, QWidget

app = QtWidgets.QApplication(sys.argv)
window = MainWindow(app)
window.show()

app.exec()
