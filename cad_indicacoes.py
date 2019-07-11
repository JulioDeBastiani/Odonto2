import peewee as pw
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from ui.ui_cad_indicacoes import Ui_CadIndicacoes
from model.indicacoes import Indicacoes
from pesq_indicacoes import PesqIndicacoes

class CadIndicacoes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.indicacao = None
        self.ui = Ui_CadIndicacoes()
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

            if not self.indicacao:
                self.indicacao = Indicacoes.create(nome=str(self.ui.edtNome.text()))
            else:
                self.indicacao.nome = str(self.ui.edtNome.text())
                self.indicacao.save()

            self.ui.set_mode(False)
            self.ui.edtId.setText(str(self.get_next_id()))
            self.ui.edtNome.clear()
            self.indicacao = None

        def on_pesquisar():
            pesq = PesqIndicacoes()
            id = pesq.pesquisar()

            if id:
                self.indicacao = Indicacoes.get(Indicacoes.id == int(id))

            if self.indicacao:
                self.ui.edtId.setText(str(self.indicacao.id))
                self.ui.edtNome.setText(self.indicacao.nome)
                self.ui.set_mode(True)
            pass

        def on_remover():
            if self.indicacao:
                self.indicacao.delete_instance()
            
            self.indicacao = None
            self.ui.edtId.setText(str(self.get_next_id()))
            self.ui.edtNome.clear()
            self.ui.set_mode(False)

        def on_id_editing_finished():
            if (not self.ui.edtId.text()):
                return

            self.indicacao = Indicacoes.get(Indicacoes.id == int(self.ui.edtId.text()))

            if self.indicacao:
                self.ui.edtNome.setText(self.indicacao.nome)
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
        mid = Indicacoes.select(pw.fn.Max(Indicacoes.id)).scalar()
        return (mid if mid else 0) + 1

    def alert(self, message):
        alertd = QMessageBox()
        alertd.setText(message)
        alertd.exec_()

    def keyPressEvent(self, event):
        if not event.isAutoRepeat():
            if event.key() == Qt.Key_Escape:
                if not self.ui.edtId.isEnabled():
                    self.indicacao = None
                    self.ui.edtId.setText(str(self.get_next_id()))
                    self.ui.edtNome.clear()
                    self.ui.set_mode(False)
                else:
                    self.close()
