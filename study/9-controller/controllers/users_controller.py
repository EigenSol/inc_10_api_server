from flask import request, jsonify

# Dummy Data
users = [{"id": 1, "name": "Ali"}, {"id": 2, "name": "Sara"}]

# ---- USERS ----

class UsersController:

    @staticmethod
    def get_users():
        """GET /users - Return list of all users"""
        return jsonify(users)

    @staticmethod
    def get_user(user_id):
        """GET /users/<user_id> - Return a single user by ID"""
        return jsonify(next((u for u in users if u['id'] == user_id), {}))

    @staticmethod
    def create_user():
        """POST /users - Create a new user"""
        users.append(request.json)
        return jsonify(request.json), 201

    @staticmethod
    def update_user(user_id):
        """PUT /users/<user_id> - Update an existing user"""
        for u in users:
            if u['id'] == user_id:
                u.update(request.json)
                return jsonify(u)
        return {}, 404

    @staticmethod
    def delete_user(user_id):
        """DELETE /users/<user_id> - Delete a user by ID"""
        global users
        users = [u for u in users if u['id'] != user_id]
        return '', 204
