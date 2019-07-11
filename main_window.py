from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from ui.ui_main_window import Ui_MainWindow
from cad_indicacoes import CadIndicacoes


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__setupEvents()

    def __setupEvents(self):
        def on_cad_indicacoes():
            indicacoes = CadIndicacoes()
            indicacoes.show()

        self.ui.actionIndica_es.triggered.connect(on_cad_indicacoes)

    def keyPressEvent(self, event):
        if not event.isAutoRepeat():
            if event.key() == Qt.Key_Escape:
                self.close()