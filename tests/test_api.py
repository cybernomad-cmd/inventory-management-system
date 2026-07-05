import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True

    with app.test_client() as client:
        yield client
        
def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Welcome to the Inventory Management System API"
    }
    
def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
    
def test_inventory_item_not_found(client):
    response = client.get("/inventory/999")

    assert response.status_code == 404

    assert response.get_json() == {
        "error": "Inventory item not found"
    }
    
def test_add_inventory_item(client):
    new_item = {
        "barcode": "123456789",
        "product_name": "Milk",
        "brand": "Brookside",
        "price": 150,
        "stock": 20
    }

    response = client.post("/inventory", json=new_item)
    assert response.status_code == 201
    data = response.get_json()
    assert data["product_name"] == "Milk"
    
def test_update_inventory_item(client):
    updates = {
        "price": 175,
        "stock": 40
    }

    response = client.patch("/inventory/1", json=updates)
    assert response.status_code == 200
    data = response.get_json()

    assert data["price"] == 175
    assert data["stock"] == 40
    
def test_delete_inventory_item(client):
    response = client.delete("/inventory/3")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Inventory item deleted successfully"
    }
    
def test_get_product_from_api(client):
    response = client.get("/product/3017620422003")

    assert response.status_code == 200
    data = response.get_json()

    assert data["barcode"] == "3017620422003"
    assert "product_name" in data
    
