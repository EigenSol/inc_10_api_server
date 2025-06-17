from flask import request, jsonify

# Dummy Data
users = [{"id": 1, "name": "Ali"}, {"id": 2, "name": "Sara"}]
categories = [{"id": 1, "name": "Electronics"}, {"id": 2, "name": "Clothing"}]
products = [{"id": 1, "name": "Laptop", "category_id": 1}, {"id": 2, "name": "T-Shirt", "category_id": 2}]
orders = [{"id": 1, "user_id": 1, "product_ids": [1]}, {"id": 2, "user_id": 2, "product_ids": [2]}]

# ---- USERS ----
def get_users(): return jsonify(users)
def get_user(user_id): return jsonify(next((u for u in users if u['id'] == user_id), {}))
def create_user(): users.append(request.json); return jsonify(request.json), 201
def update_user(user_id):
    for u in users:
        if u['id'] == user_id:
            u.update(request.json)
            return jsonify(u)
    return {}, 404
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return '', 204

# ---- CATEGORIES ----
def get_categories(): return jsonify(categories)
def get_category(cat_id): return jsonify(next((c for c in categories if c['id'] == cat_id), {}))
def create_category(): categories.append(request.json); return jsonify(request.json), 201
def update_category(cat_id):
    for c in categories:
        if c['id'] == cat_id:
            c.update(request.json)
            return jsonify(c)
    return {}, 404
def delete_category(cat_id):
    global categories
    categories = [c for c in categories if c['id'] != cat_id]
    return '', 204
def get_products_by_category(cat_id): return jsonify([p for p in products if p['category_id'] == cat_id])

# ---- PRODUCTS ----
def get_products(): return jsonify(products)
def get_product(product_id): return jsonify(next((p for p in products if p['id'] == product_id), {}))
def create_product(): products.append(request.json); return jsonify(request.json), 201
def update_product(product_id):
    for p in products:
        if p['id'] == product_id:
            p.update(request.json)
            return jsonify(p)
    return {}, 404
def delete_product(product_id):
    global products
    products = [p for p in products if p['id'] != product_id]
    return '', 204
def search_products():
    q = request.args.get("name", "").lower()
    return jsonify([p for p in products if q in p['name'].lower()])

# ---- ORDERS ----
def get_orders(): return jsonify(orders)
def get_order(order_id): return jsonify(next((o for o in orders if o['id'] == order_id), {}))
def create_order(): orders.append(request.json); return jsonify(request.json), 201
def update_order(order_id):
    for o in orders:
        if o['id'] == order_id:
            o.update(request.json)
            return jsonify(o)
    return {}, 404
def delete_order(order_id):
    global orders
    orders = [o for o in orders if o['id'] != order_id]
    return '', 204
def get_orders_by_user(user_id): return jsonify([o for o in orders if o['user_id'] == user_id])
