from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Dummy "sessions" database
sessions = {}

# ----- AUTHORIZATION -----
@app.route('/connect', methods=['POST'])
def connect():
    data = request.json
    # (Optional: validate auth_key here)
    session_key = uuid.uuid4().hex
    sessions[session_key] = {
        "mode": data.get("mode"),
        "name": data.get("name")
    }
    return jsonify({"success": True, "session_key": session_key})

# ----- VOICE ASSISTANTS -----
@app.route('/link', methods=['POST'])
def link():
    data = request.json
    session_key = data.get("session_key")
    if session_key not in sessions:
        return jsonify({"success": False, "message": "Invalid session"}), 401
    return jsonify({
        "host": "eigensol.com",
        "port": 4401,
        "protocol": "wss://",
        "success": True
    })

# ----- CHATBOTS -----
@app.route('/verify', methods=['POST'])
def verify():
    data = request.json
    session_key = data.get("session_key")
    if session_key in sessions:
        return jsonify({"success": True})
    else:
        return jsonify({
            "success": False,
            "code": 3,
            "message": "Session timed out. please start new session"
        }), 401

@app.route('/message', methods=['POST'])
def message():
    data = request.json
    session_key = data.get("session_key")
    if session_key not in sessions:
        return jsonify({"success": False, "message": "Invalid session"}), 401
    msg = data.get("message", "")
    # Just echo the message for demo purpose
    return jsonify({"success": True, "reply": f"You said: {msg}"})

@app.route('/data', methods=['POST'])
def data():
    data = request.json
    session_key = data.get("session_key")
    if session_key not in sessions:
        return jsonify({"success": False}), 401
    # Store or process payload if needed (not implemented)
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)
