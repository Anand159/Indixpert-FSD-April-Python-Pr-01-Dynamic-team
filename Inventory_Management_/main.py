from src.inventory import Inventory 
def main():
    inventory = Inventory('inventory.json')
    inventory.add_product()

if __name__ == "__main__":
    main()


