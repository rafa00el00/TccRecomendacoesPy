# encoding=utf8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
from pymongo import MongoClient
import datetime

dbName = 'DadosUsuarioVisitas'

def Database():
    con = MongoClient('localhost', 27017)
    db = con[dbName]
    return db

def addInDataBase(visita):
    db = Database()
    env = db.visitas
    env.insert_one(visita)

def getVisitasFromDatabase():
    db = Database()
    usus = db.visitas
    usuarios = [u for u in usus.find({}) if u != '_id'][0]
    del usuarios['_id']
    return usuarios

def addVisita(usuario):
    db = Database()
    visita = db.visitas.find_one({})
    key = list(usuario.keys())[0]
    if not key in visita:
        visita[key] = {}
    visita[key].update(usuario[key])
    return db.visitas.find_one_and_update({}, {"$set":visita})





