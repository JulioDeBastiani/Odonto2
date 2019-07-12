import peewee as pw
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from ui.ui_cad_tomografias import Ui_CadTomografias
from model.tomografias import Tomografias
from model.pacientes import Pacientes
from model.alunos import Alunos
from model.parametrizacoes import Parametrizacoes
from pesq_pacientes import PesqPacientes
from pesq_alunos import PesqAlunos
from cad_parametrizacoes import CadParametrizacoes
# from pesq_panoramicas import PesqPanoramicas

class CadTomografias(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.tomografia = None
        self.paciente = None
        self.aluno = None
        self.parametrizacao = None
        self.ui = Ui_CadTomografias()
        self.ui.setupUi(self)
        self.__setupEvents()
        self.ui.edtId.setText(str(self.get_next_id()))

    def __clean(self):
        self.ui.edtId.setText(str(self.get_next_id()))
        self.ui.edtPaciente.clear()
        self.ui.edtAluno.clear()
        self.ui.edtValor.clear()
        self.ui.chkEntregue.setChecked(False)
        self.ui.edtEntrega.clear()
        self.ui.cboTipo.setCurrentIndex(0)
        self.ui.cboEspecializacao.setCurrentIndex(0)
        self.ui.edtRegiao.clear()
        self.ui.edtElemento.clear()
        self.ui.cboProporcao.clear()
        self.ui.cboAlvo.clear()
        self.ui.cboResolucao.clear()

    def __validate(self):
            if not self.paciente:
                self.alert("Preencha o paciente")
                return False

            if not self.aluno:
                self.alert("Preencha o paciente")
                return False

            try:
                if self.ui.edtValor.text():
                    v = float(self.ui.edtValor.text())
            except:
                self.alert("Valor inválido")
                return False

            if not self.parametrizacao:
                self.alert("Preencha a parametrização")
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
                if not self.tomografia:
                    valor = float(self.ui.edtValor.text()) if self.ui.edtValor.text() else None
                    entrega = self.ui.edtEntrega.date().toPyDate() if self.ui.chkEntregue.isChecked() else None
                    self.tomografia = Tomografias.create(
                        paciente=self.paciente,
                        aluno=self.aluno,
                        valor=valor,
                        data_entrega=entrega,
                        motivo=str(self.ui.edtMotivo.text()),
                        parametrizacao=self.parametrizacao,
                        tipo=str(self.ui.cboTipo.currentText()),
                        especializacao=str(self.ui.cboEspecializacao.currentText()),
                        regiao=str(self.ui.edtRegiao.text()),
                        modelo=str(self.ui.cboModelo.currentText()),
                        elemento=str(self.ui.edtElemento.text()),
                        proporcao=str(self.ui.cboProporcao.currentText()),
                        alvo=str(self.ui.cboAlvo.currentText()),
                        resolucao=str(self.ui.cboResolucao.currentText()))
                else:
                    valor = float(self.ui.edtValor.text()) if self.ui.edtValor.text() else None
                    entrega = self.ui.edtEntrega.date().toPyDate() if self.ui.chkEntregue.isChecked() else None
                    self.tomografia.paciente = self.paciente
                    self.tomografia.aluno = self.aluno
                    self.tomografia.valor = valor
                    self.tomografia.data_entrega = entrega
                    self.tomografia.motivo = str(self.ui.edtMotivo.text())
                    self.tomografia.parametrizacao = self.parametrizacao
                    self.tomografia.tipo = str(self.ui.cboTipo.currentText())
                    self.tomografia.especializacao = str(self.ui.cboEspecializacao.currentText())
                    self.tomografia.regiao = str(self.ui.edtRegiao.text())
                    self.tomografia.modelo = str(self.ui.cboModelo.currentText())
                    self.tomografia.elemento = str(self.ui.edtElemento.text())
                    self.tomografia.proporcao = str(self.ui.cboProporcao.currentText())
                    self.tomografia.alvo = str(self.ui.cboAlvo.currentText())
                    self.tomografia.resolucao = str(self.ui.cboResolucao.currentText())
                    self.tomografia.save()
            except Exception as e:
                self.alert(str(e))
                return

            self.ui.set_mode(False)
            self.__clean()
            self.paciente = None
            self.indicacao = None

        def on_pesquisar():
            # pesq = PesqPanoramicas()
            # id = pesq.pesquisar()

            # if id:
            #     self.panoramica = Panoramicas.get(Panoramicas.id == int(id))
            #     self.paciente = self.panoramica.paciente
            #     self.aluno = self.panoramica.aluno
            #     self.parametrizacao = self.panoramica.parametrizacao

            # if self.panoramica:
            #     self.ui.edtId.setText(str(self.panoramica.id))
                    
            #     if self.panoramica.valor:
            #         self.ui.edtValor.setText(str(self.panoramica.valor))

            #     self.ui.chkEntregue.setChecked(self.panoramica.data_entrega != None)

            #     if self.panoramica.data_entrega:
            #         self.ui.edtEntrega.setDate(self.panoramica.data_entrega)

            #     self.ui.edtMotivo.setText(self.panoramica.motivo)
            #     self.ui.edtRegiao.setText(self.panoramica.regiao)

            #     index = self.ui.cboTipo.findText(self.panoramica.tipo)
            #     if index >= 0:
            #         self.ui.cboTipo.setCurrentIndex(index)

            #     index = self.ui.cboEspecializacao.findText(self.panoramica.especializacao)
            #     if index >= 0:
            #         self.ui.cboEspecializacao.setCurrentIndex(index)

            #     index = self.ui.cboModelo.findText(self.panoramica.modelo)
            #     if index >= 0:
            #         self.ui.cboModelo.setCurrentIndex(index)

            #     self.ui.edtPaciente.setText(self.paciente.nome)
            #     self.ui.edtAluno.setText(self.aluno.nome)

            #     self.ui.set_mode(True)
            pass

        def on_remover():
            if self.tomografia:
                self.tomografia.delete_instance()
            
            self.tomografia = None
            self.paciente = None
            self.aluno = None
            self.parametrizacao = None
            self.__clean()
            self.ui.set_mode(False)

        def on_id_editing_finished():
            if (not self.ui.edtId.text()):
                return

            try:
                self.tomografia = Tomografias.get(Tomografias.id == int(self.ui.edtId.text()))
                self.paciente = self.tomografia.paciente
                self.aluno = self.tomografia.aluno
                self.parametrizacao = self.tomografia.parametrizacao
            except:
                pass

            if self.tomografia:
                if self.tomografia.valor:
                    self.ui.edtValor.setText(str(self.tomografia.valor))

                self.ui.chkEntregue.setChecked(self.panoramica.data_entrega != None)

                if self.tomografia.data_entrega:
                    self.ui.edtEntrega.setDate(self.tomografia.data_entrega)

                self.ui.edtMotivo.setText(self.tomografia.motivo)
                self.ui.edtRegiao.setText(self.tomografia.regiao)
                self.ui.edtElemento.setText(self.tomografia.elemento)

                index = self.ui.cboTipo.findText(self.tomografia.tipo)
                if index >= 0:
                    self.ui.cboTipo.setCurrentIndex(index)

                index = self.ui.cboEspecializacao.findText(self.tomografia.especializacao)
                if index >= 0:
                    self.ui.cboEspecializacao.setCurrentIndex(index)

                index = self.ui.cboProporcao.findText(self.tomografia.proporcao)
                if index >= 0:
                    self.ui.cboProporcao.setCurrentIndex(index)

                index = self.ui.cboAlvo.findText(self.tomografia.alvo)
                if index >= 0:
                    self.ui.cboAlvo.setCurrentIndex(index)

                index = self.ui.cboResolucao.findText(self.tomografia.resolucao)
                if index >= 0:
                    self.ui.cboResolucao.setCurrentIndex(index)

                self.ui.edtPaciente.setText(self.paciente.nome)
                self.ui.edtAluno.setText(self.aluno.nome)

                self.ui.set_mode(True)

        def on_sair():
            self.close()

        def on_pesq_paciente():
            pesq = PesqPacientes()
            id = pesq.pesquisar()

            if id:
                self.paciente = Pacientes.get(Pacientes.id == int(id))

            if self.paciente:
                self.ui.edtPaciente.setText(self.paciente.nome)
            else:
                self.ui.edtPaciente.clear()

        def on_limpar_paciente():
            self.paciente = None
            self.ui.edtPaciente.clear()

        def on_pesq_aluno():
            pesq = PesqAlunos()
            id = pesq.pesquisar()

            if id:
                self.aluno = Alunos.get(Alunos.id == int(id))

            if self.aluno:
                self.ui.edtAluno.setText(self.aluno.nome)
            else:
                self.ui.edtAluno.clear()

        def on_limpar_aluno():
            self.aluno = None
            self.ui.edtAluno.clear()

        def on_parametrizacoes():
            par = CadParametrizacoes()
            id = self.parametrizacao.id if self.parametrizacao else None
            id = par.abrir(id)

            if id:
                self.parametrizacao = Parametrizacoes.get(Parametrizacoes.id == int(id))
            else:
                self.parametrizacao = None

        self.ui.btnNovo.clicked.connect(on_novo)
        self.ui.btnSalvar.clicked.connect(on_salvar)
        self.ui.btnPesquisar.clicked.connect(on_pesquisar)
        self.ui.btnRemover.clicked.connect(on_remover)
        self.ui.btnSair.clicked.connect(on_sair)
        self.ui.edtId.editingFinished.connect(on_id_editing_finished)
        self.ui.btnPesqPaciente.clicked.connect(on_pesq_paciente)
        self.ui.btnLimparPaciente.clicked.connect(on_limpar_paciente)
        self.ui.btnPesqAluno.clicked.connect(on_pesq_aluno)
        self.ui.btnLimparAluno.clicked.connect(on_limpar_aluno)
        self.ui.btnParametrizacao.clicked.connect(on_parametrizacoes)

    def get_next_id(self):
        mid = Tomografias.select(pw.fn.Max(Tomografias.id)).scalar()
        return (mid if mid else 0) + 1

    def alert(self, message):
        alertd = QMessageBox()
        alertd.setText(message)
        alertd.exec_()

    def keyPressEvent(self, event):
        if not event.isAutoRepeat():
            if event.key() == Qt.Key_Escape:
                if not self.ui.edtId.isEnabled():
                    self.tomografia = None
                    self.paciente = None
                    self.aluno = None
                    self.parametrizacao = None
                    self.__clean()
                    self.ui.set_mode(False)
                else:
                    self.close()
