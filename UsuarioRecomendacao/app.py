from flask import Flask, jsonify, request
app = Flask(__name__)

from RecomendacaoUsuario import getRecomendacoesSimilares,getRecomendacoesEventos,getRecomendacoesAllUsuarios
from UsuarioNegocio import AddVisita


@app.route('/Similares',methods=['POST'])
def post_similares():
    if not request.json:
        abort(400)
    teste = {
        '9999':request.json['usuario']
    }
    return jsonify(getRecomendacoesSimilares(teste)),200

@app.route('/Similares/<usuario>',methods=['GET'])
def get_similaresPorUsuario(usuario):
    if not usuario:
        abort(400)
    return jsonify(getRecomendacoesEventos(usuario)),200

@app.route('/AddMovimentacao',methods=['POST'])
def post_addMovimentacaco():
    if not request.json:
        abort(400)
    teste = {
        request.json['usuario']: {request.json['evento'] : request.json['status']}
    }
    retorno = AddVisita(teste) 
    return "Adicionada" ,200

@app.route('/GetAllRecomendacoes',methods=['GET'])
def GetAllrecomendacoes():
    return jsonify(getRecomendacoesAllUsuarios()),200
