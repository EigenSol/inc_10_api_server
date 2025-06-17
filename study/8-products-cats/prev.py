from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy Data
users = [{"id": 1, "name": "Ali"}, {"id": 2, "name": "Sara"}]
categories = [{"id": 1, "name": "Electronics"}, {"id": 2, "name": "Clothing"}]
products = [{"id": 1, "name": "Laptop", "category_id": 1}, {"id": 2, "name": "T-Shirt", "category_id": 2}]
orders = [{"id": 1, "user_id": 1, "product_ids": [1]}, {"id": 2, "user_id": 2, "product_ids": [2]}]

# ---- USERS ----
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(next((u for u in users if u['id'] == user_id), {}))

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for u in users:
        if u['id'] == user_id:
            u.update(data)
            return jsonify(u)
    return {}, 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return '', 204

# ---- CATEGORIES ----
@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(categories)

@app.route('/categories/<int:cat_id>', methods=['GET'])
def get_category(cat_id):
    return jsonify(next((c for c in categories if c['id'] == cat_id), {}))

@app.route('/categories', methods=['POST'])
def create_category():
    new_cat = request.json
    categories.append(new_cat)
    return jsonify(new_cat), 201

@app.route('/categories/<int:cat_id>', methods=['PUT'])
def update_category(cat_id):
    data = request.json
    for c in categories:
        if c['id'] == cat_id:
            c.update(data)
            return jsonify(c)
    return {}, 404

@app.route('/categories/<int:cat_id>', methods=['DELETE'])
def delete_category(cat_id):
    global categories
    categories = [c for c in categories if c['id'] != cat_id]
    return '', 204

@app.route('/categories/<int:cat_id>/products', methods=['GET'])
def get_products_by_category(cat_id):
    return jsonify([p for p in products if p['category_id'] == cat_id])

# ---- PRODUCTS ----
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return jsonify(next((p for p in products if p['id'] == product_id), {}))

@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.json
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    for p in products:
        if p['id'] == product_id:
            p.update(data)
            return jsonify(p)
    return {}, 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p['id'] != product_id]
    return '', 204

@app.route('/products/search', methods=['GET'])
def search_products():
    q = request.args.get("name")
    return jsonify([p for p in products if q.lower() in p['name'].lower()])

# ---- ORDERS ----
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return jsonify(next((o for o in orders if o['id'] == order_id), {}))

@app.route('/orders', methods=['POST'])
def create_order():
    new_order = request.json
    orders.append(new_order)
    return jsonify(new_order), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.json
    for o in orders:
        if o['id'] == order_id:
            o.update(data)
            return jsonify(o)
    return {}, 404

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    global orders
    orders = [o for o in orders if o['id'] != order_id]
    return '', 204

@app.route('/users/<int:user_id>/orders', methods=['GET'])
def get_orders_by_user(user_id):
    return jsonify([o for o in orders if o['user_id'] == user_id])

if __name__ == '__main__':
    app.run(debug=True)
