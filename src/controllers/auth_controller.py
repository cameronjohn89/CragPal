from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from database import db

# Create the blueprint for the auth controller
auth_controller = Blueprint('auth_controller', __name__)

# Route for user registration


@auth_controller.route('/register', methods=['POST'])
def register():
    # Retrieve the data from the request
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    # Check if the username or email already exists
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': 'Username already exists'}), 400

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error': 'Email already exists'}), 400

    # Hash the password for security
    hashed_password = generate_password_hash(password)

    # Create a new User instance
    user = User(username=username, email=email, password=hashed_password,
                first_name=first_name, last_name=last_name)

    # Save the new user to the database
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Registration successful'})

# Route for user login


@auth_controller.route('/login', methods=['POST'])
def login():
    # Retrieve the data from the request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Retrieve the user from the database based on the username
    user = User.query.filter_by(username=username).first()

    # Check if the user exists and the password is correct
    if user is None or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid username or password'}), 401

    # Return a success message or an access token for authentication

    return jsonify({'message': 'Login successful'})

# Add more routes and functionalities as needed
