import peewee as pw
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtCore import Qt
from ui.ui_pesq_tomografias import Ui_PesqTomografias
from model.tomografias import Tomografias
from pesq_pacientes import PesqPacientes
from model.pacientes import Pacientes
from pesq_alunos import PesqAlunos
from model.alunos import Alunos

class PesqTomografias(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.ui = Ui_PesqTomografias()
        self.ui.setupUi(self)
        self.paciente = None
        self.aluno = None
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Id', 'Paciente', 'Aluno', 'Valor', 'Entregue'])
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

        def on_pesq_paciente():
            pesq = PesqPacientes()
            id = pesq.pesquisar()

            if id:
                self.paciente = Pacientes.get(Pacientes.id == int(id))

            if self.paciente:
                self.ui.edtPaciente.setText(self.paciente.nome)
            else:
                self.ui.edtPaciente.clear()

            self.filtrar()

        def on_limpar_paciente():
            self.paciente = None
            self.ui.edtPaciente.clear()
            self.filtrar()

        def on_pesq_aluno():
            pesq = PesqAlunos()
            id = pesq.pesquisar()

            if id:
                self.aluno = Alunos.get(Alunos.id == int(id))

            if self.aluno:
                self.ui.edtAluno.setText(self.aluno.nome)
            else:
                self.ui.edtAluno.clear()

            self.filtrar()

        def on_limpar_aluno():
            self.aluno = None
            self.ui.edtAluno.clear()
            self.filtrar()

        self.ui.btnConfirmar.clicked.connect(on_confirmar)
        self.ui.btnCancelar.clicked.connect(on_cancelar)
        self.ui.tableWidget.doubleClicked.connect(on_confirmar)
        self.ui.btnPesqPaciente.clicked.connect(on_pesq_paciente)
        self.ui.btnLimparPaciente.clicked.connect(on_limpar_paciente)
        self.ui.btnPesqAluno.clicked.connect(on_pesq_aluno)
        self.ui.btnLimparAluno.clicked.connect(on_limpar_aluno)

    def filtrar(self):
        while self.ui.tableWidget.rowCount() > 0:
            self.ui.tableWidget.removeRow(0)

        rows = (Tomografias
            .select(Tomografias.id, Tomografias.paciente.nome.alias('paciente'), Tomografias.aluno.nome.alias('aluno'), Tomografias.valor, Tomografias.data_entrega))
            
        if self.paciente:
            rows = rows.where(Tomografias.paciente == self.paciente.id)
            
        if self.aluno:
            rows = rows.where(Tomografias.aluno == self.aluno.id)

        rows = rows.join(Pacientes).switch(Tomografias).join(Alunos).dicts()

        for row in rows:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)

            item = QTableWidgetItem(str(row['id']))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 0, item)
            
            item = QTableWidgetItem(str(row['paciente']))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 1, item)
            
            item = QTableWidgetItem(str(row['aluno']))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 2, item)
            
            item = QTableWidgetItem(str(row['valor']))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 3, item)
            
            item = QTableWidgetItem(str(row['data_entrega']))
            item.setFlags(Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(rowPosition, 4, item)

    def pesquisar(self):
        self.exec_()

        if self.selected:
            row = self.ui.tableWidget.currentItem().row()
            return int(self.ui.tableWidget.item(row, 0).text())