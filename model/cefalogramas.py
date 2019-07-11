import peewee as pw
from db import get_db
from pacientes import Pacientes
from parametrizacoes import Parametrizacoes

db = get_db()

class Cefalogramas(pw.Model):
    paciente = pw.ForeignKeyField(Pacientes, backref='panoramicas', on_delete='CASCADE')
    valor = pw.DoubleField(null=True)
    data_entrega = pw.DateField(null=True)
    motivo = pw.CharField(null=True)
    parametrizacao = pw.ForeignKeyField(Parametrizacoes, backref='panoramica', on_delete='CASCADE')
    modelo = pw.IntegerField()
    # 1..4

    class Meta:
        database = db