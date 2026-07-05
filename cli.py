import requests

BASE_URL = "http://127.0.0.1:5000"


def menu():
    print("\n====== Inventory Management System ======")
    print("1. View Inventory")
    print("2. View One Item")
    print("3. Add Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Find Product by Barcode")
    print("7. Exit")


while True:
    menu()

    choice = input("Choose an option: ")

    if choice == "1":
        response = requests.get(f"{BASE_URL}/inventory")
        print(response.json())

    elif choice == "2":
        item_id = input("Enter Item ID: ")
        response = requests.get(f"{BASE_URL}/inventory/{item_id}")
        print(response.json())

    elif choice == "3":
        barcode = input("Barcode: ")
        name = input("Product Name: ")
        brand = input("Brand: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))

        item = {
            "barcode": barcode,
            "product_name": name,
            "brand": brand,
            "price": price,
            "stock": stock
        }

        response = requests.post(f"{BASE_URL}/inventory", json=item)
        print(response.json())

    elif choice == "4":
        item_id = input("Item ID: ")

        price = float(input("New Price: "))
        stock = int(input("New Stock: "))

        updates = {
            "price": price,
            "stock": stock
        }

        response = requests.patch(
            f"{BASE_URL}/inventory/{item_id}",
            json=updates
        )

        print(response.json())

    elif choice == "5":
        item_id = input("Item ID: ")

        response = requests.delete(
            f"{BASE_URL}/inventory/{item_id}"
        )

        print(response.json())

    elif choice == "6":
        barcode = input("Barcode: ")

        response = requests.get(
            f"{BASE_URL}/product/{barcode}"
        )

        print(response.json())

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")