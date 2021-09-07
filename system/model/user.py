from logging import NullHandler
from database import database
import hashlib
import os



class UserModel():

    def __init__(self, id, username, password,nome,sobrenome,dtNascimento,endereco,cidade,estado,dataCriacao):
        self.id       = id
        self.username = username
        self.password = password
        self.nome = nome
        self.sobrenome = sobrenome
        self.dtNascimento = dtNascimento
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.dataCriacao = dataCriacao
        
    #Gravar user no DB
    def save_to_db(self):
        id = int()
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("INSERT INTO usuario(usuario,senha,nome,sobrenome,data_nascimento,endereco,cidade,estado,data_criacao) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.username, self.password, self.nome, self.sobrenome, self.dtNascimento, self.endereco, self.cidade, self.estado, self.dataCriacao))
        connect.commit()
        cur.close()

    #Ao criar verificar se o usuário já existe
    @classmethod
    def find_by_username(self, username):
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("SELECT id, usuario, senha, nome, sobrenome, data_nascimento FROM usuario WHERE usuario=%s",(username,))
        # cur.execute("SELECT id, usuario, senha FROM usuarios WHERE usuario='" + username + "'")
        username = cur.fetchone()
        if (username): 
            user = self
            user.id = username[0]
            user.username = username[1]
            user.password = username[2]
            user.sobrenome = username[3]
            user.dtNascimento = username[4]
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

class pwdHash():
    def __init__(self, password):
        self.password = password
        self.salt = os.urandom(16) # Remember this
        self.key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        self.password.encode('utf-8'), # Convert the password to bytes
        self.salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
        )
    

    def setEncriptPass(self, password):
        # Encryption with AES-256-CBC
        encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(self.key, self.salt))
        ciphertext = encrypter.feed(password.encode('utf8'))
        ciphertext += encrypter.feed()
        return ciphertext
    
    def getDecriptPass(self, password):
        # Decryption with AES-256-CBC
        decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(password))
        decryptedData = decrypter.feed(password)
        decryptedData += decrypter.feed()
        return decryptedData
