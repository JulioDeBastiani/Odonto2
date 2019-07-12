import peewee as pw
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtCore import Qt
from ui.ui_pesq_pacientes import Ui_PeqPacientes
from model.pacientes import Pacientes
from model.indicacoes import Indicacoes

class PesqPacientes(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.ui = Ui_PeqPacientes()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Id', 'Nome', 'Nascimento', 'ClinView Id', 'Indicação'])
        self.selected = False
        self.__setupEvents()
        self.filtrar()

    def __setupEvents(self):
        def on_confirmar():
            self.selected = self.ui.tableWidget.rowCount() > 0
            self.close()
        
        def on_cancelar():
            self.close()

        def on_textChanged():
            self.filtrar()

        self.ui.btnConfirmar.clicked.connect(on_confirmar)
        self.ui.btnCancelar.clicked.connect(on_cancelar)
        self.ui.tableWidget.doubleClicked.connect(on_confirmar)
        self.ui.edtNome.textChanged.connect(on_textChanged)
        self.ui.edtClinViewId.textChanged.connect(on_textChanged)
        # TODO indicacao

    def filtrar(self):
        while self.ui.tableWidget.rowCount() > 0:
            self.ui.tableWidget.removeRow(0)

        nome = str(self.ui.edtNome.text())
        clin_view_id = str(self.ui.edtClinViewId.text())

        rows = (Pacientes
            .select(Pacientes.id, Pacientes.nome, Pacientes.nascimento, Pacientes.clinview_id, Indicacoes.nome.alias('desc_indicacao'))
            .where(
                pw.fn.Upper(Pacientes.nome) % pw.fn.Upper(f'%{nome}%') if nome else True,
                pw.fn.Upper(Pacientes.clinview_id) % pw.fn.Upper(f'%{clin_view_id}%') if clin_view_id else True)
            .join(Indicacoes, pw.JOIN.LEFT_OUTER)
            .dicts())

        for row in rows:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)         
            
            item = QTableWidgetItem(str(row['id']))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 0, item)
            
            item = QTableWidgetItem(str(row['nome']))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 1, item)
            
            item = QTableWidgetItem(str(row['nascimento']))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 2, item)
            
            item = QTableWidgetItem(str(row['clinview_id']))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 3, item)
            
            item = QTableWidgetItem(str(row['desc_indicacao']))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 4, item)

    def pesquisar(self):
        self.exec_()

        if self.selected:
            row = self.ui.tableWidget.currentItem().row()
            return int(self.ui.tableWidget.item(row, 0).text())