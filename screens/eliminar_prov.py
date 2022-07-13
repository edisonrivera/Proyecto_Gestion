from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EliminarProvWindow(object):
    # ! -------- Código autogenerado ----------
    def setupUi(self, EliminarProvWindow):
        EliminarProvWindow.setObjectName("EliminarProvWindow")
        EliminarProvWindow.resize(466, 268)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bxs-trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EliminarProvWindow.setWindowIcon(icon)
        self.lb_cod_prov = QtWidgets.QLabel(EliminarProvWindow)
        self.lb_cod_prov.setGeometry(QtCore.QRect(140, 50, 48, 16))
        self.lb_cod_prov.setObjectName("lb_cod_prov")
        self.le_cod_prov = QtWidgets.QLineEdit(EliminarProvWindow)
        self.le_cod_prov.setGeometry(QtCore.QRect(200, 50, 133, 22))
        self.le_cod_prov.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_cod_prov.setObjectName("le_cod_prov")
        self.button_cancelar_prov = QtWidgets.QPushButton(EliminarProvWindow)
        self.button_cancelar_prov.setGeometry(QtCore.QRect(260, 210, 112, 38))
        self.button_cancelar_prov.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/bxs-message-square-x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cancelar_prov.setIcon(icon1)
        self.button_cancelar_prov.setIconSize(QtCore.QSize(30, 30))
        self.button_cancelar_prov.setObjectName("button_cancelar_prov")
        self.lb_eliminar_prov = QtWidgets.QLabel(EliminarProvWindow)
        self.lb_eliminar_prov.setGeometry(QtCore.QRect(120, 10, 231, 23))
        self.lb_eliminar_prov.setObjectName("lb_eliminar_prov")
        self.button_eliminar_prov = QtWidgets.QPushButton(EliminarProvWindow)
        self.button_eliminar_prov.setGeometry(QtCore.QRect(110, 210, 111, 38))
        self.button_eliminar_prov.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.button_eliminar_prov.setIcon(icon)
        self.button_eliminar_prov.setIconSize(QtCore.QSize(30, 30))
        self.button_eliminar_prov.setObjectName("button_eliminar_prov")
        self.tb_eliminar_prov = QtWidgets.QTableWidget(EliminarProvWindow)
        self.tb_eliminar_prov.setGeometry(QtCore.QRect(80, 80, 311, 115))
        self.tb_eliminar_prov.setObjectName("tb_eliminar_prov")
        self.tb_eliminar_prov.setColumnCount(3)
        self.tb_eliminar_prov.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_eliminar_prov.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_eliminar_prov.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_eliminar_prov.setHorizontalHeaderItem(2, item)

        self.retranslateUi(EliminarProvWindow)
        QtCore.QMetaObject.connectSlotsByName(EliminarProvWindow)

    def retranslateUi(self, EliminarProvWindow):
        _translate = QtCore.QCoreApplication.translate
        EliminarProvWindow.setWindowTitle(_translate("EliminarProvWindow", "Eliminar Proveedor"))
        self.lb_cod_prov.setText(_translate("EliminarProvWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">CODIGO</span></p></body></html>"))
        self.button_cancelar_prov.setText(_translate("EliminarProvWindow", "CANCELAR"))
        self.lb_eliminar_prov.setText(_translate("EliminarProvWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">ELIMINAR PROVEEDOR</span></p></body></html>"))
        self.button_eliminar_prov.setText(_translate("EliminarProvWindow", "ELIMINAR"))
        item = self.tb_eliminar_prov.horizontalHeaderItem(0)
        item.setText(_translate("EliminarProvWindow", "CODIGO"))
        item = self.tb_eliminar_prov.horizontalHeaderItem(1)
        item.setText(_translate("EliminarProvWindow", "TELEFONO"))
        item = self.tb_eliminar_prov.horizontalHeaderItem(2)
        item.setText(_translate("EliminarProvWindow", "EMAIL"))
    # ! ---------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EliminarProvWindow = QtWidgets.QWidget()
    ui = Ui_EliminarProvWindow()
    ui.setupUi(EliminarProvWindow)
    EliminarProvWindow.show()
    sys.exit(app.exec_())
