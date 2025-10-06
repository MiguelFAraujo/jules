import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Obtém o caminho absoluto para o diretório do aplicativo
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Configura o URI do banco de dados para usar um caminho relativo
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'pessoas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'<Pessoa {self.nome}>'

@app.route('/')
def index():
    pessoas = Pessoa.query.all()
    return render_template('index.html', pessoas=pessoas)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    email = request.form['email']
    nova_pessoa = Pessoa(nome=nome, email=email)
    db.session.add(nova_pessoa)
    db.session.commit()
    return redirect(url_for('index'))

# Cria o banco de dados dentro do contexto da aplicação
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)