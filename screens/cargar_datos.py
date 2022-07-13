from busqueda_producto import Ui_BusquedaProductoWindow
from PyQt5 import QtCore
from PyQt5 import QtWidgets as qtw
from fix_deprecate import suppress_qt_warnings

# * Para ejectuar desde el mismo archivo todas las 'funciones'
# * tienes que eliminar la palabra 'screens.' 
import connect_db as cdb

class show_data_table(qtw.QWidget):
    # ? ------ Funcionalidades Propias --------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_BusquedaProductoWindow()
        self.ui.setupUi(self)
        self.show_data_first()
        self.ui.button_buscar.clicked.connect(self.search_product)
        self.ui.button_ordenar.clicked.connect(self.order_products)
        self.band = True

    def show_data_first (self):
        sql_qry = "SELECT * FROM Producto"
        self.load_qry_tb(sql_qry)
        
    def search_product(self):
        if (self.ui.le_codPro.text() or self.ui.le_nomPro.text()):
            sql_qry = f"SELECT * FROM Producto WHERE cod_Pro LIKE \'%{self.ui.le_codPro.text()}%\'"
            self.load_qry_tb(sql_qry)
        else:
            qtw.QMessageBox.critical(self,"Error", "Llene al menos un campo")
        
    def order_products(self):
        if (self.band):
            order_str = "DESC"
            self.band = False
        else:
            order_str = "ASC"
            self.band = True
        sql_qry = f"SELECT * FROM Producto ORDER BY cod_Pro {order_str}"
        self.load_qry_tb(sql_qry)

    def load_qry_tb(self, sql_qry):
        data_products = cdb.show_data(sql_qry)
        tabla = self.ui.tb_busquedaProducto
        tabla.setModel(data_products)
        data_products.setHeaderData(0,QtCore.Qt.Horizontal, QtCore.QObject.tr(data_products, "CODIGO"))
        data_products.setHeaderData(1,QtCore.Qt.Horizontal, QtCore.QObject.tr(data_products, "NOMBRE"))
        data_products.setHeaderData(2,QtCore.Qt.Horizontal, QtCore.QObject.tr(data_products, "STOCK"))
        data_products.setHeaderData(3,QtCore.Qt.Horizontal, QtCore.QObject.tr(data_products, "PRECIO_UNITARIO"))
        data_products.setHeaderData(4,QtCore.Qt.Horizontal, QtCore.QObject.tr(data_products, "DESCUENTO"))
        data_products.setHeaderData(5,QtCore.Qt.Horizontal, QtCore.QObject.tr(data_products, "PROVEEDOR"))
    # ? ---------------------------------------


if __name__ == "__main__":
    suppress_qt_warnings()
    app = qtw.QApplication([])
    widget = show_data_table()
    widget.show()
    app.exec_()