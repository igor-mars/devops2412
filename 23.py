from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (in-memory storage)
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]

# Routes for CRUD operations

# Retrieve all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# Retrieve a specific item by ID
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is not None:
        return jsonify(item)
    return "Item not found", 404

# Create a new item
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    if "name" in data:
        new_item = {"id": len(items) + 1, "name": data["name"]}
        items.append(new_item)
        return jsonify(new_item), 201
    return "Invalid data", 400

# Update an existing item by ID
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    item = next((item for item in items if item["id"] == item_id), None)
    if item is not None and "name" in data:
        item["name"] = data["name"]
        return jsonify(item)
    return "Item not found or invalid data", 404

# Delete an item by ID
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is not None:
        items.remove(item)
        return "", 204  # No content
    return "Item not found", 404

if __name__ == "__main__":
    app.run(host="localhost", port="8080", debug=True)
