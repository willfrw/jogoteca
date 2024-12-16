import os

from wtforms.fields.simple import SubmitField

from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validator.DataRequired(), validators.Length(min=1, max=50)])
    categoria = StringField('Categoria', [validator.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validator.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
