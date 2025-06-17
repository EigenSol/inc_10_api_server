from flask import request, jsonify

# Dummy Data
categories = [{"id": 1, "name": "Electronics"}, {"id": 2, "name": "Clothing"}]
products = [{"id": 1, "name": "Laptop", "category_id": 1}, {"id": 2, "name": "T-Shirt", "category_id": 2}]

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
