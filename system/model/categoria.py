from logging import NullHandler
from database import database
import hashlib
import os



class CategoriaModel():

    def __init__(self, categoria):
        self.categoria       = categoria
        
        
    #Gravar user no DB
    def save_to_db(self):
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("INSERT INTO categoria(nome) VALUES (%s)", (self.categoria,))
        connect.commit()
        cur.close()

    #Ao criar verificar se o usuário já existe
    @classmethod
    def get_categoria(self, nome):
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("SELECT nome FROM categoria WHERE nome=%s",(nome,))
        registro = cur.fetchone()
        if (registro): 
            categoria = self
            categoria.nome = registro[0]
            return categoria
        categoria = False

    @classmethod
    def get_categoria_all(self):
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("SELECT * FROM categoria")
        registros = cur.fetchall()
        return registros
        

    @classmethod
    def find_by_id(cls, id):
        id = str(id)
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("SELECT id FROM usuario WHERE id='" + id + "'")
        username = cur.fetchone()
        return username
