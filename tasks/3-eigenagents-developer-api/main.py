from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/my')
def index():
    return {"success" : True}