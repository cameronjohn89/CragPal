from flask import Blueprint, jsonify, request
from models.user import User, Collection
from database import db

# Create the blueprint for the user controller
user_controller = Blueprint('user_controller', __name__)

# Route for retrieving user profile


@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Retrieve the user details based on the provided user_id
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user)

# Route for updating user profile


@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Retrieve the user details based on the provided user_id
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    # Retrieve the data from the request
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    # Update the user details
    user.username = username
    user.email = email
    user.first_name = first_name
    user.last_name = last_name

    # Save the updated user to the database
    db.session.commit()

    return jsonify({'message': 'User profile updated successfully'})

# Route for creating a new collection


@user_controller.route('/users/<int:user_id>/collections', methods=['POST'])
def create_collection(user_id):
    # Retrieve the data from the request
    data = request.get_json()
    name = data.get('name')

    # Check if the user exists
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    # Create a new Collection instance
    collection = Collection(user_id=user_id, name=name)

    # Save the new collection to the database
    collection.save()

    return jsonify(collection), 201

# Add more routes and functionalities as needed
