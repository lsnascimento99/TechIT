from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_mysqldb import MySQL
from security import authenticate , identity
from resources.user import UserRegister
from resources.categoria import CategoriaList, CategoriaMaintenance
from resources.categoria import Categoria
from resources.statusPedido import Status
from resources.produto import Produto, ProdutoList
from resources.produto import ProdutoMaintenance
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#Criando conexões com o banco de dados
app.secret_key = 'techit'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # Criação do endpoint  /auth
#Chamando as Apis através dos endpoints
api.add_resource(UserRegister, '/register')
api.add_resource(CategoriaList, '/categoria/list')   
api.add_resource(Categoria, '/categoria')   
api.add_resource(CategoriaMaintenance, '/categoria/maintenance/<string:id>')   
api.add_resource(Produto, '/produto')   
api.add_resource(ProdutoList, '/produto/list')   
api.add_resource(ProdutoMaintenance, '/produto/maintenance/<string:id>')   
api.add_resource(Status, '/pedido/status')   
# api.add_resource(Status, '/pedido')   


if __name__ == '__main__':
    app.run(port=5000, debug=True)
