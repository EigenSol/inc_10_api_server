from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return {'success': True}

app.run()
