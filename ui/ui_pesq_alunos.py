from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PesqAlunos(object):
    def setupUi(self, PesqAlunos):
        PesqAlunos.setObjectName("PesqAlunos")
        PesqAlunos.resize(509, 461)
        self.verticalLayout = QtWidgets.QVBoxLayout(PesqAlunos)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(PesqAlunos)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.edtNome = QtWidgets.QLineEdit(PesqAlunos)
        self.edtNome.setObjectName("edtNome")
        self.verticalLayout.addWidget(self.edtNome)
        self.tableWidget = QtWidgets.QTableWidget(PesqAlunos)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.btnConfirmar = QtWidgets.QPushButton(PesqAlunos)
        self.btnConfirmar.setObjectName("btnConfirmar")
        self.verticalLayout.addWidget(self.btnConfirmar)
        self.btnCancelar = QtWidgets.QPushButton(PesqAlunos)
        self.btnCancelar.setObjectName("btnCancelar")
        self.verticalLayout.addWidget(self.btnCancelar)

        self.retranslateUi(PesqAlunos)
        QtCore.QMetaObject.connectSlotsByName(PesqAlunos)

    def retranslateUi(self, PesqAlunos):
        _translate = QtCore.QCoreApplication.translate
        PesqAlunos.setWindowTitle(_translate("PesqAlunos", "Dialog"))
        self.label.setText(_translate("PesqAlunos", "Nome"))
        self.btnConfirmar.setText(_translate("PesqAlunos", "&Confirmar"))
        self.btnCancelar.setText(_translate("PesqAlunos", "Cancela&r"))
