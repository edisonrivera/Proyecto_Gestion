from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModificarProvWindow(object):
    # ! -------- Código autogenerado ----------
    def setupUi(self, ModificarProvWindow):
        ModificarProvWindow.setObjectName("ModificarProvWindow")
        ModificarProvWindow.resize(422, 229)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bxs-notepad.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ModificarProvWindow.setWindowIcon(icon)
        self.lb_tel_mod_prov = QtWidgets.QLabel(ModificarProvWindow)
        self.lb_tel_mod_prov.setGeometry(QtCore.QRect(50, 100, 61, 16))
        self.lb_tel_mod_prov.setObjectName("lb_tel_mod_prov")
        self.le_cod_mod_prov = QtWidgets.QLineEdit(ModificarProvWindow)
        self.le_cod_mod_prov.setGeometry(QtCore.QRect(120, 70, 211, 20))
        self.le_cod_mod_prov.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_cod_mod_prov.setObjectName("le_cod_mod_prov")
        self.lb_title_mod_prov = QtWidgets.QLabel(ModificarProvWindow)
        self.lb_title_mod_prov.setGeometry(QtCore.QRect(90, 20, 251, 31))
        self.lb_title_mod_prov.setObjectName("lb_title_mod_prov")
        self.lb_email_mod_prov = QtWidgets.QLabel(ModificarProvWindow)
        self.lb_email_mod_prov.setGeometry(QtCore.QRect(70, 130, 41, 16))
        self.lb_email_mod_prov.setObjectName("lb_email_mod_prov")
        self.le_email_mod_prov = QtWidgets.QLineEdit(ModificarProvWindow)
        self.le_email_mod_prov.setGeometry(QtCore.QRect(120, 130, 211, 20))
        self.le_email_mod_prov.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_email_mod_prov.setObjectName("le_email_mod_prov")
        self.button_modificar_prov = QtWidgets.QPushButton(ModificarProvWindow)
        self.button_modificar_prov.setGeometry(QtCore.QRect(80, 170, 131, 41))
        self.button_modificar_prov.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/bx-check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_modificar_prov.setIcon(icon1)
        self.button_modificar_prov.setIconSize(QtCore.QSize(30, 30))
        self.button_modificar_prov.setObjectName("button_modificar_prov")
        self.lb_cod_mod_prov = QtWidgets.QLabel(ModificarProvWindow)
        self.lb_cod_mod_prov.setGeometry(QtCore.QRect(60, 70, 51, 16))
        self.lb_cod_mod_prov.setObjectName("lb_cod_mod_prov")
        self.button_cancelar_mod_prov = QtWidgets.QPushButton(ModificarProvWindow)
        self.button_cancelar_mod_prov.setGeometry(QtCore.QRect(240, 170, 121, 41))
        self.button_cancelar_mod_prov.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/bxs-message-square-x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cancelar_mod_prov.setIcon(icon2)
        self.button_cancelar_mod_prov.setIconSize(QtCore.QSize(30, 30))
        self.button_cancelar_mod_prov.setObjectName("button_cancelar_mod_prov")
        self.le_tel_mod_prov = QtWidgets.QLineEdit(ModificarProvWindow)
        self.le_tel_mod_prov.setGeometry(QtCore.QRect(120, 100, 211, 20))
        self.le_tel_mod_prov.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_tel_mod_prov.setObjectName("le_tel_mod_prov")

        self.retranslateUi(ModificarProvWindow)
        QtCore.QMetaObject.connectSlotsByName(ModificarProvWindow)

    def retranslateUi(self, ModificarProvWindow):
        _translate = QtCore.QCoreApplication.translate
        ModificarProvWindow.setWindowTitle(_translate("ModificarProvWindow", "Modificar Producto"))
        self.lb_tel_mod_prov.setText(_translate("ModificarProvWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">TELEFONO</span></p></body></html>"))
        self.lb_title_mod_prov.setText(_translate("ModificarProvWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">MODIFICAR PROVEEDOR</span></p></body></html>"))
        self.lb_email_mod_prov.setText(_translate("ModificarProvWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">EMAIL</span></p></body></html>"))
        self.button_modificar_prov.setText(_translate("ModificarProvWindow", "MODIFICAR"))
        self.lb_cod_mod_prov.setText(_translate("ModificarProvWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">CODIGO</span></p></body></html>"))
        self.button_cancelar_mod_prov.setText(_translate("ModificarProvWindow", "CANCELAR"))
    # ! ---------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModificarProvWindow = QtWidgets.QWidget()
    ui = Ui_ModificarProvWindow()
    ui.setupUi(ModificarProvWindow)
    ModificarProvWindow.show()
    sys.exit(app.exec_())