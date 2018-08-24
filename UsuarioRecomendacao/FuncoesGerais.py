from math import sqrt
from pymongo import MongoClient
import datetime

#Calcula a similaridade de 2 itens com formato Padrao
def similaridade(lista,item1,item2):
    si = 0
    
    for item in lista[item1] :
        if item in lista[item2] : si =1

    if(si == 0) : return 0

    soma = sum([pow(lista[item1][item] + lista[item2][item],2)
                for item in lista[item1] if item in lista[item2] ])
    return 1 / (1+ sqrt(soma))

def GetSimilares(lista,itemOriginal):
    si = [(similaridade(lista,itemOriginal,item),item) 
            for item in lista if item != itemOriginal]
    si.sort()
    si.reverse()
    return si