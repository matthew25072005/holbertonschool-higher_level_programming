from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Clave secreta para generar JWT tokens

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Usuarios de ejemplo con roles y contraseñas hash
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Autenticación básica
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None

# Ruta protegida con autenticación básica
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})

# Login con JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Crear token JWT
    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify({"access_token": access_token})

# Ruta protegida con JWT
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    identity = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted", "user": identity})

# Ruta protegida solo para administradores
@app.route('/admin-only')
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})

# Manejo de errores para JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

if __name__ == "__main__":
    app.run(debug=True)
