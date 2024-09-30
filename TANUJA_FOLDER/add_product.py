class Product:
    def _init_(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.name}")
        print(f"Product Price: ₹{self.price}")
        print(f"Product Quantity: {self.quantity}")

def add_product():
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    while True:
        try:
            price = float(input("Enter product price: ₹ "))
            break
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
    while True:
        try:
            quantity = int(input("Enter product quantity: "))
            break
        except ValueError:
            print("Invalid quantity. Please enter an integer value.")
            print("your product added successfully")
    product = Product(product_id, name, price, quantity)
    product.display_details()

add_product()