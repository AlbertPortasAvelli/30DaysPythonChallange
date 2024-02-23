from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - for demonstration purposes
items = [
    {"id": 1, "name": "Master Sword", "description": "Legendary sword capable of defeating evil"},
    {"id": 2, "name": "Hylian Shield", "description": "Shield imbued with the power to repel attacks"},
    {"id": 3, "name": "Boomerang", "description": "Projectile weapon that can stun enemies and retrieve items"},
    {"id": 4, "name": "Bomb", "description": "Explosive device useful for breaking through obstacles"},
    {"id": 5, "name": "Bow", "description": "Ranged weapon capable of firing arrows at enemies"},
    {"id": 6, "name": "Hookshot", "description": "Tool that can latch onto objects and pull the user towards them"},
    {"id": 7, "name": "Triforce", "description": "Sacred relic consisting of three golden triangles representing power, wisdom, and courage"}
]
next_item_id = 8

# Routes
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/items', methods=['POST'])
def create_item():
    global next_item_id
    data = request.json
    new_item = {"id": next_item_id, "name": data["name"], "description": data["description"]}
    items.append(new_item)
    next_item_id += 1
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    for item in items:
        if item['id'] == item_id:
            item['name'] = data.get('name', item['name'])
            item['description'] = data.get('description', item['description'])
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
