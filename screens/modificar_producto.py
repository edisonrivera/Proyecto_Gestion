from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModificarProductoWindow(object):
    # ! -------- Código autogenerado ----------
    def setupUi(self, ModificarProductoWindow):
        ModificarProductoWindow.setObjectName("ModificarProductoWindow")
        ModificarProductoWindow.resize(513, 306)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bxs-notepad.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ModificarProductoWindow.setWindowIcon(icon)
        self.lb_nomMod = QtWidgets.QLabel(ModificarProductoWindow)
        self.lb_nomMod.setGeometry(QtCore.QRect(110, 90, 51, 16))
        self.lb_nomMod.setObjectName("lb_nomMod")
        self.button_AgregarMod = QtWidgets.QPushButton(ModificarProductoWindow)
        self.button_AgregarMod.setGeometry(QtCore.QRect(140, 250, 131, 41))
        self.button_AgregarMod.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/bx-check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_AgregarMod.setIcon(icon1)
        self.button_AgregarMod.setIconSize(QtCore.QSize(30, 30))
        self.button_AgregarMod.setObjectName("button_AgregarMod")
        self.le_codMod = QtWidgets.QLineEdit(ModificarProductoWindow)
        self.le_codMod.setGeometry(QtCore.QRect(170, 60, 211, 20))
        self.le_codMod.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_codMod.setObjectName("le_codMod")
        self.le_nomComMod = QtWidgets.QLineEdit(ModificarProductoWindow)
        self.le_nomComMod.setGeometry(QtCore.QRect(170, 90, 211, 20))
        self.le_nomComMod.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_nomComMod.setObjectName("le_nomComMod")
        self.lb_provMod = QtWidgets.QLabel(ModificarProductoWindow)
        self.lb_provMod.setGeometry(QtCore.QRect(80, 210, 81, 16))
        self.lb_provMod.setObjectName("lb_provMod")
        self.lb_stoMod = QtWidgets.QLabel(ModificarProductoWindow)
        self.lb_stoMod.setGeometry(QtCore.QRect(110, 150, 41, 16))
        self.lb_stoMod.setObjectName("lb_stoMod")
        self.le_preUniComMod = QtWidgets.QLineEdit(ModificarProductoWindow)
        self.le_preUniComMod.setGeometry(QtCore.QRect(170, 120, 211, 20))
        self.le_preUniComMod.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_preUniComMod.setObjectName("le_preUniComMod")
        self.le_stoMod = QtWidgets.QLineEdit(ModificarProductoWindow)
        self.le_stoMod.setGeometry(QtCore.QRect(170, 150, 211, 20))
        self.le_stoMod.setObjectName("le_stoMod")
        self.lb_descMod = QtWidgets.QLabel(ModificarProductoWindow)
        self.lb_descMod.setGeometry(QtCore.QRect(90, 180, 81, 16))
        self.lb_descMod.setObjectName("lb_descMod")
        self.lb_titleProduct = QtWidgets.QLabel(ModificarProductoWindow)
        self.lb_titleProduct.setGeometry(QtCore.QRect(150, 10, 231, 31))
        self.lb_titleProduct.setObjectName("lb_titleProduct")
        self.button_CancelarMod = QtWidgets.QPushButton(ModificarProductoWindow)
        self.button_CancelarMod.setGeometry(QtCore.QRect(280, 250, 121, 41))
        self.button_CancelarMod.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/bxs-message-square-x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_CancelarMod.setIcon(icon2)
        self.button_CancelarMod.setIconSize(QtCore.QSize(30, 30))
        self.button_CancelarMod.setObjectName("button_CancelarMod")
        self.le_prvMod = QtWidgets.QLineEdit(ModificarProductoWindow)
        self.le_prvMod.setGeometry(QtCore.QRect(170, 210, 211, 20))
        self.le_prvMod.setObjectName("le_prvMod")
        self.lb_preUniMod = QtWidgets.QLabel(ModificarProductoWindow)
        self.lb_preUniMod.setGeometry(QtCore.QRect(50, 120, 121, 16))
        self.lb_preUniMod.setObjectName("lb_preUniMod")
        self.le_desMod = QtWidgets.QLineEdit(ModificarProductoWindow)
        self.le_desMod.setGeometry(QtCore.QRect(170, 180, 211, 20))
        self.le_desMod.setObjectName("le_desMod")
        self.lb_codMod = QtWidgets.QLabel(ModificarProductoWindow)
        self.lb_codMod.setGeometry(QtCore.QRect(110, 60, 51, 16))
        self.lb_codMod.setObjectName("lb_codMod")

        self.retranslateUi(ModificarProductoWindow)
        QtCore.QMetaObject.connectSlotsByName(ModificarProductoWindow)

    def retranslateUi(self, ModificarProductoWindow):
        _translate = QtCore.QCoreApplication.translate
        ModificarProductoWindow.setWindowTitle(_translate("ModificarProductoWindow", "Modificar Producto"))
        self.lb_nomMod.setText(_translate("ModificarProductoWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">NOMBRE</span></p></body></html>"))
        self.button_AgregarMod.setText(_translate("ModificarProductoWindow", "MODIFICAR"))
        self.lb_provMod.setText(_translate("ModificarProductoWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">PROVEEDOR</span></p></body></html>"))
        self.lb_stoMod.setText(_translate("ModificarProductoWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">STOCK</span></p></body></html>"))
        self.lb_descMod.setText(_translate("ModificarProductoWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">DESCUENTO</span></p></body></html>"))
        self.lb_titleProduct.setText(_translate("ModificarProductoWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">MODIFICAR PRODUCTO</span></p></body></html>"))
        self.button_CancelarMod.setText(_translate("ModificarProductoWindow", "CANCELAR"))
        self.lb_preUniMod.setText(_translate("ModificarProductoWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">PRECIO UNITARIO</span></p></body></html>"))
        self.lb_codMod.setText(_translate("ModificarProductoWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">CODIGO</span></p></body></html>"))
    # ! ---------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModificarProductoWindow = QtWidgets.QWidget()
    ui = Ui_ModificarProductoWindow()
    ui.setupUi(ModificarProductoWindow)
    ModificarProductoWindow.show()
    sys.exit(app.exec_())