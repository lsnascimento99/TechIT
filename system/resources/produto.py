from model.produto import ProdutoModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Produto(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('idCategoria',
                        type=str,
                        # required=False,
                        # help="O Campo nome não pode estar em branco."
                        )
    parser.add_argument('nome',
                        type=str,
                        # required=False,
                        # help="O Campo nome não pode estar em branco."
                        )
    parser.add_argument('detalhe',
                        type=str,
                        # required=False,
                        # help="O Campo nome não pode estar em branco."
                        )
    parser.add_argument('preco',
                        type=str,
                        # required=False,
                        # help="O Campo nome não pode estar em branco."
                        )
    parser.add_argument('img',
                        type=str,
                        # required=False,
                        # help="O Campo img não pode estar em branco."
                        )

    # @jwt_required()
    def post(self):
        #Função post para registro de usuário
        data = Produto.parser.parse_args()
        #Função para verificar se o usuário já existe no ban    co de dados
        if ProdutoModel.get_produto(data['nome']):
            #caso não existir retorno a mensagem abaixo
            return {"message": "Essa categoria já existe no sistema"},409
        #chamando a classe para gravar o usuário no banco de dados
        categoria = ProdutoModel(data['idCategoria'],data['nome'],data['detalhe'], data['preco'],data['img'])
        categoria.save_to_db()
        
        return {"message": "Produto criado com sucesso!"}, 201
    
    def get(self,id):
        #Função post para registro de usuário
        #Função para verificar se o usuário já existe no banco de dados
        categoria = ProdutoModel.get_produto(id)
        if categoria:
            #caso não existir retorno a mensagem abaixo
            return categoria
        #chamando a classe para gravar o usuário no banco de dados
        return {"message": "Categoria não encontrada"}, 404

class ProdutoList(Resource):
    def get(self):
        registros = ProdutoModel.get_produto_all()
        produtos = []
        for row in registros:
            produtos.append({'id': row[0], 'idCategoria': row[1], 'nome': row[2], 'detalhe': row[3], 'preco': str(row[4]), 'img': row[5] })
        return produtos

class ProdutoMaintenance(Resource):
    #Atualização do produto
    def put(self,id):
        data = Produto.parser.parse_args()
        produtoModel = ProdutoModel.find_by_id(id)
        if (produtoModel):
             #Depois de ter verificado os campos que foram atualizados chamo a função para atualizar 
            try:
                ProdutoModel.update_produto(data['idCategoria'],data['nome'],data['detalhe'],data['preco'],id, data['img'])
                return {"message": "Produto atualizado com sucesso!"}  
            except:
                {"message": "Ocorreu um erro para atualizar o produto"}
        else:
            return {"message": "Erro o produto não foi encontrado!"}, 404
    def delete(self, id):
        produtoModel = ProdutoModel.find_by_id(id)
        if (produtoModel):
            try:
                ProdutoModel.delete_by_id(id)
                return {'message': 'produto deletado'}
            except:
                return {"message": "Ocorreu um erro para deletar o produto"}
        else:
            return {"message": "Produto não encontrado para ser deletado!"}       

    # def get(self, id):
    #     #Função post para registro de usuário
    #     data = Produto.parser.parse_args()
    #     #Função para verificar se o usuário já existe no banco de dados
    #     produto = ProdutoModel.get_produto(id)
    #     if produto:
    #         #caso não existir retorno a mensagem abaixo
    #         produtos = []
    #         for row in registros:
    #          produtos.({'id': row[0], 'idCategoria': row[1], 'nome': row[2], 'detalhe': row[3], 'preco': str(row[4]), 'img': row[5] })
    #          return categoria.json()
    #     #chamando a classe para gravar o usuário no banco de dados
    #     return {"message": "Categoria não encontrada"}, 404
     
        