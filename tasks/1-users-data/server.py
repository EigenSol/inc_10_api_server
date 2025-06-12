from flask import Flask

app  = Flask(__name__)

@app.route('/')
def index():
    return {'success' : True}

@app.route('/users')
def user():
    return {'Name': 'Ali'}

app.run()


