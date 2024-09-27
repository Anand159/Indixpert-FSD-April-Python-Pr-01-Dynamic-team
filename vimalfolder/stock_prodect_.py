class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def check_stock(self):
        if not self.products:
            print("No products available.")
            return

        for product in self.products:
            status = "Out of stock" if product.quantity == 0 else f"Available: {product.quantity}"
            print(f"ID: {product.product_id}, Product: {product.name}, Price: ₹{product.price / 100:.2f}, Status: {status}")

    def sell_product(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print(f"Sold {quantity} of {product.name}. Remaining: {product.quantity}")
                else:
                    print(f"Not enough stock for {product.name}. Available: {product.quantity}")
                return
        print("Product not found.")

    def check_low_stock(self):
        low_stock_products = [product for product in self.products if product.quantity < 10]
        if low_stock_products:
            print("Warning: The following products have low stock (less than 10):")
            for product in low_stock_products:
                print(f"ID: {product.product_id}, Product: {product.name}, Available: {product.quantity}")
        else:
            print("No products with low stock.")

store = Store()
store.add_product(Product(1, "apple", 50000, 8))  
store.add_product(Product(2, "laptop", 8000000, 50))
store.add_product(Product(3, "watch", 1000000, 2)) 

store.check_stock()
store.check_low_stock()
