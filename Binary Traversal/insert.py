class User:
    def __init__(self, username: str):
        self.username = username

class UserDataBase:
    def __init__(self) -> None:
        self.users = []
        
    def insert(self, user: User):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
                
    def list_all(self):
        return self.users

# Create instances of User
rukhsana = User("Rukhsana")
moina = User("Moina")

# Create an instance of UserDataBase and insert users
database = UserDataBase()
database.insert(rukhsana)
database.insert(moina)

# List all users
for user in database.list_all():
    print(user.username)
