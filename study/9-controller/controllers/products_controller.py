from flask import request, jsonify

# Dummy Data
products = [{"id": 1, "name": "Laptop", "category_id": 1}, {"id": 2, "name": "T-Shirt", "category_id": 2}]

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
