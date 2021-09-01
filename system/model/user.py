from database import mysqlconnector

class UserModel():

    def __init__(self, username, password):
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
        cur.execute("SELECT id, usuario FROM usuarios WHERE usuario='" + username + "'")
        username = cur.fetchone()
        return username
