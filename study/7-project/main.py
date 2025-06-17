from flask import Flask
from .handlers import home, all_posts, single_post

# Server
app = Flask(__name__)

# Routing Table
routes = {
  '/':               {'methods': ['GET'], 'function': home},
  '/posts':          {'methods': ['GET'], 'function': all_posts},
  '/posts/<int:id>': {'methods': ['GET'], 'function': single_post},
}

# Register Routes
for url, details in routes.items():
  app.add_url_rule(
    url       = url,
    view_func = details['function'],
    methods   = details['methods'],
  )

# Start server
app.run()
