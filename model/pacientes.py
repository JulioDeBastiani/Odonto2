import peewee as pw
from db import get_db
from alunos import Alunos
from indicacoes import Indicacoes

db = get_db()

class Pacientes(pw.Model):
    nome = pw.CharField(unique=True)
    nascimento = pw.DateField()
    clinview_id = pw.CharField(unique=True)
    aluno = pw.ForeignKeyField(Alunos, backref='pacientes', on_delete='CASCADE', null=True)
    indicacao = pw.ForeignKeyField(Indicacoes, backref='pacientes', on_delete='CASCADE', null=True)

    class Meta:
        database = db