from pymongo import MongoClient

con = MongoClient('localhost', 27017)
db = con['DadosEventos']
env = db.eventos
env.insert_one({})

db = con['DadosUsuarioVisitas']
env = db.visitas
env.insert_one({})