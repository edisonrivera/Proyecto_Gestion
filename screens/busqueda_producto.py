import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# ! Esta funcionalidad se complementa con 'cargar_datos.py', 
# ! para ver los datos de la BD solo hay que ejecutar 'cargar_datos.py'

# * Para ejectuar desde el mismo archivo todas las 'funciones'
# * tienes que eliminar la palabra 'screens.' 

class Ui_BusquedaProductoWindow(object):
    # ! -------- Código autogenerado ----------
    def setupUi(self, BusquedaProductoWindow):
        BusquedaProductoWindow.setObjectName("BusquedaProductoWindow")
        BusquedaProductoWindow.resize(656, 338)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bxs-file-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BusquedaProductoWindow.setWindowIcon(icon)
        self.lb_nomPro = QtWidgets.QLabel(BusquedaProductoWindow)
        self.lb_nomPro.setGeometry(QtCore.QRect(50, 60, 71, 16))
        self.lb_nomPro.setObjectName("lb_nomPro")
        self.lb_codPro = QtWidgets.QLabel(BusquedaProductoWindow)
        self.lb_codPro.setGeometry(QtCore.QRect(60, 90, 61, 21))
        self.lb_codPro.setObjectName("lb_codPro")
        self.le_nomPro = QtWidgets.QLineEdit(BusquedaProductoWindow)
        self.le_nomPro.setGeometry(QtCore.QRect(120, 60, 141, 20))
        self.le_nomPro.setObjectName("le_nomPro")
        self.le_codPro = QtWidgets.QLineEdit(BusquedaProductoWindow)
        self.le_codPro.setGeometry(QtCore.QRect(120, 90, 141, 20))
        self.le_codPro.setObjectName("le_codPro")
        self.button_buscar = QtWidgets.QPushButton(BusquedaProductoWindow)
        self.button_buscar.setGeometry(QtCore.QRect(290, 70, 91, 31))
        self.button_buscar.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/bx-search-alt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_buscar.setIcon(icon1)
        self.button_buscar.setIconSize(QtCore.QSize(25, 25))
        self.button_buscar.setObjectName("button_buscar")
        self.button_ordenar = QtWidgets.QPushButton(BusquedaProductoWindow)
        self.button_ordenar.setGeometry(QtCore.QRect(400, 70, 91, 31))
        self.button_ordenar.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/bx-font-size.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_ordenar.setIcon(icon2)
        self.button_ordenar.setIconSize(QtCore.QSize(25, 25))
        self.button_ordenar.setObjectName("button_ordenar")
        self.tb_busquedaProducto = QtWidgets.QTableView(BusquedaProductoWindow)
        self.tb_busquedaProducto.setGeometry(QtCore.QRect(20, 130, 611, 181))
        self.tb_busquedaProducto.setObjectName("tb_busquedaProducto")
        self.label = QtWidgets.QLabel(BusquedaProductoWindow)
        self.label.setGeometry(QtCore.QRect(240, 20, 171, 21))
        self.label.setObjectName("label")

        self.retranslateUi(BusquedaProductoWindow)
        QtCore.QMetaObject.connectSlotsByName(BusquedaProductoWindow)

    def retranslateUi(self, BusquedaProductoWindow):
        _translate = QtCore.QCoreApplication.translate
        BusquedaProductoWindow.setWindowTitle(_translate("BusquedaProductoWindow", "Busqueda de Producto"))
        self.lb_nomPro.setText(_translate("BusquedaProductoWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Nombre</span></p></body></html>"))
        self.lb_codPro.setText(_translate("BusquedaProductoWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Codigo</span></p></body></html>"))
        self.button_buscar.setText(_translate("BusquedaProductoWindow", "Buscar"))
        self.button_ordenar.setText(_translate("BusquedaProductoWindow", "Ordenar"))
        self.label.setText(_translate("BusquedaProductoWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">BUSCAR PRODUCTO</span></p></body></html>"))
    # ! ---------------------------------------

    # ? ------ Funcionalidades Propias --------
    def open_busqueda_producto_window(self):
        app = QtWidgets.QApplication(sys.argv)
        BusquedaProductoWindow = QtWidgets.QWidget()
        ui = Ui_BusquedaProductoWindow()
        ui.setupUi(BusquedaProductoWindow)
        BusquedaProductoWindow.show()
        sys.exit(app.exec_())
    # ? ---------------------------------------
    
if __name__ == "__main__":
    busqueda_producto_window = Ui_BusquedaProductoWindow()
    busqueda_producto_window.open_busqueda_producto_window()