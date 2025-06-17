from flask import Flask

# from controllers.users_controller import get_users, create_user, get_user, update_user, delete_user
from controllers.users_controller import UsersController
from controllers.categories_controller import get_categories, create_category, get_category, update_category, delete_category, get_products_by_category
from controllers.products_controller import get_products, create_product, get_product, update_product, delete_product, search_products
from controllers.orders_controller import get_orders, create_order, get_order, update_order, delete_order, get_orders_by_user

# Server
app = Flask(__name__)

# Routing Table
routes = [

    # ---- USERS ----
    {'url': '/users',                     'methods': ['GET'],    'function': UsersController.get_users},
    {'url': '/users',                     'methods': ['POST'],   'function': UsersController.create_user},
    {'url': '/users/<int:user_id>',       'methods': ['GET'],    'function': UsersController.get_user},
    {'url': '/users/<int:user_id>',       'methods': ['PUT'],    'function': UsersController.update_user},
    {'url': '/users/<int:user_id>',       'methods': ['DELETE'], 'function': UsersController.delete_user},

    # ---- CATEGORIES ----
    {'url': '/categories',                        'methods': ['GET'],    'function': get_categories},
    {'url': '/categories',                        'methods': ['POST'],   'function': create_category},
    {'url': '/categories/<int:cat_id>',           'methods': ['GET'],    'function': get_category},
    {'url': '/categories/<int:cat_id>',           'methods': ['PUT'],    'function': update_category},
    {'url': '/categories/<int:cat_id>',           'methods': ['DELETE'], 'function': delete_category},
    {'url': '/categories/<int:cat_id>/products',  'methods': ['GET'],    'function': get_products_by_category},

    # ---- PRODUCTS ----
    {'url': '/products',                    'methods': ['GET'],    'function': get_products},
    {'url': '/products',                    'methods': ['POST'],   'function': create_product},
    {'url': '/products/<int:product_id>',   'methods': ['GET'],    'function': get_product},
    {'url': '/products/<int:product_id>',   'methods': ['PUT'],    'function': update_product},
    {'url': '/products/<int:product_id>',   'methods': ['DELETE'], 'function': delete_product},
    {'url': '/products/search',             'methods': ['GET'],    'function': search_products},

    # ---- ORDERS ----
    {'url': '/orders',                     'methods': ['GET'],    'function': get_orders},
    {'url': '/orders',                     'methods': ['POST'],   'function': create_order},
    {'url': '/orders/<int:order_id>',      'methods': ['GET'],    'function': get_order},
    {'url': '/orders/<int:order_id>',      'methods': ['PUT'],    'function': update_order},
    {'url': '/orders/<int:order_id>',      'methods': ['DELETE'], 'function': delete_order},
    {'url': '/users/<int:user_id>/orders', 'methods': ['GET'],    'function': get_orders_by_user},
]

# Register Routes
for route in routes:
    app.add_url_rule(
        route['url'],
        view_func=route['function'],
        methods=route['methods']
    )

# Start server
app.run(debug=True)
