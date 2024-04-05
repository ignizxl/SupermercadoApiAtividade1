from flask import Flask, request, jsonify
from database import products_array, users_array, sectors_array, categories_array

app = Flask(__name__)

@app.route('/')
def index():
  return "Learning Flask"

#endpoint: /products
#requisição: get (Listagem de todos os produtos)
#requisição: post (Criar um novo produto e adicionar no products_array)

@app.route('/products', methods=["GET", "POST"])
def products():
  if (request.method == "POST"):
    new_product = request.get_json()
    products_array.append(new_product)
    return jsonify({"message" : "Produto adicionado com sucesso!", "Produto" : new_product}), 201
  
  elif (request.method == "GET"):
    return jsonify({"Products" : products_array })
  
#endpoint   : /products/<int:id>
#get_product()  : Buscar um produto pelo id
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
  for product in products_array:
    if (product['id'] == id):
      return jsonify(product)
  return jsonify({"message": "Produto não encontrado"}), 404

#--------------------------------------------------------------------------------------------------

#endpoint: /users
#requisição: get (Listagem de todos os usuários)
#requisição: post (Criar um novo usuário e adicionar no users_array)

@app.route('/users', methods=["GET", "POST"])
def users():
  if (request.method == "POST"):
    new_user = request.get_json()
    users_array.append(new_user)
    return jsonify({"message" : "Usuário adicionado com sucesso!", "Usuário" : new_user}), 201
  
  elif (request.method == "GET"):
    return jsonify({"Users" : users_array })

#endpoint   : /users/<int:id>
#get_user()  : Buscar um usuário pelo id
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
  for user in users_array:
    if (user['id'] == id):
      return jsonify(user)
  return jsonify({"message": "Usuário não encontrado"}), 404

#--------------------------------------------------------------------------------------------------

#endpoint: /sectors
#requisição: get (Listagem de todos os setores)
#requisição: post (Criar um novo usuário e adicionar no sectors_array)
  
@app.route('/sectors', methods=["GET", "POST"])
def sectors():
  if (request.method == "POST"):
    new_sector = request.get_json()
    sectors_array.append(new_sector)
    return jsonify({"message" : "Setor adicionado com sucesso!", "Setor" : new_sector}), 201
  
  elif (request.method == "GET"):
   return jsonify({"Sectors" : sectors_array })

#endpoint   : /sectors/<int:id>
#get_sector()  : Buscar um setor pelo id
@app.route('/sectors/<int:id>', methods=['GET'])
def get_sector(id):
  for sector in sectors_array:
    if (sector['id'] == id):
      return jsonify(sector)
  return jsonify({"message": "Setor não encontrado"}), 404

#--------------------------------------------------------------------------------------------------

#endpoint: /categories
#requisição: get (Listagem de todas as categorias)
#requisição: post (Criar uma nova categoria e adicionar no categories_array)

@app.route('/categories', methods=["GET", "POST"])
def categories():
  if (request.method == "POST"):
    new_categorie = request.get_json()
    categories_array.append(new_categorie)
    return jsonify({"message" : "Categoria adicionado com sucesso!", "Categoria" : new_categorie}), 201
  
  elif (request.method == "GET"):
   return jsonify({"Categories" : categories_array })

#endpoint   : /categories/<int:id>
#get_categorie()  : Buscar uma categoria pelo id
@app.route('/categories/<int:id>', methods=['GET'])
def get_categorie(id):
  for categorie in categories_array:
    if (categorie['id'] == id):
      return jsonify(categorie)
  return jsonify({"message": "Categoria não encontrada"}), 404

if (__name__ == "__main__"):
  app.run(debug=True)