from logging import NullHandler
from database import mysqlconnector

class UserModel():

    def __init__(self, id, username, password):
        self.id       = id
        self.username = username
        self.password = password
        
    #Gravar user no DB
    def save_to_db(self):
        id = int()
        cur = mysqlconnector.cursor()
        cur.execute("INSERT INTO usuarios(usuario,senha) VALUES (%s, %s)", (self.username, self.password))
        mysqlconnector.commit()
        cur.close()

    #Ao criar verificar se o usuário já existe
    @classmethod
    def find_by_username(cls, username):
        cur = mysqlconnector.cursor()
        cur.execute("SELECT id, usuario, senha FROM usuarios WHERE usuario='" + username + "'")
        username = cur.fetchone()
        if username == True:    
            cls.id = username[0]
            cls.username = username[1]
            cls.password = username[2]
            return cls
        username = False
        return username

    @classmethod
    def find_by_id(cls, id):
        id = str(id)
        cur = mysqlconnector.cursor()
        cur.execute("SELECT id FROM usuarios WHERE id='" + id + "'")
        username = cur.fetchone()
        return username