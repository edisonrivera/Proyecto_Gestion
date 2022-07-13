from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AgregarProvWindow(object):
    # ! -------- Código autogenerado ----------
    def setupUi(self, AgregarProvWindow):
        AgregarProvWindow.setObjectName("AgregarProvWindow")
        AgregarProvWindow.resize(443, 221)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bx-body.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AgregarProvWindow.setWindowIcon(icon)
        self.button_cancelar_prov = QtWidgets.QPushButton(AgregarProvWindow)
        self.button_cancelar_prov.setGeometry(QtCore.QRect(240, 160, 121, 41))
        self.button_cancelar_prov.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/bxs-message-square-x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cancelar_prov.setIcon(icon1)
        self.button_cancelar_prov.setIconSize(QtCore.QSize(30, 30))
        self.button_cancelar_prov.setObjectName("button_cancelar_prov")
        self.le_cod_prov = QtWidgets.QLineEdit(AgregarProvWindow)
        self.le_cod_prov.setGeometry(QtCore.QRect(140, 60, 211, 20))
        self.le_cod_prov.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_cod_prov.setObjectName("le_cod_prov")
        self.lb_tel_prov = QtWidgets.QLabel(AgregarProvWindow)
        self.lb_tel_prov.setGeometry(QtCore.QRect(70, 90, 61, 16))
        self.lb_tel_prov.setObjectName("lb_tel_prov")
        self.lb_email_prov = QtWidgets.QLabel(AgregarProvWindow)
        self.lb_email_prov.setGeometry(QtCore.QRect(90, 120, 41, 16))
        self.lb_email_prov.setObjectName("lb_email_prov")
        self.le_tel_prov = QtWidgets.QLineEdit(AgregarProvWindow)
        self.le_tel_prov.setGeometry(QtCore.QRect(140, 90, 211, 20))
        self.le_tel_prov.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_tel_prov.setObjectName("le_tel_prov")
        self.le_email_prov = QtWidgets.QLineEdit(AgregarProvWindow)
        self.le_email_prov.setGeometry(QtCore.QRect(140, 120, 211, 20))
        self.le_email_prov.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_email_prov.setObjectName("le_email_prov")
        self.button_agregar_prov = QtWidgets.QPushButton(AgregarProvWindow)
        self.button_agregar_prov.setGeometry(QtCore.QRect(100, 160, 111, 41))
        self.button_agregar_prov.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/bx-check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_agregar_prov.setIcon(icon2)
        self.button_agregar_prov.setIconSize(QtCore.QSize(30, 30))
        self.button_agregar_prov.setObjectName("button_agregar_prov")
        self.lb_title_prov = QtWidgets.QLabel(AgregarProvWindow)
        self.lb_title_prov.setGeometry(QtCore.QRect(110, 10, 221, 31))
        self.lb_title_prov.setObjectName("lb_title_prov")
        self.lb_cod_prov = QtWidgets.QLabel(AgregarProvWindow)
        self.lb_cod_prov.setGeometry(QtCore.QRect(80, 60, 51, 16))
        self.lb_cod_prov.setObjectName("lb_cod_prov")

        self.retranslateUi(AgregarProvWindow)
        QtCore.QMetaObject.connectSlotsByName(AgregarProvWindow)

    def retranslateUi(self, AgregarProvWindow):
        _translate = QtCore.QCoreApplication.translate
        AgregarProvWindow.setWindowTitle(_translate("AgregarProvWindow", "Agregar Proveedor"))
        self.button_cancelar_prov.setText(_translate("AgregarProvWindow", "CANCELAR"))
        self.lb_tel_prov.setText(_translate("AgregarProvWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">TELEFONO</span></p></body></html>"))
        self.lb_email_prov.setText(_translate("AgregarProvWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">EMAIL</span></p></body></html>"))
        self.button_agregar_prov.setText(_translate("AgregarProvWindow", "AGREGAR"))
        self.lb_title_prov.setText(_translate("AgregarProvWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">AGREGAR PROVEEDOR</span></p></body></html>"))
        self.lb_cod_prov.setText(_translate("AgregarProvWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">CODIGO</span></p></body></html>"))
    # ! ---------------------------------------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgregarProvWindow = QtWidgets.QWidget()
    ui = Ui_AgregarProvWindow()
    ui.setupUi(AgregarProvWindow)
    AgregarProvWindow.show()
    sys.exit(app.exec_())