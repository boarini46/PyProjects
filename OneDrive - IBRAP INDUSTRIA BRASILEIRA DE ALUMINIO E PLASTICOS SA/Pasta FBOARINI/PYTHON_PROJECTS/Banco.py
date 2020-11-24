#importando módulo do SQlite

import sqlite3

#import cx_Oracle
#import sys


#


class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                     idusuario integer primary key autoincrement ,
                     nome text,
                     telefone text,
                     email text,
                     usuario text,
                     senha text)""")
        self.conexao.commit()
        c.close()

'''
cx_Oracle.init_oracle_client(lib_dir="C:/ORACLE/instantclient_19_8_32")
uid = "protheus_homologa"       # usuário
pwd = "totvs"                   # senha
db  = "protheus_homologa"       # string de conexão do Oracle, configurado no cliente Oracle, arquivo tnsnames.ora
 
connection = cx_Oracle.connect(uid+"/"+pwd+"@"+db) #cria a conexão
cursor = connection.cursor()                       # cria um cursor
cliente = input("Código do Cliente: ")
cursor.execute("SELECT SA1.A1_CONTATO ,SA1.* from SA1010 SA1 where D_E_L_E_T_ <> '*' and A1_MSBLQL = '2' and A1_COD = '"+ cliente +"'") # consulta sql
result = cursor.fetchone()                         # busca o resultado da consulta
if result == None: 
        print( "Nenhum Resultado")
        exit
else:
        while result:   
                print ("CLIENTE: " + result[2].strip()+" - CNPJ: "+result[6].strip())
                result = cursor.fetchone()
cursor.close()
connection.close()
'''