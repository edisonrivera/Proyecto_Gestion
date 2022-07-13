from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VerInventarioWindow(object):

    # ! -------- Código autogenerado ----------
    def setupUi(self, VerInventarioWindow):
        VerInventarioWindow.setObjectName("VerInventarioWindow")
        VerInventarioWindow.resize(565, 401)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bxs-data.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VerInventarioWindow.setWindowIcon(icon)
        self.lb_inventario = QtWidgets.QLabel(VerInventarioWindow)
        self.lb_inventario.setGeometry(QtCore.QRect(240, 20, 101, 16))
        self.lb_inventario.setObjectName("lb_inventario")
        self.tb_inventario = QtWidgets.QTableView(VerInventarioWindow)
        self.tb_inventario.setGeometry(QtCore.QRect(20, 50, 521, 301))
        self.tb_inventario.setObjectName("tb_inventario")
        self.lb_canProductos = QtWidgets.QLabel(VerInventarioWindow)
        self.lb_canProductos.setGeometry(QtCore.QRect(30, 370, 91, 16))
        self.lb_canProductos.setObjectName("lb_canProductos")
        self.lb_numero = QtWidgets.QLabel(VerInventarioWindow)
        self.lb_numero.setGeometry(QtCore.QRect(130, 370, 21, 16))
        self.lb_numero.setObjectName("lb_numero")

        self.retranslateUi(VerInventarioWindow)
        QtCore.QMetaObject.connectSlotsByName(VerInventarioWindow)

    def retranslateUi(self, VerInventarioWindow):
        _translate = QtCore.QCoreApplication.translate
        VerInventarioWindow.setWindowTitle(_translate("VerInventarioWindow", "Ver Inventario"))
        self.lb_inventario.setText(_translate("VerInventarioWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">INVENTARIO</span></p></body></html>"))
        self.lb_canProductos.setText(_translate("VerInventarioWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">N# Productos</span></p></body></html>"))
        self.lb_numero.setText(_translate("VerInventarioWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">#</span></p></body></html>"))
    # ! ---------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VerInventarioWindow = QtWidgets.QWidget()
    ui = Ui_VerInventarioWindow()
    ui.setupUi(VerInventarioWindow)
    VerInventarioWindow.show()
    sys.exit(app.exec_())
