import os
import json
from .product import Product

class Inventory:
    MAX_USERS = 4
    PASSWORD_LENGTH = 7

    def __init__(self, users_filepath, products_filepath):
        self.users_filepath = users_filepath
        self.products_filepath = products_filepath
        self.ensure_data_files_exist()
        self.users = {}
        self.products = []
        self.load_users()
        self.load_products()

    def ensure_data_files_exist(self):

        data_dir = os.path.dirname(self.users_filepath)
        os.makedirs(data_dir, exist_ok=True)
        
        if not os.path.isfile(self.users_filepath):
            with open(self.users_filepath, 'w') as file:
                json.dump({}, file, indent=2)

        if not os.path.isfile(self.products_filepath):
            with open(self.products_filepath, 'w') as file:
                json.dump([], file, indent=2)

    def load_users(self):
        with open(self.users_filepath, 'r') as file:
            self.users = json.load(file)

    def save_users(self):
        with open(self.users_filepath, 'w') as file:
            json.dump(self.users, file, indent=2)

    def load_products(self):
        with open(self.products_filepath, 'r') as file:
            self.products = [Product(**data) for data in json.load(file)]

    def save_products(self):
        with open(self.products_filepath, 'w') as file:
            json.dump([product.to_dict() for product in self.products], file, indent=2)

    def add_product(self, username):
        while True:
            product_id = input("Enter product ID: ")
            if any(product.product_id == product_id for product in self.products):
                print("Product with this ID already exists. Please use a different ID.")
            else:
                break

        name = input("Enter product name: ")
        try:
            price = float(input("Enter product price: "))
            if price < 0:
                print("Price cannot be negative.")
                return
            quantity = int(input("Enter product quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                return
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        new_product = Product(product_id, name, price, quantity, username)
        self.products.append(new_product)
        self.save_products()
        print("Product added successfully.")

    def sell_product(self, username):
        product_id = input("Enter product ID to sell: ")

        while True:
            try:
                quantity_to_sell = int(input("Enter quantity to sell: "))
                if quantity_to_sell < 1:
                    print("Quantity must be at least 1. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        product = next((p for p in self.products if p.product_id == product_id), None)

        if product is None:
            print("Product not found.")
            return username

        if quantity_to_sell <= product.quantity:
            product.quantity -= quantity_to_sell
            self.save_products()
            print(f"Sold {quantity_to_sell} of product ID {product_id}.")
        else:
            print("Insufficient stock.")

        return username

    def update_quantity(self, username):
        product_id = input("Enter product ID to update: ")
        new_quantity = input("Enter new quantity: ")
        try:
            new_quantity = int(new_quantity)
            for product in self.products:
                if product.product_id == product_id:
                    product.quantity = new_quantity
                    self.save_products()
                    print("Product quantity updated successfully.")
                    return
            print("Product not found.")
        except ValueError:
            print("Invalid quantity. Please enter a numeric value.")
        return username

    def delete_product(self, username):
        product_id = input("Enter product ID to delete: ")
        self.products = [p for p in self.products if p.product_id != product_id]
        self.save_products()
        print("Product deleted successfully.")
        return username

    def check_stock(self):
        print("\nCurrent Stock Levels:")
        for product in self.products:
            print(f"  - ID: {product.product_id}, Name: {product.name}, Quantity: {product.quantity}, Owner: {product.owner}")

    def search_product(self):
        search_term = input("Enter product ID or name to search: ").strip()
        results = [product for product in self.products if search_term in product.product_id or search_term.lower() in product.name.lower()]

        if results:
            print("\nSearch Results:")
            for product in results:
                print(f"  - ID: {product.product_id}, Name: {product.name}, Price: {product.price:.2f}, Quantity: {product.quantity}, Owner: {product.owner}")
        else:
            print("No products found.")

    def view_user_products(self, admin_username):
        if not self.users[admin_username]["is_admin"]:
            print("Access denied. Only admins can view other users' products.")
            return

        username = input("Enter the username of the user whose products you want to view: ")

        if username not in self.users:
            print("User not found.")
            return

        print(f"\nProducts for {username}:")
        user_products = [product for product in self.products if product.owner == username]
        if user_products:
            for product in user_products:
                print(f"  - ID: {product.product_id}, Name: {product.name}, Price: {product.price:.2f}, Quantity: {product.quantity}")
        else:
            print("  No products found for this user.")