from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# * Para ejectuar desde el mismo archivo todas las 'funciones'
# * tienes que eliminar la palabra 'screens.' 
import screens.connect_db as cdb


class Ui_AddProductWindow(object):
    # ! -------- Código autogenerado ----------
    def setupUi(self, AddProductWindow):
        AddProductWindow.setObjectName("AddProductWindow")
        AddProductWindow.resize(567, 319)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bx-cart-add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddProductWindow.setWindowIcon(icon)
        self.lb_titleProduct = QtWidgets.QLabel(AddProductWindow)
        self.lb_titleProduct.setGeometry(QtCore.QRect(200, 20, 211, 31))
        self.lb_titleProduct.setObjectName("lb_titleProduct")
        self.lb_cod = QtWidgets.QLabel(AddProductWindow)
        self.lb_cod.setGeometry(QtCore.QRect(140, 70, 51, 16))
        self.lb_cod.setObjectName("lb_cod")
        self.lb_nom = QtWidgets.QLabel(AddProductWindow)
        self.lb_nom.setGeometry(QtCore.QRect(140, 100, 51, 16))
        self.lb_nom.setObjectName("lb_nom")
        self.lb_preUni = QtWidgets.QLabel(AddProductWindow)
        self.lb_preUni.setGeometry(QtCore.QRect(80, 130, 121, 16))
        self.lb_preUni.setObjectName("lb_preUni")
        self.lb_sto = QtWidgets.QLabel(AddProductWindow)
        self.lb_sto.setGeometry(QtCore.QRect(150, 160, 41, 16))
        self.lb_sto.setObjectName("lb_sto")
        self.lb_prov = QtWidgets.QLabel(AddProductWindow)
        self.lb_prov.setGeometry(QtCore.QRect(110, 220, 81, 16))
        self.lb_prov.setObjectName("lb_prov")
        self.le_cod = QtWidgets.QLineEdit(AddProductWindow)
        self.le_cod.setGeometry(QtCore.QRect(200, 70, 211, 20))
        self.le_cod.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_cod.setObjectName("le_cod")
        self.le_nomCom = QtWidgets.QLineEdit(AddProductWindow)
        self.le_nomCom.setGeometry(QtCore.QRect(200, 100, 211, 20))
        self.le_nomCom.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_nomCom.setObjectName("le_nomCom")
        self.le_preUniCom = QtWidgets.QLineEdit(AddProductWindow)
        self.le_preUniCom.setGeometry(QtCore.QRect(200, 130, 211, 20))
        self.le_preUniCom.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.le_preUniCom.setObjectName("le_preUniCom")
        self.le_sto = QtWidgets.QLineEdit(AddProductWindow)
        self.le_sto.setGeometry(QtCore.QRect(200, 160, 211, 20))
        self.le_sto.setObjectName("le_sto")
        self.le_des = QtWidgets.QLineEdit(AddProductWindow)
        self.le_des.setGeometry(QtCore.QRect(200, 190, 211, 20))
        self.le_des.setObjectName("le_des")
        self.button_Agregar = QtWidgets.QPushButton(AddProductWindow)
        self.button_Agregar.setGeometry(QtCore.QRect(170, 260, 111, 41))
        self.button_Agregar.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/bx-check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_Agregar.setIcon(icon1)
        self.button_Agregar.setIconSize(QtCore.QSize(30, 30))
        self.button_Agregar.setObjectName("button_Agregar")
        self.button_Cancelar = QtWidgets.QPushButton(AddProductWindow)
        self.button_Cancelar.setGeometry(QtCore.QRect(310, 260, 121, 41))
        self.button_Cancelar.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/bxs-message-square-x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_Cancelar.setIcon(icon2)
        self.button_Cancelar.setIconSize(QtCore.QSize(30, 30))
        self.button_Cancelar.setObjectName("button_Cancelar")
        self.lb_sto_2 = QtWidgets.QLabel(AddProductWindow)
        self.lb_sto_2.setGeometry(QtCore.QRect(120, 190, 81, 16))
        self.lb_sto_2.setObjectName("lb_sto_2")
        self.le_prv = QtWidgets.QLineEdit(AddProductWindow)
        self.le_prv.setGeometry(QtCore.QRect(200, 220, 211, 20))
        self.le_prv.setObjectName("le_prv")

        self.retranslateUi(AddProductWindow)
        QtCore.QMetaObject.connectSlotsByName(AddProductWindow)

    def retranslateUi(self, AddProductWindow):
        _translate = QtCore.QCoreApplication.translate
        AddProductWindow.setWindowTitle(_translate("AddProductWindow", "Agregar Producto"))
        self.lb_titleProduct.setText(_translate("AddProductWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">AGREGAR PRODUCTO</span></p></body></html>"))
        self.lb_cod.setText(_translate("AddProductWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">CODIGO</span></p></body></html>"))
        self.lb_nom.setText(_translate("AddProductWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">NOMBRE</span></p></body></html>"))
        self.lb_preUni.setText(_translate("AddProductWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">PRECIO UNITARIO</span></p></body></html>"))
        self.lb_sto.setText(_translate("AddProductWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">STOCK</span></p></body></html>"))
        self.lb_prov.setText(_translate("AddProductWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">PROVEEDOR</span></p></body></html>"))
        self.button_Agregar.setText(_translate("AddProductWindow", "AGREGAR"))
        self.button_Cancelar.setText(_translate("AddProductWindow", "CANCELAR"))
        self.lb_sto_2.setText(_translate("AddProductWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">DESCUENTO</span></p></body></html>"))

    # ! ---------------------------------------


    # ? ------ Funcionalidades Propias --------
    def guardar_datos(self):
        qry = """INSERT INTO Producto(cod_Pro, nom_Pro, sto_Pro, precUni_Pro, desc_Pro, FKcod_Prv)
        VALUES (?,?,?,?,?,?)"""
        cod = self.ui.le_cod.text()
        nom_Com = self.ui.le_nomCom.text()
        stock = int(self.ui.le_sto.text())
        prec_Uni = float(self.ui.le_preUniCom.text())
        descuento = int(self.ui.le_des.text())
        prv = self.ui.le_prv.text()
        datos = [cod,nom_Com, stock, prec_Uni, descuento,prv]

        cdb.request_query(qry, datos)
            
    def open_AddProductWindow(self):
        app = QtWidgets.QApplication(sys.argv)
        AddProductWindow = QtWidgets.QWidget()
        self.ui = Ui_AddProductWindow()
        self.ui.setupUi(AddProductWindow)
        self.ui.button_Agregar.clicked.connect(self.guardar_datos)
        AddProductWindow.show()
        sys.exit(app.exec_())
    # ? ---------------------------------------

if __name__ == "__main__":
    window = Ui_AddProductWindow()
    window.open_AddProductWindow()