from logging import NullHandler
from database import database

class UserModel():

    def __init__(self, id, username, password):
        self.id       = id
        self.username = username
        self.password = password
        
    #Gravar user no DB
    def save_to_db(self):
        id = int()
        # cur = mysqlconnector.cursor()
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("INSERT INTO usuario(usuario,senha) VALUES (%s, %s)", (self.username, self.password))
        connect.commit()
        cur.close()

    #Ao criar verificar se o usuário já existe
    @classmethod
    def find_by_username(self, username):
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("SELECT id, usuario, senha FROM usuario WHERE usuario=%s",(username,))
        # cur.execute("SELECT id, usuario, senha FROM usuarios WHERE usuario='" + username + "'")
        username = cur.fetchone()
        if (username): 
            user = self
            user.id = username[0]
            user.username = username[1]
            user.password = username[2]
            return user
        username = False

    @classmethod
    def find_by_id(cls, id):
        id = str(id)
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("SELECT id FROM usuario WHERE id='" + id + "'")
        username = cur.fetchone()
        return username