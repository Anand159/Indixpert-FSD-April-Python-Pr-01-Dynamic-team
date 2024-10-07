from src.domain.inventory import Inventory
from src.domain.user import UserManager
from src.menu_mangement.menu import Menu

if __name__ == "__main__":
    inventory = Inventory()
    user_manager = UserManager(inventory)
    menu = Menu(inventory, user_manager)
    menu.start()

