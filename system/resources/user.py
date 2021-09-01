
from model.user import UserModel
from flask_restful import Resource, reqparse

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

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "Este usuário já existe no sistema"},400
        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "Usuário criado com sucesso!"}, 201
