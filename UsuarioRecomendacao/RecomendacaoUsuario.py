from math import sqrt
from pymongo import MongoClient
from usuarioDados import getVisitasFromDatabase
from FuncoesGerais import similaridade, GetSimilares
import datetime

def getVisitas():
    return getVisitasFromDatabase()

def getSimilares(item):
    usuarios = getVisitasFromDatabase()
    if type(item) is dict:
        key = list(item.keys())[0]
        usuarios[key] = item[key]
        item = key
    return GetSimilares(usuarios,item)

def getRecomendacoesSimilares(usuario):
    si = getSimilares(usuario)
    return  [ item[1] for item in si if item[0] > 0.2] 

def getRecomendacoesEventos(usuario):
    usuariosRecomendados = getRecomendacoesSimilares(usuario)
    usuarios = getVisitasFromDatabase()
    eventosUsuario =  [usuarios[item] for item in usuariosRecomendados]
    lista = [list(evus.keys()) for evus in eventosUsuario]
    eventos = list(set([ ev for ev in lista for ev in ev]))
    eventos = [e for e in eventos if not e in usuarios[usuario] or usuarios[usuario][e] < 2]
    return eventos


