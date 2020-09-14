from os.path import dirname, realpath, isfile
from json import dump, load
import json
from unicodedata import normalize
import re
import pymysql


mydb= pymysql.connect(
    host="localhost",
    user="root",
    password="root"

)
cursor=mydb.cursor()
class Json:
    def __init__(self):
        self.path= dirname(realpath(__file__))+'/'

    def pegarManager(self,file):
        if isfile(self.path+file):
            with open(self.path+file) as f:
                data = json.load(f)
            return data


        else:
            print(self.path)
            return False

    def Escrever(self,file,dados):
        if isfile(self.path+file):
            with open(self.path+file,'a') as f:
               json.dump(dados,f)

    def Administradores():
        a = Json()
        dados = a.pegarManager("source_file_2.json")
        managers = []
        for d in dados:
            nome = d['name']
            for a in d['managers']:
                managers.append(a)

        l = []
        for i in managers:
            if i not in l:
                l.append(i)
        return l
    def Servidores():
        a = Json()
        dados = a.pegarManager("source_file_2.json")
        servidores = []
        for d in dados:
            nome = d['name']
            for a in d['watchers']:
                servidores.append(a)

        l = []
        for i in servidores:
            if i not in l:
                l.append(i)
        return l
Escritor=Json()
Gerentes=Json.Administradores()
print(Gerentes)
for Gerentes in Gerentes:
    cursor.execute("SELECT name FROM goupbot.source_file_2 where managers like '%"+Gerentes+"%' order by priority")
    data=cursor.fetchall()
    dados={
        Gerentes:[
            data

        ]
    }
    Escritor.Escrever('managers.json',dados)

Assistentes=Json.Servidores()
for Assistentes in Assistentes:
    cursor.execute("SELECT name FROM goupbot.source_file_2 where watchers like '%"+Assistentes+"%' order by priority")
    data=cursor.fetchall()
    dados={
        Assistentes:[
            data

        ]
    }
    Escritor.Escrever('watchers.json',dados)





