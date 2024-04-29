from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy  # Import for database operations

from models import State

# Define the Blueprint object
states = Blueprint('states', __name__, url_prefix='/api/v1/states')

# Define route for getting all states
@states.route('/', methods=['GET'])
def get_states():
  """
  Get a list of all State objects
  """
  states = State.query.all()
  return jsonify([state.to_dict() for state in states])

# Define route for getting a specific state by ID
@states.route('/<state_id>', methods=['GET'])
def get_state(state_id):
  """
  Get a specific State object by ID
  """
  state = State.query.get(state_id)
  if not state:
    return jsonify({'error': 'Not found'}), 404
  return jsonify(state.to_dict())

# Define route for creating a new State
@states.route('/', methods=['POST'])
def create_state():
  """
  Create a new State object
  """
  # Get data from the request body
  data = request.get_json()

  # Check for valid JSON and required field 'name'
  if not data:
    return jsonify({'error': 'Not a JSON'}), 400
  if 'name' not in data:
    return jsonify({'error': 'Missing name'}), 400

  # Create a new State object
  new_state = State(name=data['name'])

  # Save the State to the database
  db.session.add(new_state)
  db.session.commit()

  # Return the newly created State with status code 201
  return jsonify(new_state.to_dict()), 201

# Define route for updating a State
@states.route('/<state_id>', methods=['PUT'])
def update_state(state_id):
  """
  Update a specific State object
  """
  # Get the State object by ID
  state = State.query.get(state_id)
  if not state:
    return jsonify({'error': 'Not found'}), 404

  # Get data from the request body
  data = request.get_json()

  # Check for valid JSON
  if not data:
    return jsonify({'error': 'Not a JSON'}), 400

  # Update the State object with data (excluding id, created_at, updated_at)
  for key, value in data.items():
    if key not in ['id', 'created_at', 'updated_at']:
      setattr(state, key, value)

  # Save the updated State to the database
  db.session.add(state)
  db.session.commit()

  # Return the updated State
  return jsonify(state.to_dict())

# Define route for deleting a State
@states.route('/<state_id>', methods=['DELETE'])
def delete_state(state_id):
  """
  Delete a specific State object
  """
  # Get the State object by ID
  state = State.query.get(state_id)
  if not state:
    return jsonify({'error': 'Not found'}), 404

  # Delete the State from the database
  db.session.delete(state)
  db.session.commit()

  # Return an empty dictionary with status code 200
  return jsonify({}), 200