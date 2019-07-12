import peewee as pw
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import Qt
from ui.ui_cad_parametrizacoes import Ui_CadParametrizacoes
from model.parametrizacoes import Parametrizacoes

class CadParametrizacoes(QDialog):
    def __init__(self):
        super().__init__()
        self.parametrizacao = None
        self.ui = Ui_CadParametrizacoes()
        self.ui.setupUi(self)
        self.__setupEvents()

    def __validate(self):
        if not self.ui.edtTensao.text():
            self.alert("Preencha a tensão")
            return False

        try
            v = float(self.ui.edtTensao.text())
        except:
            self.alert("Tensão inválida")
            return False

        if not self.ui.edtCorrente.text():
            self.alert("Preencha a corrente")
            return False

        try
            v = float(self.ui.edtCorrente.text())
        except:
            self.alert("Corrente inválida")
            return False

        if not self.ui.edtTempo.text():
            self.alert("Preencha o tempo")
            return False

        try
            v = float(self.ui.edtTempo.text())
        except:
            self.alert("Tempo inválido")
            return False

        if not self.ui.edtMgycm.text():
            self.alert("Preencha o mGcym")
            return False

        try
            v = float(self.ui.edtMgycm.text())
        except:
            self.alert("mGcym inválido")
            return False
        
        return True

    def __setupEvents(self):
        def on_salvar():
            if not self.__validate():
                return

            try:
                if not self.parametrizacao:
                    self.parametrizacao = Parametrizacoes.create(
                        tensao=float(self.ui.edtTensao.text())
                        corrente=float(self.ui.edtCorrente.text())
                        tempo=float(self.ui.edtTempo.text())
                        mgycm=float(self.ui.edtMgycm.text())
                        tamanho=str(self.ui.cboTamanho.text()))
                else:
                    self.parametrizacao.tensao = float(self.ui.edtTensao.text())
                    self.parametrizacao.corrente = float(self.ui.edtCorrente.text())
                    self.parametrizacao.tempo = float(self.ui.edtTempo.text())
                    self.parametrizacao.mgycm = float(self.ui.edtMgycm.text())
                    self.parametrizacao.tamanho = str(self.ui.cboTamanho.text())
                    self.parametrizacao.save()
            except Exception as e:
                self.alert(str(e))
                return

            self.close()

        def on_cancelar():
            self.close()

        self.ui.btnSalvar.clicked.connect(on_salvar)
        self.ui.btnCancelar.clicked.connect(on_cancelar)

    def alert(self, message):
        alertd = QMessageBox()
        alertd.setText(message)
        alertd.exec_()

    def abrir(self, id=None):
        if id:
            self.parametrizacao = Parametrizacoes.get(Parametrizacoes.id == id)

            if self.parametrizacao:
                self.ui.edtTensao.setText(str(self.parametrizacao.tensao))
                self.ui.edtCorrente.setText(str(self.parametrizacao.corrente))
                self.ui.edtTempo.setText(str(self.parametrizacao.tempo))
                self.ui.edtMgycm.setText(str(self.parametrizacao.mgycm))

                index = self.ui.cboTamanho.findText(self.parametrizacao.tamanho)
                if index >= 0:
                    self.ui.cboTamanho.setCurrentIndex(index)

        self.exec_()

        if self.parametrizacao:
            return self.parametrizacao.id

    def keyPressEvent(self, event):
        if not event.isAutoRepeat():
            if event.key() == Qt.Key_Escape:
                self.close()
