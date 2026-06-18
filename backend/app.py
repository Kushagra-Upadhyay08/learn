
"""Hello gues"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

PORT = int(os.getenv('PORT', 5001))

# In-memory database
names = [
    {'id': 1, 'name': 'John', 'age': 25},
    {'id': 2, 'name': 'Sarah', 'age': 30},
    {'id': 3, 'name': 'Mike', 'age': 28}
]

next_id = 4


# Root route
@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'healthy', 'message': 'Names & Ages Manager API is running'})


# Get all names
@app.route('/api/names', methods=['GET'])
def get_all_names():
    return jsonify(names)


# Add new name
@app.route('/api/names', methods=['POST'])
def add_name():
    global next_id
    data = request.get_json()

    if not data or not data.get('name') or not data.get('age'):
        return jsonify({'error': 'Name and age are required'}), 400

    try:
        age = int(data.get('age'))
    except ValueError:
        return jsonify({'error': 'Age must be a number'}), 400

    new_entry = {
        'id': next_id,
        'name': data.get('name'),
        'age': age
    }

    names.append(new_entry)
    next_id += 1
    return jsonify(new_entry), 201


# Search by name or age
@app.route('/api/names/search', methods=['GET'])
def search_names():
    search_name = request.args.get('name', '').lower()
    search_age = request.args.get('age', '')

    results = names

    if search_name:
        results = [entry for entry in results if search_name in entry['name'].lower()]

    if search_age:
        try:
            search_age = int(search_age)
            results = [entry for entry in results if entry['age'] == search_age]
        except ValueError:
            return jsonify({'error': 'Age must be a number'}), 400

    return jsonify(results)


# Delete name
@app.route('/api/names/<int:id>', methods=['DELETE'])
def delete_name(id):
    global names
    entry = next((entry for entry in names if entry['id'] == id), None)

    if not entry:
        return jsonify({'error': 'Not found'}), 404

    names = [entry for entry in names if entry['id'] != id]
    return jsonify(entry)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
