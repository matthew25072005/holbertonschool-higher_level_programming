from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulamos la base de datos de usuarios
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Ruta para la raíz de la aplicación
@app.route('/')
def home():
    """Muestra un mensaje de bienvenida."""
    return "Welcome to the Flask API!"

# Ruta para devolver el estado del API
@app.route('/status')
def status():
    """Devuelve un mensaje OK indicando que el servidor está activo."""
    return "OK"

# Ruta para devolver la lista de usuarios
@app.route('/data')
def get_data():
    """Devuelve la lista de nombres de usuario."""
    return jsonify(list(users.keys()))

# Ruta para obtener los detalles de un usuario
@app.route('/users/<username>')
def get_user(username):
    """Devuelve los detalles del usuario dado el nombre de usuario."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Ruta para agregar un nuevo usuario (método POST)
@app.route('/add_user', methods=['POST'])
def add_user():
    """Agrega un nuevo usuario a la base de datos simulada."""
    data = request.get_json()

    # Verifica si el cuerpo de la solicitud es válido
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    # Verifica que todos los campos necesarios estén presentes
    if "username" not in data or not data.get("username"):
        return jsonify({"error": "Username is required"}), 400
    if "name" not in data or not data.get("name"):
        return jsonify({"error": "Name is required"}), 400
    if "age" not in data or not data.get("age"):
        return jsonify({"error": "Age is required"}), 400
    if "city" not in data or not data.get("city"):
        return jsonify({"error": "City is required"}), 400

    username = data["username"]
    
    # Verifica si el usuario ya existe
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Agregamos el nuevo usuario
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
