# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1282, 840)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.ModuloBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModuloBox.sizePolicy().hasHeightForWidth())
        self.ModuloBox.setSizePolicy(sizePolicy)
        self.ModuloBox.setObjectName("ModuloBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.ModuloBox)
        self.gridLayout_9.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_2.addWidget(self.ModuloBox)
        self.PhaseBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PhaseBox.sizePolicy().hasHeightForWidth())
        self.PhaseBox.setSizePolicy(sizePolicy)
        self.PhaseBox.setObjectName("PhaseBox")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.PhaseBox)
        self.gridLayout_10.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_2.addWidget(self.PhaseBox)
        self.RespuestaBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RespuestaBox.sizePolicy().hasHeightForWidth())
        self.RespuestaBox.setSizePolicy(sizePolicy)
        self.RespuestaBox.setObjectName("RespuestaBox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.RespuestaBox)
        self.gridLayout_11.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_2.addWidget(self.RespuestaBox)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ConfigBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConfigBox.sizePolicy().hasHeightForWidth())
        self.ConfigBox.setSizePolicy(sizePolicy)
        self.ConfigBox.setMaximumSize(QtCore.QSize(310, 16777215))
        self.ConfigBox.setObjectName("ConfigBox")
        self.gridLayout = QtWidgets.QGridLayout(self.ConfigBox)
        self.gridLayout.setObjectName("gridLayout")
        self.FontSizeLabel = QtWidgets.QLabel(self.ConfigBox)
        self.FontSizeLabel.setObjectName("FontSizeLabel")
        self.gridLayout.addWidget(self.FontSizeLabel, 2, 0, 1, 1)
        self.FontFamilyComboBox = QtWidgets.QComboBox(self.ConfigBox)
        self.FontFamilyComboBox.setObjectName("FontFamilyComboBox")
        self.gridLayout.addWidget(self.FontFamilyComboBox, 1, 1, 1, 2)
        self.FontSizeSpinbox = QtWidgets.QSpinBox(self.ConfigBox)
        self.FontSizeSpinbox.setMinimum(1)
        self.FontSizeSpinbox.setProperty("value", 10)
        self.FontSizeSpinbox.setObjectName("FontSizeSpinbox")
        self.gridLayout.addWidget(self.FontSizeSpinbox, 2, 1, 1, 2)
        self.FontFamilyLabel = QtWidgets.QLabel(self.ConfigBox)
        self.FontFamilyLabel.setObjectName("FontFamilyLabel")
        self.gridLayout.addWidget(self.FontFamilyLabel, 1, 0, 1, 1)
        self.ShowPlotGroupBox = QtWidgets.QGroupBox(self.ConfigBox)
        self.ShowPlotGroupBox.setObjectName("ShowPlotGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ShowPlotGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ModuleCheckBox = QtWidgets.QCheckBox(self.ShowPlotGroupBox)
        self.ModuleCheckBox.setChecked(True)
        self.ModuleCheckBox.setObjectName("ModuleCheckBox")
        self.horizontalLayout.addWidget(self.ModuleCheckBox)
        self.PhaseCheckBox = QtWidgets.QCheckBox(self.ShowPlotGroupBox)
        self.PhaseCheckBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.PhaseCheckBox.setChecked(True)
        self.PhaseCheckBox.setObjectName("PhaseCheckBox")
        self.horizontalLayout.addWidget(self.PhaseCheckBox)
        self.ResponseCheckBox = QtWidgets.QCheckBox(self.ShowPlotGroupBox)
        self.ResponseCheckBox.setChecked(True)
        self.ResponseCheckBox.setObjectName("ResponseCheckBox")
        self.horizontalLayout.addWidget(self.ResponseCheckBox)
        self.gridLayout.addWidget(self.ShowPlotGroupBox, 0, 0, 1, 3)
        self.verticalLayout.addWidget(self.ConfigBox)
        self.TracesBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TracesBox.sizePolicy().hasHeightForWidth())
        self.TracesBox.setSizePolicy(sizePolicy)
        self.TracesBox.setMaximumSize(QtCore.QSize(310, 16777215))
        self.TracesBox.setObjectName("TracesBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.TracesBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.TracesListBox = QtWidgets.QListWidget(self.TracesBox)
        self.TracesListBox.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.TracesListBox.setObjectName("TracesListBox")
        self.gridLayout_7.addWidget(self.TracesListBox, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.TracesBox)
        self.ButtonsBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonsBox.sizePolicy().hasHeightForWidth())
        self.ButtonsBox.setSizePolicy(sizePolicy)
        self.ButtonsBox.setMaximumSize(QtCore.QSize(310, 16777215))
        self.ButtonsBox.setObjectName("ButtonsBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ButtonsBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.EntradaDeDatosBox = QtWidgets.QGroupBox(self.ButtonsBox)
        self.EntradaDeDatosBox.setTitle("")
        self.EntradaDeDatosBox.setObjectName("EntradaDeDatosBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.EntradaDeDatosBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.TransfFunctButton = QtWidgets.QPushButton(self.EntradaDeDatosBox)
        self.TransfFunctButton.setObjectName("TransfFunctButton")
        self.gridLayout_6.addWidget(self.TransfFunctButton, 0, 0, 1, 1)
        self.PolosYCerosButton = QtWidgets.QPushButton(self.EntradaDeDatosBox)
        self.PolosYCerosButton.setObjectName("PolosYCerosButton")
        self.gridLayout_6.addWidget(self.PolosYCerosButton, 0, 1, 1, 1)
        self.RespuestaButton = QtWidgets.QPushButton(self.EntradaDeDatosBox)
        self.RespuestaButton.setObjectName("RespuestaButton")
        self.gridLayout_6.addWidget(self.RespuestaButton, 1, 0, 1, 2)
        self.AddTraceButton = QtWidgets.QPushButton(self.EntradaDeDatosBox)
        self.AddTraceButton.setObjectName("AddTraceButton")
        self.gridLayout_6.addWidget(self.AddTraceButton, 2, 0, 1, 2)
        self.DeleteTraceButton = QtWidgets.QPushButton(self.EntradaDeDatosBox)
        self.DeleteTraceButton.setObjectName("DeleteTraceButton")
        self.gridLayout_6.addWidget(self.DeleteTraceButton, 3, 0, 1, 2)
        self.PlotButton = QtWidgets.QPushButton(self.EntradaDeDatosBox)
        self.PlotButton.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.PlotButton.setFont(font)
        self.PlotButton.setObjectName("PlotButton")
        self.gridLayout_6.addWidget(self.PlotButton, 4, 0, 1, 2)
        self.gridLayout_3.addWidget(self.EntradaDeDatosBox, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.ButtonsBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.ModuleCheckBox.toggled['bool'].connect(self.ModuloBox.setVisible) # type: ignore
        self.PhaseCheckBox.toggled['bool'].connect(self.PhaseBox.setVisible) # type: ignore
        self.ResponseCheckBox.toggled['bool'].connect(self.RespuestaBox.setVisible) # type: ignore
        self.PlotButton.clicked.connect(MainWindow.Plot) # type: ignore
        self.TracesListBox.itemDoubleClicked['QListWidgetItem*'].connect(MainWindow.ModTrace) # type: ignore
        self.DeleteTraceButton.clicked.connect(MainWindow.deleteTraceEvent) # type: ignore
        self.AddTraceButton.clicked.connect(MainWindow.addTraceEvent) # type: ignore
        self.FontSizeSpinbox.valueChanged['int'].connect(MainWindow.updateFontSize) # type: ignore
        self.FontFamilyComboBox.currentTextChanged['QString'].connect(MainWindow.updateFontFamily) # type: ignore
        self.PolosYCerosButton.clicked.connect(MainWindow.showPolesAndZeros) # type: ignore
        self.TransfFunctButton.clicked.connect(MainWindow.addTransferFuction) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plot Tool - Grupo 4"))
        self.ModuloBox.setTitle(_translate("MainWindow", "Módulo"))
        self.PhaseBox.setTitle(_translate("MainWindow", "Fase"))
        self.RespuestaBox.setTitle(_translate("MainWindow", "Señal"))
        self.ConfigBox.setTitle(_translate("MainWindow", "Configuracion"))
        self.FontSizeLabel.setText(_translate("MainWindow", "Tamaño de fuente"))
        self.FontFamilyLabel.setText(_translate("MainWindow", "Familia de fuente"))
        self.ShowPlotGroupBox.setTitle(_translate("MainWindow", "Mostrar graficos:"))
        self.ModuleCheckBox.setText(_translate("MainWindow", "Módulo"))
        self.PhaseCheckBox.setText(_translate("MainWindow", "Fase"))
        self.ResponseCheckBox.setText(_translate("MainWindow", "Señal"))
        self.TracesBox.setTitle(_translate("MainWindow", "Curvas"))
        self.ButtonsBox.setTitle(_translate("MainWindow", "Cargar Datos"))
        self.TransfFunctButton.setText(_translate("MainWindow", "H(s)"))
        self.PolosYCerosButton.setText(_translate("MainWindow", "Polos y Ceros"))
        self.RespuestaButton.setText(_translate("MainWindow", "Respuesta"))
        self.AddTraceButton.setText(_translate("MainWindow", "Añadir Mediciones"))
        self.DeleteTraceButton.setText(_translate("MainWindow", "Quitar Curva"))
        self.PlotButton.setText(_translate("MainWindow", "Graficar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
