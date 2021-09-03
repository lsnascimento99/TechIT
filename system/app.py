from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_mysqldb import MySQL
from security import authenticate , identity
from resources.user import UserRegister

app = Flask(__name__)
#Criando conexões com o banco de dados
app.secret_key = 'techit'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # Criação do endpoint  /auth
#Chamando as Apis através dos endpoints
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
