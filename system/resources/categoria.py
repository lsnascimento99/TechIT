from model.categoria import CategoriaModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Categoria(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="O Campo nome não pode estar em branco."
                        )
    # @jwt_required()
    def post(self):
        #Função post para registro de usuário
        data = Categoria.parser.parse_args()
        #Função para verificar se o usuário já existe no banco de dados
        if CategoriaModel.get_categoria(data['nome']):
            #caso não existir retorno a mensagem abaixo
            return {"message": "Essa categoria já existe no sistema"},409
        #chamando a classe para gravar o usuário no banco de dados
        categoria = CategoriaModel(data['nome'])
        categoria.save_to_db()
        
        return {"message": "Categoria criado com sucesso!"}, 201
    
    def get(self):
        #Função post para registro de usuário
        data = Categoria.parser.parse_args()
        #Função para verificar se o usuário já existe no banco de dados
        categoria = CategoriaModel.get_categoria(data['nome'])
        if categoria:
            #caso não existir retorno a mensagem abaixo
            return categoria.json()
        #chamando a classe para gravar o usuário no banco de dados
        return {"message": "Categoria não encontrada"}, 404

class CategoriaList(Resource):
    def get(self):
        registros = CategoriaModel.get_categoria_all()
        items = []
        for row in registros:
            items.append({'id': row[0], 'categoria': row[1]})
        return items


class CategoriaMaintenance(Resource):
    #Atualização do produto
    def put(self,id):
        data = Categoria.parser.parse_args()
        produtoModel = CategoriaModel.find_by_id(id)
        if (produtoModel):
             #Depois de ter verificado os campos que foram atualizados chamo a função para atualizar 
            try:
                CategoriaModel.update_categoria(id,data['nome'])
                return {"message": "Categoria atualizada com sucesso!"}  
            except:
                return {"message": "Ocorreu um erro para atualizar a categoria"}
        else:
            return {"message": "Erro a categoria não foi encontrada!"}, 404

    def delete(self, id):
        produtoModel = CategoriaModel.find_by_id(id)
        if (produtoModel):
            try:
                CategoriaModel.delete_by_id(id)
                return {'message': 'categoria deletada com sucesso'}
            except:
                return {"message": "Ocorreu um erro para deletar a categoria"}
        else:
            return {"message": "Categoria não encontrado para ser deletada!"}          
     