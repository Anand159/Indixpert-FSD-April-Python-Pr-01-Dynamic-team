from src.inventory.inventory import Inventory
from src.inventory.user import UserManager
from src.menu.menu import Menu

if __name__ == "__main__":
    inventory = Inventory("src/database/users.json", "src/database/products.json")
    user_manager = UserManager(inventory)
    menu = Menu(inventory, user_manager)
    menu.start()