import json
import hashlib

FILE = "users.json"

def load_users():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup():
    users = load_users()
    username = input("Username: ")
    if username in users:
        print("❌ User exists")
        return

    password = input("Password: ")
    users[username] = hash_password(password)
    save_users(users)
    print("✅ Signup successful")

def login():
    users = load_users()
    username = input("Username: ")
    password = input("Password: ")

    if users.get(username) == hash_password(password):
        print("🎉 Login successful")
    else:
        print("❌ Invalid credentials")

while True:
    print("\n1. Signup\n2. Login\n3. Exit")
    c = input("Choose: ")

    if c == "1":
        signup()
    elif c == "2":
        login()
    elif c == "3":
        break
