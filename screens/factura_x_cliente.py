from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_FacturaClienteWindow(object):
    # ! -------- Código autogenerado ----------
    def setupUi(self, FacturaClienteWindow):
        FacturaClienteWindow.setObjectName("FacturaClienteWindow")
        FacturaClienteWindow.resize(598, 315)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bx-search-alt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FacturaClienteWindow.setWindowIcon(icon)
        self.lb_factura_x_cliente = QtWidgets.QLabel(FacturaClienteWindow)
        self.lb_factura_x_cliente.setGeometry(QtCore.QRect(220, 10, 151, 16))
        self.lb_factura_x_cliente.setObjectName("lb_factura_x_cliente")
        self.lb_numero_cedula = QtWidgets.QLabel(FacturaClienteWindow)
        self.lb_numero_cedula.setGeometry(QtCore.QRect(30, 50, 81, 16))
        self.lb_numero_cedula.setObjectName("lb_numero_cedula")
        self.le_cedula_cliente = QtWidgets.QLineEdit(FacturaClienteWindow)
        self.le_cedula_cliente.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.le_cedula_cliente.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.le_cedula_cliente.setObjectName("le_cedula_cliente")
        self.tb_facturas = QtWidgets.QTableView(FacturaClienteWindow)
        self.tb_facturas.setGeometry(QtCore.QRect(20, 80, 561, 192))
        self.tb_facturas.setObjectName("tb_facturas")
        self.button_ordenar_fecha = QtWidgets.QPushButton(FacturaClienteWindow)
        self.button_ordenar_fecha.setGeometry(QtCore.QRect(260, 40, 41, 31))
        self.button_ordenar_fecha.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/bx-font-size.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_ordenar_fecha.setIcon(icon1)
        self.button_ordenar_fecha.setIconSize(QtCore.QSize(25, 25))
        self.button_ordenar_fecha.setObjectName("button_ordenar_fecha")
        self.lb_numero_facturas = QtWidgets.QLabel(FacturaClienteWindow)
        self.lb_numero_facturas.setGeometry(QtCore.QRect(20, 290, 81, 16))
        self.lb_numero_facturas.setObjectName("lb_numero_facturas")
        self.lb_n_facturas = QtWidgets.QLabel(FacturaClienteWindow)
        self.lb_n_facturas.setGeometry(QtCore.QRect(120, 290, 41, 16))
        self.lb_n_facturas.setObjectName("lb_n_facturas")

        self.retranslateUi(FacturaClienteWindow)
        QtCore.QMetaObject.connectSlotsByName(FacturaClienteWindow)

    def retranslateUi(self, FacturaClienteWindow):
        _translate = QtCore.QCoreApplication.translate
        FacturaClienteWindow.setWindowTitle(_translate("FacturaClienteWindow", "Factura_x_Cliente"))
        self.lb_factura_x_cliente.setText(_translate("FacturaClienteWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Factura_x_Cliente</span></p></body></html>"))
        self.lb_numero_cedula.setText(_translate("FacturaClienteWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">N. Cedula</span></p></body></html>"))
        self.lb_numero_facturas.setText(_translate("FacturaClienteWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">N# Facturas</span></p><p><br/></p></body></html>"))
        self.lb_n_facturas.setText(_translate("FacturaClienteWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">#</span></p><p><br/></p></body></html>"))
    # ! ---------------------------------------

    # ? ------ Funcionalidades Propias --------
    def open_busqueda_x_factura(self):
        app = QtWidgets.QApplication(sys.argv)
        FacturaClienteWindow = QtWidgets.QWidget()
        ui = Ui_FacturaClienteWindow()
        ui.setupUi(FacturaClienteWindow)
        FacturaClienteWindow.show()
        sys.exit(app.exec_())
    # ? ---------------------------------------

if __name__ == "__main__":
    busqueda_x_factura_window = Ui_FacturaClienteWindow()
    busqueda_x_factura_window.open_busqueda_x_factura()