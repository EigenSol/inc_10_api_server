from flask import Flask, abort

app = Flask(__name__)

def home():
  return {
    'success': True,
  }

def all_posts():
  return {
    'success': True,
    'posts': [
      {'id': 1, 'title': 'AI'},
      {'id': 2, 'title': 'CS'},
      {'id': 3, 'title': 'Prompt Egnineering'},
    ]
  }

def single_post(id):

  if id > 100:
    abort(404)

  return {
    'success': True,
    'post': {
      'id': id,
      'title': f'Post {id}'
    },
  }

routes = {
  '/':               {'methods': ['GET'], 'function': home},
  '/posts':          {'methods': ['GET'], 'function': all_posts},
  '/posts/<int:id>': {'methods': ['GET'], 'function': single_post},
}

for url, details in routes.items():

  func = details['function']
  methods = details['methods']

  app.add_url_rule(
    url       = url,
    view_func = func,
    methods   = methods,
  )


app.run()
