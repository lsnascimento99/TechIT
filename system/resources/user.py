
from model.user import UserModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="O Campo username não pode estar em branco."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="O Campo password não pode estar em branco"
                        )
    # @jwt_required()
    def post(self):
        #Função post para registro de usuário
        data = UserRegister.parser.parse_args()
        #Função para verificar se o usuário já existe no bano de dados
        if UserModel.find_by_username(data['username']):
            #caso não existir retorno a mensagem abaixo
            return {"message": "Este usuário já existe no sistema"},400
        #chamando a classe para gravar o usuário no banco de dados
        user = UserModel(False, data['username'], data['password'])
        user.save_to_db()

        return {"message": "Usuário criado com sucesso!"}, 201
