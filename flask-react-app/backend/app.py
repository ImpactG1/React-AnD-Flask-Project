from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Sample data
items = [
    {"id": 1, "name": "Item 1", "description": "The first item"},
    {"id": 2, "name": "Item 2", "description": "The second item"},
    {"id": 3, "name": "Item 3", "description": "The third item"},
]

# Endpoint to fetch items with optional query parameter 'name'
@app.route('/api/items', methods=['GET'])
def get_items():
    name = request.args.get('name')  # Get the 'name' query parameter
    if name:
        filtered_items = [item for item in items if name.lower() in item['name'].lower()]
        return jsonify(filtered_items)
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
