from urllib import response

from flask import Flask, jsonify, request
import requests
from data import inventory

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Inventory Management System API"
    }), 200

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200

@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200

    return jsonify({
        "error": "Inventory item not found"
    }), 404

@app.route("/inventory", methods=["POST"])
def add_inventory_item():
    new_item = request.get_json()
    new_item["id"] = len(inventory) + 1
    inventory.append(new_item)

    return jsonify(new_item), 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):
    updates = request.get_json()

    for item in inventory:
        if item["id"] == item_id:
            item.update(updates)
            return jsonify(item), 200

    return jsonify({
        "error": "Inventory item not found"
    }), 404
    
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({
                "message": "Inventory item deleted successfully"
            }), 200

    return jsonify({
        "error": "Inventory item not found"
    }), 404
    
@app.route("/product/<barcode>", methods=["GET"])
def get_product_from_api(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    headers = {
        "User-Agent": "InventoryManagementSystem/1.0 (student project)"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    print("=" * 50)
    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print(response.text[:500])
    print("=" * 50)

    data = response.json()

    if data.get("status") == 0:
        return jsonify({
            "error": "Product not found"
        }), 404

    product = data.get("product", {})

    return jsonify({
        "barcode": barcode,
        "product_name": product.get("product_name", "N/A"),
        "brand": product.get("brands", "N/A"),
        "ingredients": product.get("ingredients_text", "N/A")
    }), 200




if __name__ == "__main__":
    app.run(debug=True)