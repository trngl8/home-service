import sys


class User:
    def __init__(self, name, pswd, mail):
        self.username = name
        self.password = pswd
        self.email = mail


class Storage:
    def __init__(self):
        self.users = []

    def add_user(self, u: User):
        self.users.append(u)


# main
if len(sys.argv) > 1 and sys.argv[1] == 'user':

    username = input("Add a new user: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    storage = Storage()
    user = User(username, password, email)
    storage.add_user(user)
    print(f"User {username} added")
