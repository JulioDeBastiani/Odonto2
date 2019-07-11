import peewee as pw
from db_init import get_db
from pacientes import Pacientes
from parametrizacoes import Parametrizacoes

db = get_db()

class Panoramicas(pw.Model):
    paciente = pw.ForeignKeyField(Pacientes, backref='panoramicas', on_delete='CASCADE')
    valor = pw.DoubleField(null=True)
    data_entrega = pw.DateField(null=True)
    motivo = pw.CharField(null=True)
    parametrizacao = pw.ForeignKeyField(Parametrizacoes, backref='panoramica', on_delete='CASCADE')
    tipo = pw.CharField()
    # 'Normal', 'Infantil', 'Implantes', 'Telerradiografia Lateral', 'Telerradiografia Frontal', 'Radiografia Carpal', 'Radiografia Atm Planigrafia', 'Radiografia Seios Maxilares'
    especializacao = pw.CharField()
    # 'Topo', 'Oclusao', 'Idade Ossea'
    regiao = pw.CharField()
    modelo = pw.IntegerField()
    # 1..9

    class Meta:
        database = db