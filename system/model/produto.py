from logging import NullHandler
from database import database
import hashlib
import os



class ProdutoModel():

    def __init__(self, idCategoria, nome, detalhe, preco, img):
        self.idCategoria = idCategoria
        self.nome        = nome
        self.detalhe     = detalhe
        self.preco       = preco
        self.img       = img
        
        
    #Gravar user no DB
    def save_to_db(self):
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("INSERT INTO produto(id_categoria, nome, detalhe, preco,img) VALUES (%s,%s,%s,%s,%s)", (self.idCategoria,self.nome,self.detalhe,self.preco,self.img))
        connect.commit()
        cur.close()

    #Ao criar verificar se o categoria já existe
    @classmethod
    def get_produto(self, nome):
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("SELECT id FROM produto WHERE nome=%s",(nome,))
        registro = cur.fetchone()
        if (registro): 
            categoria = self
            categoria.nome = registro[0]
            return categoria
        categoria = False

    @classmethod
    def get_produto_all(self):
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("SELECT * FROM produto")
        registros = cur.fetchall()
        return registros
        
    @classmethod
    def delete_by_id(self, id):
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("DELETE FROM produto WHERE id =%s",(int(id),))
        connect.commit()
        cur.close()



    @classmethod
    def update_produto(self,idCategoria, nome, detalhe, preco, id, img):
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("UPDATE produto SET id_categoria =%s, nome =%s, detalhe= %s, preco = %s, img = %s where id= %s",(int(idCategoria),nome,detalhe,preco, img, id))
        connect.commit()
        cur.close()
        

    @classmethod
    def find_by_id(self, id):
        idProduto = int(id)
        connectorDatabase = database()
        connect = connectorDatabase.abrirConexao()
        cur = connect.cursor()
        cur.execute("SELECT id FROM produto WHERE id='%s'",(idProduto,))
        produto = cur.fetchone()
        return produto
