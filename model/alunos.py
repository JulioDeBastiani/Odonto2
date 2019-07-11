import peewee as pw
from db import get_db

db = get_db()

class Alunos(pw.Model):
    nome = pw.CharField(unique=True)

    class Meta:
        database = db