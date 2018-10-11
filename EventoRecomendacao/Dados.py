# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

eventos = {
    '1':{
        'gastronomico':1,
        'todos':1,
        'familia':1,
        'churros':1,
        'cerveja artesanal':1,
        'zona norte':1,
        'sabado':1,
        'domigo':1,
        'food truck':1,
        'ar livre':1,
        'gratuito':1
    },
    '2':{
        'apresentação':1,
        'familia':1,
        'infantil':1,
        'diversao':1,
        'magico':1,
        'palhaço':1,
        'picadeiro':1,
        'acrobata':1,
        'trapezio':1,
        'pago':1,
        'barato':1
    },
    '3':{  
        'feira':1,
        'feminino':1,
        'plus size':1,
        'vestido':1,
        'saia':1,
        'camisa':1,
        'calça':1,
        'estilo':1,
        'moderno':1,
        'arrojado':1,
        'criativo':1,
        'fechado':1,
        'pago':1
    },
    '4':{
        'apresentação':1,
        'espetaculo':1,
        'comédia':1,
        'adulto':1,
        'pago':1,
        'centro':1,
        'standup':1,
        'ator':1,
        'atriz':1,
        'direcao':1,
        'marcos castro':1,
        'thiago ventura':1,
        'nando vianna':1,
        'afonço padilha':1
    },
    '5':{
        'decoração':1,
        'casa':1,
        'jardinagem':1,
        'casal':1,
        'arquiteto':1,
        'design de interiores':1,
        'iluminação':1,
        'estilo de vida':1,
        'streampunk':1,
        'vintage':1,
        'moveis em madeira':1,
        'sustentabilidade':1,
        'cores':1,
        'pintura':1
    },
    '6':{
        'gastronomico':1,
        'food truck':1,
        'cachaça artesanal':1,
        'cerveja artesanal':1,
        'hambuguer':1,
        'mea culpa':1,
        'massa na caveira':1,
        'jupiter':1,
        'ar livre':1,
        'zona leste':1,
        'tatuape':1,
        'hotdog':1,
        'pizza':1,
        'veggie':1,
        'show ao vivo':1,
        'banda':1,
        'barato':1
    },
    '7':{
        'espetaculo':1,
        'drama':1,
        'vagner moura':1,
        'tiro':1,
        'policia':1,
        'tony ramos':1,
        'pago':1,
        'regina duarte':1,
        'jk iquatemi':1,
        'fechado':1,
        'teatro':1,
        'realista':1
    },
    '8':{
        'feira':1,
        'epi':1,
        'cipa':1,
        'primeiros socorros':1,
        'capacete':1,
        'luva':1,
        'segurança do trabalho':1,
        'bota':1,
        'palestra':1
    }
}


from math import sqrt
from pymongo import MongoClient
import datetime

def addInDataBase():
    con = MongoClient('localhost', 27017)
    db = con['DadosEventos']
    env = db.eventos
    env.insert_one(eventos)

def addEvento(key,evento):
    con = MongoClient('localhost', 27017)
    db = con['DadosEventos']
    env = db.eventos.find_one({}) or {}
    env[key] = evento[key]
    db.eventos.find_one_and_update({},{"$set":env})

def getEventosFromDatabase():
    con = MongoClient('localhost',27017)
    db = con.DadosEventos
    env = db.eventos
    ev = [ ev for ev in env.find({}) if ev != '_id'][0]
    del ev['_id']
    return ev

def similaridade(evento1,evento2,lista):
    si = 0
    # eventos = getEventosFromDatabase()
    eventos = lista
    for item in eventos[evento1] :
        if item in eventos[evento2] : si =1

    if(si == 0) : return 0

    soma = sum([pow(eventos[evento1][item] + eventos[evento2][item],2)
                for item in eventos[evento1] if item in eventos[evento2] ])
    return 1 / (1+ sqrt(soma))

def getSimilares(evento):
    eventos = getEventosFromDatabase()
    if type(evento) is dict:
        key = list(evento.keys())[0]
        eventos[key] = evento[key]
        evento = key
    si = [(similaridade(evento,item,eventos),item) 
            for item in eventos if item != evento]
    si.sort()
    si.reverse()
    return si

def getRecomendacoesSimilares(evento):
    si = getSimilares(evento)
    return { evento:  [ item[1] for item in si if item[0] > 0.2] }

def makeRecomendacoesSimilares():
    eventos = getEventosFromDatabase()
    recomendacoes = [getRecomendacoesSimilares(evento) for evento in eventos]
    con = MongoClient('localhost', 27017)
    db = con['RecomendacoesEventos']
    env = db.eventos
    env.delete_many({})
    env.insert_many(recomendacoes)
    return recomendacoes
