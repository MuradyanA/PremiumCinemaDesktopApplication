import json

from PySide6.QtCore import QTime, QDate
from PySide6.QtWidgets import QMainWindow, QHeaderView, QPushButton, QToolBar, QMessageBox, QAbstractItemView, QLabel, \
    QDialog
from PySide6.QtUiTools import QUiLoader
from CustomNetworkAccessManager import CustomNetworkAccessManager
from PaymentsDetailsManager import PaymentsDetailsManager
from PaymentsDetailsModel import PaymentsDetailsModel
from PaymentsModel import PaymentsModel
from Ui_MainWindow import Ui_MainWindow
from SettingsDialog import SettingsDialog
from datetime import datetime

from Ui_UpdateUserDialog import Ui_UpdateUserDialog
from UpdateUserDialog import UpdateUserDialog
from UsersModel import UsersModel
from PaymentsDetails import PaymentsDetails

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app, settings):
        super().__init__()
        self.setupUi(self)
        self.settings = settings
        self.baseUrl = settings.get_param('servicePath')
        self.usersNetManager = CustomNetworkAccessManager(self.baseUrl + "/users")
        self.actionEditUser.setVisible(False)

        self.paymentNetManager = CustomNetworkAccessManager(self.baseUrl + "/payments")
        self.paymentsTableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.usersTableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.dtInpStart.setDate(datetime(datetime.today().year, 1, 1))
        self.dtInpEnd.setDate(datetime.today().date())
        self.paymentNetManager.completed.connect(self.processPaymentData)

        self.usersNetManager.completed.connect(self.populateUsersTable)

        self.paymentNetManager.get()

        self.actionCancelPayment.triggered.connect(self.cancelPayment)
        self.btnTickets.clicked.connect(lambda: self.switchPage(1))
        self.btnUsers.clicked.connect(lambda: self.switchPage(0))

        self._paymentsHeaders = ['Id', 'Name', 'Card Number', 'Amount', 'Status', 'Creation Date']
        self.paymentModel = [[]]

        self._usersHeaders = ['Id', 'Name', 'Email', 'Account Status', 'Is Admin', 'Registration Date']
        self.userModel = [[]]

        header = self.paymentsTableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        users_header = self.usersTableView.horizontalHeader()
        users_header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.app = app
        self.setWindowTitle("Premium Cinema")
        self.pSearchButton.clicked.connect(self.searchPayers)

        self.uSearchButton.clicked.connect(self.searchEmployees)

        self.updateUserDialog = UpdateUserDialog()
        self.actionEditUser.triggered.connect(self.openUpdateUserDialog)

        self._paymentsDetailsHeaders = ['Seat', 'Seat Type', 'Hall']
        self.paymentsDetailsModel = [[]]
        self.paymentsDetails = PaymentsDetails()
        self.actionViewDetails.triggered.connect(self.openPaymentsDetailsWindow)

        self.actionSettings.triggered.connect(self.openSettingsDialog)

    def processPaymentData(self, url):
        if url == 'http://localhost/api/payments':
            self.paymentModel = PaymentsModel(self.paymentNetManager.getTabularData(), self._paymentsHeaders)
            self.paymentsTableView.setModel(self.paymentModel)
        elif url.startswith('http://localhost/api/payments'):
            payment_details = self.paymentNetManager.get_data()
            print(payment_details)
            self.paymentsDetailsModel = PaymentsDetailsModel(self.paymentNetManager.getTabularData(
                payment_details['tickets']),
                self._paymentsDetailsHeaders)
            seance_time_list = payment_details['seance_time'].split(':')
            seance_time = QTime(int(seance_time_list[0]), int(seance_time_list[1]))

            seance_date_list = payment_details['seance_date'].split('-')
            seance_date = QDate(int(seance_date_list[0]), int(seance_date_list[1]), int(seance_date_list[2]))

            self.paymentsDetails.lMovieName.setText(payment_details['movie'])
            self.paymentsDetails.tSeanceTime.setTime(seance_time)
            self.paymentsDetails.seanceDate.setDate(seance_date)
            self.paymentsDetails.lMovieName.setEnabled(False)
            self.paymentsDetails.tSeanceTime.setEnabled(False)
            self.paymentsDetails.seanceDate.setEnabled(False)
            self.paymentsDetails.paymentsDetailsTableView.setModel(self.paymentsDetailsModel)

    def populateUsersTable(self):
        self.userModel = UsersModel(self.usersNetManager.getTabularData(), self._usersHeaders)
        self.usersTableView.setModel(self.userModel)


    def searchPayers(self):
        payers_filter = {
            'name': ('like', self.lePayerSearch.text()),
            'start': ("gte", self.dtInpStart.date().toString("yyyy-M-d")),
            'end': ("lte", self.dtInpEnd.date().toString("yyyy-M-d"))
        }
        self.paymentNetManager.setQueryParams(payers_filter)
        self.paymentNetManager.get()
        # self.n2.post('http://localhost/api/payments?', self.payerInfo)

    def searchEmployees(self):
        employees_filter = {
            'name': ('like', self.leUserSearch.text())
        }
        self.usersNetManager.setQueryParams(employees_filter)
        self.usersNetManager.get()
        # self.n2.post('http://localhost/api/payments?', self.payerInfo)

    def cancelPayment(self):
        try:
            index = self.paymentsTableView.selectionModel().selectedRows()[0]
        except IndexError:
            QMessageBox.critical(self, 'Undefined Payment', 'Please select the payment in the table')
            return
        message_box = QMessageBox(QMessageBox.Warning, "Cancel Payment", "Are you sure to cancel the payment?",
                                  QMessageBox.Ok | QMessageBox.Cancel)
        button = message_box.exec_()

        if button == QMessageBox.Ok:
            index = self.paymentsTableView.selectionModel().selectedRows()[0]
            payment_list = self.paymentNetManager.getTabularData()
            payment_id = payment_list[index.row()][0]
            self.statusBar().showMessage("Updating data...", 2000)

            self.paymentNetManager.put(payment_id, b'{"status": "cancelled"}')

    def viewDetails(self):
        pass

    def switchPage(self, index):
        if index == 0:
            self.actionEditUser.setVisible(True)
            self.actionViewDetails.setVisible(False)
            self.actionCancelPayment.setVisible(False)

            self.usersNetManager.get()
        else:
            self.actionEditUser.setVisible(False)
            self.actionViewDetails.setVisible(True)
            self.actionCancelPayment.setVisible(True)

        self.stackedWidget.setCurrentIndex(index)

    def openUpdateUserDialog(self):
        try:
            index = self.usersTableView.selectionModel().selectedRows()[0]
            users_list = self.usersNetManager.getTabularData()
            user_id = users_list[index.row()][0]
            user_name = users_list[index.row()][1]
            user_account_status = False if users_list[index.row()][3] == "Disabled" else True
            user_is_admin = users_list[index.row()][4]
        except IndexError:
            QMessageBox.critical(self, 'Undefined User', 'Please select the user in the table')
            return

        self.updateUserDialog.chStatus.setChecked(user_account_status)
        if user_is_admin == "Admin":
            self.updateUserDialog.rAdmin.setChecked(True)
        else:
            self.updateUserDialog.rController.setChecked(True)

        dlg = self.updateUserDialog.exec()

        if dlg == QDialog.Accepted:
            updated_user_account_status = self.updateUserDialog.chStatus.isChecked()
            updated_user_is_admin = self.updateUserDialog.userRoles.checkedButton().text()
            if user_account_status != updated_user_account_status or user_is_admin != updated_user_is_admin:
                is_admin = True if updated_user_is_admin == 'Admin' else False
                data = {'status': updated_user_account_status, 'isAdmin': is_admin}
                self.usersNetManager.put(user_id, json.dumps(data).encode())
                # self.usersNetManager.put(user_id, ''.join(format(ord(i), '08b') for i in json.dumps(data)))

    def openPaymentsDetailsWindow(self):
        try:
            row_index = self.paymentsTableView.selectionModel().selectedRows()[0].row()
            payment_id = self.paymentModel.index(row_index, 0).data()
            self.paymentNetManager.get(payment_id)
        except IndexError:
            QMessageBox.critical(self, 'Undefined Payer', 'Please select the payer in the table')
            return
        self.paymentsDetails.exec()

    def openSettingsDialog(self):
        settings_dialog = SettingsDialog()
        settings_dialog.lServicePath.setText(self.settings.get_param('servicePath'))
        dlg = settings_dialog.exec()

        if dlg == QDialog.Accepted:
            self.settings.set_param('servicePath', settings_dialog.lServicePath.text())

