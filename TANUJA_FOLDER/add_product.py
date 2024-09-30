import json
import os

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
    

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
        try:
            while True:
                try:
                    product_id = int(input("Enter product ID: "))
                    if product_id < 0:  
                        print("ID cannot be negative. Please enter a valid ID:")
                        continue 
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid ID:")

            while True:
                name = input("Enter product name: ")
                if not name:  
                    print("Name cannot be empty. Please enter a valid name:")
                    continue
                break
        
            while True:
                try:
                    price = float(input("Enter product price: "))  
                    if price < 0:  
                        print("Price cannot be negative. Please enter a valid price:")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid price number:")

            while True:
                try:
                    quantity = int(input("Enter product quantity: "))
                    if quantity < 0:  
                        print("Quantity cannot be negative. Please enter a valid quantity:")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid quantity number:")

            new_product = Product(product_id, name, price, quantity)
            self.products.append(new_product)
            self.save_products()
            print(f"Product '{name}' with ID '{product_id}' added successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    inventory = Inventory("products.json")
    inventory.add_product()
