import sys

if len(sys.argv) > 1 and sys.argv[1] == 'user':

    username = input("Add a new user: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    user = User(username, password, email)
    storage.add_user(user)
    print(f"User {username} added")

