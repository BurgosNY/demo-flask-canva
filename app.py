from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)
mongodb_uri = os.environ.get("MONGODB_URI")

@app.route("/")
def hello_world():
    return "<p>Olá, pessoal!</p>"


@app.route("/aulas")
def lista_aulas():
    db = MongoClient(mongodb_uri, ssl=True, tlsAllowInvalidCertificates=True)['mjd']
    disciplinas = db['disciplinas']
    disciplinas_mjd003 = []
    for disciplina in disciplinas.find({"turma": "MJD003"}):
        disciplinas_mjd003.append(disciplina)
    return render_template("lista_aulas.html", disciplinas=disciplinas_mjd003)


@app.route("/gravacoes/<zoom_id>")
def gravacoes(zoom_id):
    db = MongoClient(mongodb_uri, ssl=True, tlsAllowInvalidCertificates=True)['mjd']
    gravacoes = db['gravacoes']
    lista_gravacoes = []
    for gravacao in gravacoes.find({"meeting_id": int(zoom_id)}, {"_id": 0}):
        lista_gravacoes.append(gravacao)
    return render_template('lista_gravacoes.html', gravacoes=lista_gravacoes)

