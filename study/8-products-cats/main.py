from flask import Flask
from handlers import get_users, create_user, get_user, update_user, delete_user, \
  get_categories, create_category, get_category, update_category, delete_category, \
  get_products_by_category, get_products, create_product, get_product, update_product, \
  delete_product, search_products, get_orders, create_order, get_order, update_order, \
  delete_order, get_orders_by_user

# Server
app = Flask(__name__)

# Routing Table
routes = {
    # ---- USERS ----
    '/users':                     {'methods': ['GET'],    'function': get_users},
    '/users':                     {'methods': ['POST'],   'function': create_user},
    '/users/<int:user_id>':       {'methods': ['GET'],    'function': get_user},
    '/users/<int:user_id>':       {'methods': ['PUT'],    'function': update_user},
    '/users/<int:user_id>':       {'methods': ['DELETE'], 'function': delete_user},

    # ---- CATEGORIES ----
    '/categories':                        {'methods': ['GET'],    'function': get_categories},
    '/categories':                        {'methods': ['POST'],   'function': create_category},
    '/categories/<int:cat_id>':           {'methods': ['GET'],    'function': get_category},
    '/categories/<int:cat_id>':           {'methods': ['PUT'],    'function': update_category},
    '/categories/<int:cat_id>':           {'methods': ['DELETE'], 'function': delete_category},
    '/categories/<int:cat_id>/products':  {'methods': ['GET'],    'function': get_products_by_category},

    # ---- PRODUCTS ----
    '/products':                    {'methods': ['GET'],    'function': get_products},
    '/products':                    {'methods': ['POST'],   'function': create_product},
    '/products/<int:product_id>':   {'methods': ['GET'],    'function': get_product},
    '/products/<int:product_id>':   {'methods': ['PUT'],    'function': update_product},
    '/products/<int:product_id>':   {'methods': ['DELETE'], 'function': delete_product},
    '/products/search':             {'methods': ['GET'],    'function': search_products},

    # ---- ORDERS ----
    '/orders':                     {'methods': ['GET'],    'function': get_orders},
    '/orders':                     {'methods': ['POST'],   'function': create_order},
    '/orders/<int:order_id>':      {'methods': ['GET'],    'function': get_order},
    '/orders/<int:order_id>':      {'methods': ['PUT'],    'function': update_order},
    '/orders/<int:order_id>':      {'methods': ['DELETE'], 'function': delete_order},
    '/users/<int:user_id>/orders': {'methods': ['GET'],    'function': get_orders_by_user},
}

# Register Routes
for url, details in routes.items():
    app.add_url_rule(
      url,
      view_func=details['function'],
      methods=details['methods']
    )

# Start server
app.run(debug=True)
