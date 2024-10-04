
import json
import os
from .product import Product

class Inventory:
    def __init__(self, filepath):
        self.filepath = filepath
        self.products = []
        self.load_products()

    def load_products(self):
        if os.path.isfile(self.filepath):
            with open(self.filepath, 'r') as file:
                self.products = [Product(**data) for data in json.load(file)]

    def save_products(self):
        with open(self.filepath, 'w') as file:
            json.dump([product.to_dict() for product in self.products], file, indent=2)

    def add_product(self):
        while True:
            try:
                product_id = int(input("Enter product ID: "))
                if product_id < 0:
                    print("ID cannot be negative. Please enter a valid ID.")
                    continue
                if any(product.product_id == product_id for product in self.products):
                    print("Product ID already exists. Please enter a unique ID.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid ID.")

        name = input("Enter product name: ")

        while True:
            try:
                price = float(input("Enter product price: "))
                if price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid price number.")

        while True:
            try:
                quantity = int(input("Enter product quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative. Please enter a valid quantity.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid quantity number.")

        new_product = Product(product_id, name, price, quantity)
        self.products.append(new_product)
        self.save_products()
        print(f"Product '{name}' with ID '{product_id}' added successfully.")
