def check_stock(products):
    if not products:
        print("No products available.")
        return  

    low_stock_products = [] 

    for product in products:
        try:
            print(f"ID: {product.product_id}, Product: {product.name}, Price: ₹{product.price:.2f}, Quantity: {product.quantity}")

            if product.quantity < 10:
                low_stock_products.append(product)
        except AttributeError as a:
            print(f"Error accessing product attributes: {a}")

  
    if low_stock_products:
        print("\nWarning: The following products have low stock (less than 10):")
        for product in low_stock_products:
            print(f"ID: {product.product_id}, Product: {product.name}, Quantity: {product.quantity}")
