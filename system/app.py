from flask import Flask , session, make_response, request, render_template, redirect, send_from_directory, jsonify
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
from contextlib import closing

import werkzeug
import json
import simplejson

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

@app.route("/")
def raiz():
    produto = ProdutoList()
    categoria = CategoriaList()
    listaProdutos = produto.get()
    listaCategorias = categoria.get()
    
    return render_template("index.html", produtos = listaProdutos, categorias = listaCategorias)

@app.route("/confirmProduto",methods=["POST","GET"])
def confirmProduto():
    if request.method == 'POST':
        produto = Produto()
        onlyProduto = produto.get(request.form['userid'])
        employeelist = []
    return jsonify({'htmlresponse': render_template('confirmProduto.html',produto=onlyProduto)})

@app.route("/cart",methods=["POST","GET"])
def cart():
    # name = request.cookies.get('name')
    try:
        produtos = session['cart']
        return render_template("cart.html",carrinho=produtos)
    except Exception as error:
        return render_template("cart.html")
    # teste = simplejson.loads(str(name))
    # return render_template("cart.html")

@app.route("/addCart",methods=["POST","GET"])
def addCart():
    id = request.args.get('id')
    if 'cart' not in session:
        session['cart'] = []  # 
    cart_list = session['cart']

    count = 0
    for x in cart_list:
        count = count +1
        if x['id'] == request.form['id']:
            return {'message': 'Este produto já foi adicionado ao carrinho'}, 400
        

    cart_list.append({"id": request.form['id'], "nome": request.form['nome'], "qtd": request.form['qtd'], "preco": request.form['preco'], "obs": request.form['obs']})
    session['cart'] = cart_list  # 
    return session

@app.route("/minusProduto",methods=["POST","GET"])
def minusProduto():
    cart_list = session['cart']
    count = 0
    for x in cart_list:
        if x['id'] == request.form['id']:
            count= count +1 
            
            return {'message': 'Este produto já foi adicionado ao carrinho'}, 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
