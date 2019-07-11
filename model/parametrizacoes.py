import peewee as pw
from db_init import get_db

db = get_db()

class Parametrizacoes(pw.Model):
    nome = pw.CharField(unique=True)
    tensao = pw.DoubleField()
    corrente = pw.DoubleField()
    tempo = pw.DoubleField()
    mgycm = pw.DoubleField()
    tamanho = pw.CharField()

    class Meta:
        database = db