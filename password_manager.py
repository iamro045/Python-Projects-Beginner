import json
import hashlib

FILE = "vault.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

vault = load()

site = input("Enter website: ")
password = input("Enter password: ")

vault[site] = hash_password(password)
save(vault)

print("🔐 Password stored securely!")
