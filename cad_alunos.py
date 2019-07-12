import peewee as pw
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from ui.ui_cad_alunos import Ui_CadAlunos
from model.alunos import Alunos
from pesq_alunos import PesqAlunos

class CadAlunos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.aluno = None
        self.ui = Ui_CadAlunos()
        self.ui.setupUi(self)
        self.__setupEvents()
        self.ui.edtId.setText(str(self.get_next_id()))

    def __setupEvents(self):
        def on_novo():
            self.ui.edtId.setText(str(self.get_next_id()))
            self.ui.edtNome.clear()
            self.ui.set_mode(True)

        def on_salvar():
            if not self.ui.edtNome.text():
                self.alert("Preencha o nome")
                return

            try:
                if not self.aluno:
                    self.aluno = Alunos.create(nome=str(self.ui.edtNome.text()))
                else:
                    self.aluno.nome = str(self.ui.edtNome.text())
                    self.aluno.save()
            except Exception as e:
                self.alert(str(e))
                return

            self.ui.set_mode(False)
            self.ui.edtId.setText(str(self.get_next_id()))
            self.ui.edtNome.clear()
            self.aluno = None

        def on_pesquisar():
            pesq = PesqAlunos()
            id = pesq.pesquisar()

            if id:
                self.aluno = Alunos.get(Alunos.id == int(id))

            if self.aluno:
                self.ui.edtId.setText(str(self.aluno.id))
                self.ui.edtNome.setText(self.aluno.nome)
                self.ui.set_mode(True)

        def on_remover():
            if self.aluno:
                self.aluno.delete_instance()
            
            self.aluno = None
            self.ui.edtId.setText(str(self.get_next_id()))
            self.ui.edtNome.clear()
            self.ui.set_mode(False)

        def on_id_editing_finished():
            if (not self.ui.edtId.text()):
                return

            try:
                self.aluno = Alunos.get(Alunos.id == int(self.ui.edtId.text()))
            except:
                pass

            if self.aluno:
                self.ui.edtNome.setText(self.aluno.nome)
                self.ui.set_mode(True)

        def on_sair():
            self.close()

        self.ui.btnNovo.clicked.connect(on_novo)
        self.ui.btnSalvar.clicked.connect(on_salvar)
        self.ui.btnPesquisar.clicked.connect(on_pesquisar)
        self.ui.btnRemover.clicked.connect(on_remover)
        self.ui.btnSair.clicked.connect(on_sair)
        self.ui.edtId.editingFinished.connect(on_id_editing_finished)

    def get_next_id(self):
        mid = Alunos.select(pw.fn.Max(Alunos.id)).scalar()
        return (mid if mid else 0) + 1

    def alert(self, message):
        alertd = QMessageBox()
        alertd.setText(message)
        alertd.exec_()

    def keyPressEvent(self, event):
        if not event.isAutoRepeat():
            if event.key() == Qt.Key_Escape:
                if not self.ui.edtId.isEnabled():
                    self.aluno = None
                    self.ui.edtId.setText(str(self.get_next_id()))
                    self.ui.edtNome.clear()
                    self.ui.set_mode(False)
                else:
                    self.close()
