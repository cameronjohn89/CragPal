from flask import Blueprint, jsonify, request
from models.route import Route
from models.climb import Climb
from models.user import User
from database import db

route_controller = Blueprint('route_controller', __name__)


@route_controller.route('/routes', methods=['POST'])
def create_route():
    # Retrieve the data from the request
    data = request.get_json()
    crag_id = data.get('crag_id')
    user_id = data.get('user_id')
    name = data.get('name')
    difficulty_level = data.get('difficulty_level')
    route_type = data.get('type')
    description = data.get('description')

    # Check if the crag and user exist
    crag = Crag.query.get(crag_id)
    user = User.query.get(user_id)
    if crag is None or user is None:
        return jsonify({'error': 'Crag or user not found'}), 404

    # Create a new Route instance
    route = Route(crag_id=crag_id, user_id=user_id, name=name, difficulty_level=difficulty_level,
                  type=route_type, description=description)

    # Save the new route to the database
    db.session.add(route)
    db.session.commit()

    return jsonify({'message': 'Route created successfully'})


@route_controller.route('/routes/<int:route_id>', methods=['GET'])
def get_route(route_id):
    # Retrieve the route details based on the provided route_id
    route = Route.query.get(route_id)
    if route is None:
        return jsonify({'error': 'Route not found'}), 404

    return jsonify(route)


@route_controller.route('/routes/<int:route_id>/climbs', methods=['POST'])
def log_climb(route_id):
    # Retrieve the data from the request
    data = request.get_json()
    user_id = data.get('user_id')
    date = data.get('date')
    notes = data.get('notes')

    # Check if the route and user exist
    route = Route.query.get(route_id)
    user = User.query.get(user_id)
    if route is None or user is None:
        return jsonify({'error': 'Route or user not found'}), 404

    # Create a new Climb instance
    climb = Climb(route_id=route_id, user_id=user_id, date=date, notes=notes)

    # Save the new climb to the database
    db.session.add(climb)
    db.session.commit()

    return jsonify({'message': 'Climb logged successfully'})

# Add more routes and functionalities as needed
