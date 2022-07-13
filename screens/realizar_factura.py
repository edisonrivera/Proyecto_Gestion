from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# * Para ejectuar desde el mismo archivo todas las 'funciones'
# * tienes que eliminar la palabra 'screens.' 


class Ui_RealizarFacturaWindow(object):
    # ! -------- Código autogenerado ----------
    def setupUi(self, RealizarFacturaWindow):
        RealizarFacturaWindow.setObjectName("RealizarFacturaWindow")
        RealizarFacturaWindow.resize(512, 203)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bx-cart-add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RealizarFacturaWindow.setWindowIcon(icon)
        self.lb_cedCli = QtWidgets.QLabel(RealizarFacturaWindow)
        self.lb_cedCli.setGeometry(QtCore.QRect(40, 20, 51, 16))
        self.lb_cedCli.setObjectName("lb_cedCli")
        self.le_ced = QtWidgets.QLineEdit(RealizarFacturaWindow)
        self.le_ced.setGeometry(QtCore.QRect(100, 20, 181, 20))
        self.le_ced.setObjectName("le_ced")
        self.check_Consumidor = QtWidgets.QCheckBox(RealizarFacturaWindow)
        self.check_Consumidor.setGeometry(QtCore.QRect(310, 20, 121, 17))
        self.check_Consumidor.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.check_Consumidor.setObjectName("check_Consumidor")
        self.lb_nomCli = QtWidgets.QLabel(RealizarFacturaWindow)
        self.lb_nomCli.setGeometry(QtCore.QRect(30, 50, 61, 16))
        self.lb_nomCli.setObjectName("lb_nomCli")
        self.le_nom = QtWidgets.QLineEdit(RealizarFacturaWindow)
        self.le_nom.setGeometry(QtCore.QRect(100, 50, 181, 20))
        self.le_nom.setObjectName("le_nom")
        self.lb_apeCli = QtWidgets.QLabel(RealizarFacturaWindow)
        self.lb_apeCli.setGeometry(QtCore.QRect(30, 80, 61, 21))
        self.lb_apeCli.setObjectName("lb_apeCli")
        self.le_ape = QtWidgets.QLineEdit(RealizarFacturaWindow)
        self.le_ape.setGeometry(QtCore.QRect(100, 80, 181, 20))
        self.le_ape.setObjectName("le_ape")
        self.le_tel = QtWidgets.QLineEdit(RealizarFacturaWindow)
        self.le_tel.setGeometry(QtCore.QRect(100, 110, 181, 20))
        self.le_tel.setObjectName("le_tel")
        self.le_em = QtWidgets.QLineEdit(RealizarFacturaWindow)
        self.le_em.setGeometry(QtCore.QRect(100, 140, 181, 20))
        self.le_em.setObjectName("le_em")
        self.le_dir = QtWidgets.QLineEdit(RealizarFacturaWindow)
        self.le_dir.setGeometry(QtCore.QRect(100, 170, 181, 20))
        self.le_dir.setObjectName("le_dir")
        self.lb_telCli = QtWidgets.QLabel(RealizarFacturaWindow)
        self.lb_telCli.setGeometry(QtCore.QRect(30, 110, 71, 21))
        self.lb_telCli.setObjectName("lb_telCli")
        self.lb_emCli = QtWidgets.QLabel(RealizarFacturaWindow)
        self.lb_emCli.setGeometry(QtCore.QRect(50, 140, 51, 21))
        self.lb_emCli.setObjectName("lb_emCli")
        self.lb_dirCli = QtWidgets.QLabel(RealizarFacturaWindow)
        self.lb_dirCli.setGeometry(QtCore.QRect(20, 170, 71, 21))
        self.lb_dirCli.setObjectName("lb_dirCli")
        self.lb_valT = QtWidgets.QLabel(RealizarFacturaWindow)
        self.lb_valT.setGeometry(QtCore.QRect(360, 80, 81, 16))
        self.lb_valT.setObjectName("lb_valT")
        self.lb_valT_2 = QtWidgets.QLabel(RealizarFacturaWindow)
        self.lb_valT_2.setGeometry(QtCore.QRect(450, 80, 51, 16))
        self.lb_valT_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lb_valT_2.setObjectName("lb_valT_2")
        self.lb_pagoCli = QtWidgets.QLabel(RealizarFacturaWindow)
        self.lb_pagoCli.setGeometry(QtCore.QRect(400, 110, 41, 21))
        self.lb_pagoCli.setStyleSheet("color: rgb(0, 0, 127);")
        self.lb_pagoCli.setObjectName("lb_pagoCli")
        self.le_devuel = QtWidgets.QLabel(RealizarFacturaWindow)
        self.le_devuel.setGeometry(QtCore.QRect(450, 140, 51, 16))
        self.le_devuel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_devuel.setObjectName("le_devuel")
        self.le_pago = QtWidgets.QLineEdit(RealizarFacturaWindow)
        self.le_pago.setGeometry(QtCore.QRect(450, 110, 51, 20))
        self.le_pago.setObjectName("le_pago")
        self.lb_devuel = QtWidgets.QLabel(RealizarFacturaWindow)
        self.lb_devuel.setGeometry(QtCore.QRect(370, 140, 71, 21))
        self.lb_devuel.setStyleSheet("color: rgb(255, 0, 0);")
        self.lb_devuel.setObjectName("lb_devuel")

        self.retranslateUi(RealizarFacturaWindow)
        QtCore.QMetaObject.connectSlotsByName(RealizarFacturaWindow)

    def retranslateUi(self, RealizarFacturaWindow):
        _translate = QtCore.QCoreApplication.translate
        RealizarFacturaWindow.setWindowTitle(_translate("RealizarFacturaWindow", "Datos Factura"))
        self.lb_cedCli.setText(_translate("RealizarFacturaWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Cedula</span></p></body></html>"))
        self.check_Consumidor.setText(_translate("RealizarFacturaWindow", "Consumidor Final"))
        self.lb_nomCli.setText(_translate("RealizarFacturaWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Nombre</span></p></body></html>"))
        self.lb_apeCli.setText(_translate("RealizarFacturaWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Apellido</span></p></body></html>"))
        self.lb_telCli.setText(_translate("RealizarFacturaWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Telefono</span></p></body></html>"))
        self.lb_emCli.setText(_translate("RealizarFacturaWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Email</span></p></body></html>"))
        self.lb_dirCli.setText(_translate("RealizarFacturaWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Direccion</span></p></body></html>"))
        self.lb_valT.setText(_translate("RealizarFacturaWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Valor Total</span></p></body></html>"))
        self.lb_valT_2.setText(_translate("RealizarFacturaWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lb_pagoCli.setText(_translate("RealizarFacturaWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Pago</span></p></body></html>"))
        self.le_devuel.setText(_translate("RealizarFacturaWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lb_devuel.setText(_translate("RealizarFacturaWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Devuelvo</span></p></body></html>"))

    # ! ---------------------------------------


    # ? ------ Funcionalidades Propias --------
    def open_RealizarFacturaWindow(self):
        app = QtWidgets.QApplication(sys.argv)
        RealizarFacturaWindow = QtWidgets.QWidget()
        ui = Ui_RealizarFacturaWindow()
        ui.setupUi(RealizarFacturaWindow)
        RealizarFacturaWindow.show()
        sys.exit(app.exec_())
    # ? ---------------------------------------
    
    
if __name__ == "__main__":
    realizar_factura_window = Ui_RealizarFacturaWindow()
    realizar_factura_window.open_RealizarFacturaWindow()