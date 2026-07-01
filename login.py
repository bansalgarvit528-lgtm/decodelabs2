import json
import os
import hashlib

FILE_NAME = "users.json"

def encrypt(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump({}, f)

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_users(users):
    with open(FILE_NAME, "w") as f:
        json.dump(users, f, indent=4)


def register():
    users = load_users()

    print("\n===== Register =====")

    username = input("Enter Username : ")

    if username in users:
        print("Username already exists!")
        return

    password = input("Enter Password : ")

    users[username] = encrypt(password)

    save_users(users)

    print("Registration Successful!\n")


def login():
    users = load_users()

    print("\n===== Login =====")

    username = input("Username : ")
    password = input("Password : ")

    if username in users and users[username] == encrypt(password):
        print("\nLogin Successful!\n")
        return True

    print("\nInvalid Username or Password\n")
    return False