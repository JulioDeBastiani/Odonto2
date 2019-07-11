from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PesqIndicacoes(object):
    def setupUi(self, PesqIndicacoes):
        PesqIndicacoes.setObjectName("PesqIndicacoes")
        PesqIndicacoes.resize(551, 461)
        self.verticalLayout = QtWidgets.QVBoxLayout(PesqIndicacoes)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(PesqIndicacoes)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.edtNome = QtWidgets.QLineEdit(PesqIndicacoes)
        self.edtNome.setObjectName("edtNome")
        self.verticalLayout.addWidget(self.edtNome)
        self.tableWidget = QtWidgets.QTableWidget(PesqIndicacoes)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.btnConfirmar = QtWidgets.QPushButton(PesqIndicacoes)
        self.btnConfirmar.setObjectName("btnConfirmar")
        self.verticalLayout.addWidget(self.btnConfirmar)
        self.btnCancelar = QtWidgets.QPushButton(PesqIndicacoes)
        self.btnCancelar.setObjectName("btnCancelar")
        self.verticalLayout.addWidget(self.btnCancelar)

        self.retranslateUi(PesqIndicacoes)
        QtCore.QMetaObject.connectSlotsByName(PesqIndicacoes)

    def retranslateUi(self, PesqIndicacoes):
        _translate = QtCore.QCoreApplication.translate
        PesqIndicacoes.setWindowTitle(_translate("PesqIndicacoes", "Dialog"))
        self.label.setText(_translate("PesqIndicacoes", "Nome"))
        self.btnConfirmar.setText(_translate("PesqIndicacoes", "&Confirmar"))
        self.btnCancelar.setText(_translate("PesqIndicacoes", "Cancela&r"))
