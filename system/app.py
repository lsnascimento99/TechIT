from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from flask_mysqldb import MySQL

from security import authenticate
from resources.user import UserRegister

app = Flask(__name__)
#Criando conexões com o banco de dados

api = Api(app)
#Chamando as Apis através dos endpoints
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
