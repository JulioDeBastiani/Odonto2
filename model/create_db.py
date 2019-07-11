from db_init import get_db
from indicacoes import Indicacoes
from alunos import Alunos
from pacientes import Pacientes
from parametrizacoes import Parametrizacoes
from panoramicas import Panoramicas
from tomografias import Tomografias
from cefalogramas import Cefalogramas

db = get_db()
db.connect
db.create_tables([Indicacoes, Alunos, Pacientes, Parametrizacoes, Panoramicas, Tomografias, Cefalogramas])