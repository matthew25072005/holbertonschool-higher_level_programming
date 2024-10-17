#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# Almacenar usuarios en un diccionario
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    """Root endpoint that returns a welcome message"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_users():
    """Returns a list of all usernames in the API"""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Returns a status message"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Returns the user data for the given username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the API"""
    data = request.get_json()

    # Verifica si el nombre de usuario está presente
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    
    # Agregar el usuario al diccionario
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
