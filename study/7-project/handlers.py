from flask import abort

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
