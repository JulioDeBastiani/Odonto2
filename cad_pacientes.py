import peewee as pw
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from ui.ui_cad_pacientes import Ui_CadPacientes
from model.pacientes import Pacientes
from model.indicacoes import Indicacoes
from pesq_pacientes import PesqPacientes
from pesq_indicacoes import PesqIndicacoes

class CadPacientes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.paciente = None
        self.indicacao = None
        self.ind_text_changed = False
        self.ui = Ui_CadPacientes()
        self.ui.setupUi(self)
        self.__setupEvents()
        self.ui.edtId.setText(str(self.get_next_id()))

    def __clean(self):
        self.ui.edtId.setText(str(self.get_next_id()))
        self.ui.edtNome.clear()
        self.ui.edtNasc.clear()
        self.ui.edtClinViewId.clear()
        self.ui.edtIndicacao.clear()

    def __validate(self):
            if not self.ui.edtNome.text():
                self.alert("Preencha o nome")
                return False

            if not self.ui.edtNasc.date():
                self.alert("Preencha a data de nascimento")
                return False

            if not self.ui.edtClinViewId.text():
                self.alert("Preencha o id ClinView")
                return False

            return True

    def __setupEvents(self):
        def on_novo():
            self.__clean()
            self.ui.set_mode(True)

        def on_salvar():
            if not self.__validate():
                return

            try:
                if not self.paciente:
                    self.paciente = Pacientes.create(nome=str(self.ui.edtNome.text()), nascimento=self.ui.edtNasc.date().toPyDate(), clinview_id=str(self.ui.edtClinViewId.text()), indicacao=self.indicacao)
                else:
                    self.paciente.nome = str(self.ui.edtNome.text())
                    self.paciente.nascimento = self.ui.edtNasc.date().toPyDate()
                    self.paciente.clinview_id = str(self.ui.edtClinViewId.text())
                    self.paciente.indicacao = self.indicacao
                    self.paciente.save()
            except Exception as e:
                self.alert(str(e))
                return

            self.ui.set_mode(False)
            self.__clean()
            self.paciente = None
            self.indicacao = None

        def on_pesquisar():
            pesq = PesqPacientes()
            id = pesq.pesquisar()

            if id:
                self.paciente = Pacientes.get(Pacientes.id == int(id))
                self.indicacao = self.paciente.indicacao if self.paciente else None

            if self.paciente:
                self.ui.edtId.setText(str(self.paciente.id))
                self.ui.edtNome.setText(self.paciente.nome)
                self.ui.edtNasc.setDate(self.paciente.nascimento)
                self.ui.edtClinViewId.setText(self.paciente.clinview_id)

                if self.indicacao:
                    self.ui.edtIndicacao.setText(self.indicacao.nome)
                else:
                    self.ui.edtIndicacao.clear()

                self.ui.set_mode(True)
            pass

        def on_remover():
            if self.paciente:
                self.paciente.delete_instance()
            
            self.paciente = None
            self.indicacao = None
            self.__clean()
            self.ui.set_mode(False)

        def on_id_editing_finished():
            if (not self.ui.edtId.text()):
                return

            try:
                self.paciente = Pacientes.get(Pacientes.id == int(self.ui.edtId.text()))
                self.indicacao = self.paciente.indicacao if self.paciente else None
            except:
                pass

            if self.paciente:
                self.ui.edtNome.setText(self.paciente.nome)
                self.ui.edtNasc.setDate(self.paciente.nascimento)
                self.ui.edtClinViewId.setText(self.paciente.clinview_id)

                if self.indicacao:
                    self.ui.edtIndicacao.setText(self.indicacao.nome)
                else:
                    self.ui.edtIndicacao.clear()
                
                self.ui.set_mode(True)

        def on_sair():
            self.close()

        def on_pesq_indicacao():
            pesq = PesqIndicacoes()
            id = pesq.pesquisar()

            if id:
                self.indicacao = Indicacoes.get(Indicacoes.id == int(id))

            if self.indicacao:
                self.ui.edtIndicacao.setText(self.indicacao.nome)
            else:
                self.ui.edtIndicacao.clear()

        self.ui.btnNovo.clicked.connect(on_novo)
        self.ui.btnSalvar.clicked.connect(on_salvar)
        self.ui.btnPesquisar.clicked.connect(on_pesquisar)
        self.ui.btnRemover.clicked.connect(on_remover)
        self.ui.btnSair.clicked.connect(on_sair)
        self.ui.edtId.editingFinished.connect(on_id_editing_finished)
        self.ui.btnPesqIndicacao.clicked.connect(on_pesq_indicacao)

    def get_next_id(self):
        mid = Pacientes.select(pw.fn.Max(Pacientes.id)).scalar()
        return (mid if mid else 0) + 1

    def alert(self, message):
        alertd = QMessageBox()
        alertd.setText(message)
        alertd.exec_()

    def keyPressEvent(self, event):
        if not event.isAutoRepeat():
            if event.key() == Qt.Key_Escape:
                if not self.ui.edtId.isEnabled():
                    self.paciente = None
                    self.indicacao = None
                    self.__clean()
                    self.ui.set_mode(False)
                else:
                    self.close()
