from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BuscarProvWindow(object):
    # ! -------- Código autogenerado ----------
    def setupUi(self, BuscarProvWindow):
        BuscarProvWindow.setObjectName("BuscarProvWindow")
        BuscarProvWindow.resize(514, 322)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bx-search-alt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BuscarProvWindow.setWindowIcon(icon)
        self.button_buscar_prov = QtWidgets.QPushButton(BuscarProvWindow)
        self.button_buscar_prov.setGeometry(QtCore.QRect(260, 60, 91, 31))
        self.button_buscar_prov.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.button_buscar_prov.setIcon(icon)
        self.button_buscar_prov.setIconSize(QtCore.QSize(25, 25))
        self.button_buscar_prov.setObjectName("button_buscar_prov")
        self.button_ordenar_prov = QtWidgets.QPushButton(BuscarProvWindow)
        self.button_ordenar_prov.setGeometry(QtCore.QRect(370, 60, 91, 31))
        self.button_ordenar_prov.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/bx-font-size.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_ordenar_prov.setIcon(icon1)
        self.button_ordenar_prov.setIconSize(QtCore.QSize(25, 25))
        self.button_ordenar_prov.setObjectName("button_ordenar_prov")
        self.lb_cod_prov = QtWidgets.QLabel(BuscarProvWindow)
        self.lb_cod_prov.setGeometry(QtCore.QRect(30, 70, 61, 21))
        self.lb_cod_prov.setObjectName("lb_cod_prov")
        self.tb_busqueda_prov = QtWidgets.QTableView(BuscarProvWindow)
        self.tb_busqueda_prov.setGeometry(QtCore.QRect(80, 110, 351, 181))
        self.tb_busqueda_prov.setObjectName("tb_busqueda_prov")
        self.le_cod_pro = QtWidgets.QLineEdit(BuscarProvWindow)
        self.le_cod_pro.setGeometry(QtCore.QRect(90, 70, 141, 20))
        self.le_cod_pro.setObjectName("le_cod_pro")
        self.lb_buscar_prov = QtWidgets.QLabel(BuscarProvWindow)
        self.lb_buscar_prov.setGeometry(QtCore.QRect(170, 20, 181, 21))
        self.lb_buscar_prov.setObjectName("lb_buscar_prov")

        self.retranslateUi(BuscarProvWindow)
        QtCore.QMetaObject.connectSlotsByName(BuscarProvWindow)

    def retranslateUi(self, BuscarProvWindow):
        _translate = QtCore.QCoreApplication.translate
        BuscarProvWindow.setWindowTitle(_translate("BuscarProvWindow", "Buscar Proveedor"))
        self.button_buscar_prov.setText(_translate("BuscarProvWindow", "Buscar"))
        self.button_ordenar_prov.setText(_translate("BuscarProvWindow", "Ordenar"))
        self.lb_cod_prov.setText(_translate("BuscarProvWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Codigo</span></p></body></html>"))
        self.lb_buscar_prov.setText(_translate("BuscarProvWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">BUSCAR PROVEEDOR</span></p></body></html>"))
    # ! ---------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BuscarProvWindow = QtWidgets.QWidget()
    ui = Ui_BuscarProvWindow()
    ui.setupUi(BuscarProvWindow)
    BuscarProvWindow.show()
    sys.exit(app.exec_())