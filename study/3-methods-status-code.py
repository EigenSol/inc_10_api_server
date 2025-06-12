from flask import Flask

app = Flask(__name__)

@app.route("/")
def func():
  return {
    'success': True
  }

@app.route("/", methods=["POST", "PUT"])
def func2():
  return {
    'success': False,
    'message': "There is an error on server, apologies for inconvience."
  }, 500

@app.route("/", methods=["DELETE", "PATCH"])
def func3():
  return {
    'success': False,
    'message': "We are working on this one ATM."
  }

app.run()