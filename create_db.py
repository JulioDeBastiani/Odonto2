from model.db_init import get_db
from model.indicacoes import Indicacoes
from model.alunos import Alunos
from model.pacientes import Pacientes
from model.parametrizacoes import Parametrizacoes
from model.panoramicas import Panoramicas
from model.tomografias import Tomografias
from model.cefalogramas import Cefalogramas

db = get_db()
db.connect
db.create_tables([Indicacoes, Alunos, Pacientes, Parametrizacoes, Panoramicas, Tomografias, Cefalogramas])