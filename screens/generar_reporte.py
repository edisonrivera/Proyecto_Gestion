# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generar_reporte.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GenerarReporteWindow(object):
    # ! -------- Código autogenerado ----------
    def setupUi(self, GenerarReporteWindow):
        GenerarReporteWindow.setObjectName("GenerarReporteWindow")
        GenerarReporteWindow.resize(341, 157)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bxs-report.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GenerarReporteWindow.setWindowIcon(icon)
        self.lb_generarReporte = QtWidgets.QLabel(GenerarReporteWindow)
        self.lb_generarReporte.setGeometry(QtCore.QRect(100, 10, 141, 21))
        self.lb_generarReporte.setObjectName("lb_generarReporte")
        self.bt_printer = QtWidgets.QPushButton(GenerarReporteWindow)
        self.bt_printer.setGeometry(QtCore.QRect(200, 70, 101, 31))
        self.bt_printer.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/bx-printer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_printer.setIcon(icon1)
        self.bt_printer.setIconSize(QtCore.QSize(25, 25))
        self.bt_printer.setObjectName("bt_printer")
        self.rb_semana = QtWidgets.QRadioButton(GenerarReporteWindow)
        self.rb_semana.setGeometry(QtCore.QRect(30, 50, 111, 17))
        self.rb_semana.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.rb_semana.setObjectName("rb_semana")
        self.rb_mes = QtWidgets.QRadioButton(GenerarReporteWindow)
        self.rb_mes.setGeometry(QtCore.QRect(30, 80, 101, 17))
        self.rb_mes.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.rb_mes.setObjectName("rb_mes")
        self.rb_trimestre = QtWidgets.QRadioButton(GenerarReporteWindow)
        self.rb_trimestre.setGeometry(QtCore.QRect(30, 110, 111, 17))
        self.rb_trimestre.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.rb_trimestre.setObjectName("rb_trimestre")

        self.retranslateUi(GenerarReporteWindow)
        QtCore.QMetaObject.connectSlotsByName(GenerarReporteWindow)

    def retranslateUi(self, GenerarReporteWindow):
        _translate = QtCore.QCoreApplication.translate
        GenerarReporteWindow.setWindowTitle(_translate("GenerarReporteWindow", "Generar Reporte"))
        self.lb_generarReporte.setText(_translate("GenerarReporteWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Generar Reporte</span></p></body></html>"))
        self.bt_printer.setText(_translate("GenerarReporteWindow", "Imprimir"))
        self.rb_semana.setText(_translate("GenerarReporteWindow", "Ultima Semana"))
        self.rb_mes.setText(_translate("GenerarReporteWindow", "Ultimo Mes"))
        self.rb_trimestre.setText(_translate("GenerarReporteWindow", "Ultimo trimestre"))
    # ! ---------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GenerarReporteWindow = QtWidgets.QWidget()
    ui = Ui_GenerarReporteWindow()
    ui.setupUi(GenerarReporteWindow)
    GenerarReporteWindow.show()
    sys.exit(app.exec_())