from model.statusPedido import StatusModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Status(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('status',
                        type=str,
                        required=True,
                        help="O Campo status não pode estar em branco."
                        )

    # @jwt_required()
    def post(self):
        #Função post para registro de usuário
        data = Status.parser.parse_args()
        #Função para verificar se o usuário já existe no banco de dados
        if StatusModel.get_status(data['nome']):
            #caso não existir retorno a mensagem abaixo
            return {"message": "Essa categoria já existe no sistema"},409
        #chamando a classe para gravar o usuário no banco de dados
        statusPedido = StatusModel(data['status'])
        statusPedido.save_to_db()
        
        return {"message": "Categoria criado com sucesso!"}, 201
    
    