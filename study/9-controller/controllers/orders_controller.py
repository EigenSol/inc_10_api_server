from flask import request, jsonify

# Dummy Data
orders = [{"id": 1, "user_id": 1, "product_ids": [1]}, {"id": 2, "user_id": 2, "product_ids": [2]}]

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
