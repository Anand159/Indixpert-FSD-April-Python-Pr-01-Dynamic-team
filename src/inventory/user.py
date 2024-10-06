class UserManager:
    def __init__(self, inventory):
        self.inventory = inventory

    def get_password(self):
        while True:
            password = input(f"Enter password (must be exactly {self.inventory.PASSWORD_LENGTH} characters): ")
            if len(password) == self.inventory.PASSWORD_LENGTH:
                confirm_password = input("Confirm password: ")
                if password == confirm_password:
                    return password
                print("Passwords do not match.")
            else:
                print(f"Password must be exactly {self.inventory.PASSWORD_LENGTH} characters. Please try again.")

    def signup(self):
        if len(self.inventory.users) >= self.inventory.MAX_USERS:
            print("Maximum user limit reached. Cannot sign up more users.")
            return
        first_name = ""
        last_name = ""
        username = ""

        print("Choose signup type:")
        print("1. Admin Signup")
        print("2. User Signup")
        choice = input("Enter your choice (1/2): ")

        while not first_name.strip():
            first_name = input("Enter first name: ").strip()
            if not first_name:
                print("First name cannot be blank. Please try again.")

        while not last_name.strip():
            last_name = input("Enter last name: ").strip()
            if not last_name:
                print("Last name cannot be blank. Please try again.")

        while not username.strip():
            username = input("Enter username: ").strip()
            if not username:
                print("Username cannot be blank. Please try again.")

        if username in self.inventory.users:
            print("Username already exists.")
            return

        if choice == "1" and any(user['is_admin'] for user in self.inventory.users.values()):
            print("An admin already exists. Cannot create another admin.")
            return

        password = self.get_password()
        if not password:
            return

        is_admin = choice == "1"
        self.inventory.users[username] = {
            "first_name": first_name,
            "last_name": last_name,
            "password": password,
            "is_admin": is_admin
        }
        self.inventory.save_users()
        print("Signup successful.")

    def login(self):
        username = input("Enter username: ")
        if username not in self.inventory.users:
            print("Incorrect username.")
            return None

        password = input("Enter password: ")
        if self.inventory.users[username]["password"] == password:
            print("Login successful.")
            return username
        print("Incorrect password.")
        return None

    def delete_user(self):
        username = input("Enter the username to delete: ").strip()

        if not username:
            print("Username cannot be empty.")
            return

        if username in self.inventory.users:
            del self.inventory.users[username]
            self.inventory.save_users()
            print(f"User '{username}' deleted successfully.")
        else:
            print("User not found.")