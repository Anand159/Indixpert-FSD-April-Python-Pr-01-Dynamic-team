from src.dashboard.option_menu import display_menu, main_menu

class Menu:
    def __init__(self, inventory, user_manager):
        self.inventory = inventory
        self.user_manager = user_manager
        self.current_user = None

    def start(self):
        while True:
            display_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                self.user_manager.signup()
            elif choice == "2":
                self.current_user = self.user_manager.login()
                if self.current_user:
                    self.handle_user_session()
            elif choice == "3":
                print("Exiting from the program ...")
                break
            else:
                print("Incorrect choice. Please try again.")

    def handle_user_session(self):
        while True:
            choice = input("if you display menu press y for yes n for no: ").lower()

            if choice != "y" and choice != "n":
                print("validated input: Please input string value")
                continue

            if choice == "y":
                main_menu()
                action = input("Choose an action: ")
            else:
                action = input("Choose an action: ")

            if action == "1":
                self.inventory.add_product(self.current_user)
            elif action == "2":
                self.inventory.sell_product(self.current_user)
            elif action == "3":
                self.inventory.update_quantity(self.current_user)
            elif action == "4":
                self.inventory.check_stock()
            elif action == "5":
                self.inventory.delete_product(self.current_user)
            elif action == "6" and self.inventory.users[self.current_user]["is_admin"]:
                self.inventory.view_user_products(self.current_user)
            elif action == "7":
                self.inventory.search_product()
            elif action == "8" and self.inventory.users[self.current_user]["is_admin"]:
                self.user_manager.delete_user()
            elif action == "9":
                print("Logged out successfully.")
                self.current_user = None
                break
            else:
                print("Incorrect choice. Please try again.")
