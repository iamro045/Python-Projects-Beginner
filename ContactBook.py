import json

FILE = "contacts.json"

def load():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

contacts = load()

name = input("Enter name & Surname: ")
phone = input("Enter phone: ")
contacts[name] = phone
save(contacts)

print("Saved successfully!")
