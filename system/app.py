from flask import Flask, session, url_for, make_response, request, render_template, redirect, send_from_directory, jsonify
from flask_restful import Api
from flask_jwt import JWT
from flask_mysqldb import MySQL
from security import authenticate, identity
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
# Criando conexões com o banco de dados
app.secret_key = 'techit'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # Criação do endpoint  /auth
# Chamando as Apis através dos endpoints
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
    try:
        carrinho = session['cart']
    except Exception as error:
        carrinho = []
    
    ValorTotal = 0
    ValorTotal = float(ValorTotal)
    for x in carrinho:
        ValorTotal = ValorTotal + float(x['precoTotal'])
    try:
        session['valorTotal'] = ValorTotal
    except Exception as error:
        ValorTotal




    return render_template("index.html", produtos=listaProdutos, categorias=listaCategorias, carrinho = ValorTotal)


@app.route("/confirmProduto", methods=["POST", "GET"])
def confirmProduto():
    if request.method == 'POST':
        produto = Produto()
        onlyProduto = produto.get(request.form['userid'])
        employeelist = []
    return jsonify({'htmlresponse': render_template('confirmProduto.html', produto=onlyProduto)})


@app.route("/cart", methods=["POST", "GET"])
def cart():
    # name = request.cookies.get('name')
    try:
        produtos = session['cart']
        qtdTotal = len(session['cart'])
        ValorTotal = 0
        ValorTotal = float(ValorTotal)
        for x in produtos:
            ValorTotal = ValorTotal + float(x['precoTotal'])
        session['valorTotal'] = ValorTotal
        return render_template("cart.html", carrinho=produtos, qtdCarrinho = qtdTotal, total = ValorTotal )

    except Exception as error:
        return render_template("cart.html",carrinho='', qtdCarrinho = 0, total = 0)
    # teste = simplejson.loads(str(name))
    # return render_template("cart.html")
    
@app.route("/addCart", methods=["POST", "GET"])
def addCart():
    id = request.args.get('id')
    if 'cart' not in session:
        session['cart'] = []  #
    cart_list = session['cart']

    count = 0
    for x in cart_list:
        count = count + 1
        if x['id'] == request.form['id']:
            return {'message': 'Este produto já foi adicionado ao carrinho'}, 400

    cart_list.append({"id": request.form['id'], "nome": request.form['nome'],
                     "qtd": request.form['qtd'], "preco": request.form['preco'], "precoTotal":request.form['precoTotal'], "obs": request.form['obs']})
    session['cart'] = cart_list  #
    return session


@app.route("/calcProduto", methods=["POST", "GET"])
def calcProduto():
    cart_list = session['cart']
    count = 0
    if request.form['sinal'] == '-':
        for x in cart_list:
            if x['id'] == request.form['id']:
                qtd = x['qtd']
                qtd = int(qtd)
                if qtd == 1:
                    preco = session['cart'][count]['preco'] 
                    del session['cart'][count]
                    session.modified = True
                    preco = float(preco)
                    qtd = 0
                    session['valorTotal'] = session['valorTotal'] - preco
                    if session['valorTotal'] <= 0:
                        session['valorTotal'] = 0

                    return {"quantidade":qtd, "total":session['valorTotal']},200
                    exit
                else:
                    qtd = x['qtd']
                    qtd = int(qtd)
                    precoTotal = x['precoTotal']
                    preco = x['preco']
                    preco = float(preco)
                    precoTotal = float(precoTotal)
                    session['cart'][count]['qtd'] = qtd - 1
                    session.modified = True
                    qtd = qtd - 1
                    session['cart'][count]['precoTotal'] = precoTotal - preco
                    session.modified = True
                    precoTotal = precoTotal - preco 
                    session['valorTotal'] = session['valorTotal'] - preco
                    if session['valorTotal'] <= 0:
                        session['valorTotal'] = 0
                    
            count = count+1
    else:
        for x in cart_list:
                
            if x['id'] == request.form['id']:
                qtd = x['qtd']
                qtd = int(qtd)
                precoTotal = x['precoTotal']
                preco = x['preco']
                preco = float(preco)
                precoTotal = float(precoTotal)
                session['cart'][count]['qtd'] = qtd + 1
                qtd = qtd + 1
                session['cart'][count]['precoTotal'] = precoTotal +preco
                session['valorTotal'] = session['valorTotal'] + preco
                if session['valorTotal'] <= 0:
                    session['valorTotal'] = 0

                precoTotal = precoTotal + preco
                session.modified = True
                
            count = count+1
    return {"quantidade": qtd, "id": request.form['id'], "precoTotal":precoTotal, "total":session['valorTotal']},200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
