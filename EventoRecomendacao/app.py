from flask import Flask, jsonify, request
app = Flask(__name__)

from Dados import getSimilares,getEventosFromDatabase,addEvento,makeRecomendacoesSimilares

@app.route('/Similares',methods=['POST'])
def post_similares():
    if not request.json:
        abort(400)
    teste = {
        '9999':request.json['evento']
    }
    return jsonify(getSimilares(teste)),200

@app.route('/SimilaresCodEvento',methods=['POST'])
def post_similaresCodEvento():
    if not request.json:
        abort(400)
    teste = {
        '9999':request.json['evento']
    }
    return jsonify([e[1] for e in getSimilares(teste) if e[0] >0.3 ]),200


@app.route('/Evento',methods=['POST'])
def post_addEvento():
    if not request.json:
        abort(400)
    tags = request.json["Tags"]
    key = str(request.json["Id"])
    evento = {key : dict([(str(item),1) for item in tags])}
    addEvento(key,evento)
    return jsonify(evento),201

@app.route('/Make',methods=['GET'])
def atualizaEventos():
    makeRecomendacoesSimilares()
    return jsonify("Ok"),200