from flask import Flask, abort

app = Flask(__name__)

@app.route('/', methods=['GET'])
def func():
  return {
    'success': True,
  }

@app.route('/posts', methods=['GET'])
def func3():
  return {
    'success': True,
    'posts': [
      {'id': 1, 'title': 'AI'},
      {'id': 2, 'title': 'CS'},
      {'id': 3, 'title': 'Prompt Egnineering'},
    ]
  }

@app.route('/posts/1', methods=['GET'])
def func2():
  return {
    'success': True,
    'post': {
      'id': 1,
      'title': 'AI'
    },
  }

@app.route('/posts/<int:id>', methods=['GET'])
def func4(id):

  # id = int(id)

  if id > 100:
    abort(404)

  return {
    'success': True,
    'post': {
      'id': id,
      'title': f'Post {id}'
    },
  }



app.run()