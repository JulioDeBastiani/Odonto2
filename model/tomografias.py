import peewee as pw
from db_init import get_db
from pacientes import Pacientes
from parametrizacoes import Parametrizacoes

db = get_db()

class Tomografias(pw.Model):
    paciente = pw.ForeignKeyField(Pacientes, backref='panoramicas', on_delete='CASCADE')
    aluno = pw.ForeignKeyField(Alunos, backref='tomografias', on_delete='CASCADE', null=True)
    valor = pw.DoubleField(null=True)
    data_entrega = pw.DateField(null=True)
    motivo = pw.CharField(null=True)
    parametrizacao = pw.ForeignKeyField(Parametrizacoes, backref='panoramica', on_delete='CASCADE')
    tipo = pw.CharField()
    # 'Maxila', 'Mandibula', 'ATM', 'Segmento', 'Elemento'
    especializacao = pw.CharField()
    # 'Ramos Mandibulares', 'Oclusao', 'Abertura'
    regiao = pw.CharField()
    elemento = pw.CharField()
    proporcao = pw.CharField()
    # '5x5', '6x8', '8x8', '8x15', '13x15'
    alvo = pw.CharField()
    # 'Alvo', 'Dente'
    resolucao = pw.CharField()
    # 'B', 'M', 'A'

    class Meta:
        database = db