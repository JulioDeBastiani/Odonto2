import peewee as pw
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtCore import Qt
from ui.ui_pesq_alunos import Ui_PesqAlunos
from model.alunos import Alunos

class PesqAlunos(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.ui = Ui_PesqAlunos()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Id', 'Nome'])
        self.selected = False
        self.__setupEvents()
        self.filtrar("")

    def __setupEvents(self):
        def on_confirmar():
            self.selected = self.ui.tableWidget.rowCount() > 0
            self.close()
        
        def on_cancelar():
            self.close()

        def on_textChanged():
            if self.ui.edtNome.text():
                self.filtrar(self.ui.edtNome.text())

        self.ui.btnConfirmar.clicked.connect(on_confirmar)
        self.ui.btnCancelar.clicked.connect(on_cancelar)
        self.ui.tableWidget.doubleClicked.connect(on_confirmar)
        self.ui.edtNome.textChanged.connect(on_textChanged)

    def filtrar(self, nome):
        while self.ui.tableWidget.rowCount() > 0:
            self.ui.tableWidget.removeRow(0)

        if nome:
            rows = Alunos.select().where(pw.fn.Upper(Alunos.nome) % pw.fn.Upper(f'%{nome}%'))
        else:
            rows = Alunos.select()

        for row in rows:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)         
            
            item = QTableWidgetItem(str(row.id))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 0, item)
            
            item = QTableWidgetItem(str(row.nome))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 1, item)

    def pesquisar(self):
        self.exec_()

        if self.selected:
            row = self.ui.tableWidget.currentItem().row()
            return int(self.ui.tableWidget.item(row, 0).text())