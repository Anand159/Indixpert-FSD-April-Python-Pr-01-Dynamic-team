from datetime import datetime

class Product:
    def __init__(self, product_id, name, price, quantity, owner, creation_date=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.owner = owner
        self.creation_date = creation_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "owner": self.owner,
            "creation_date": self.creation_date
        }