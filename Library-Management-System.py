import json

FILE = "data.json"

class Library:
    def __init__(self):
        self.data = self.load()

    def load(self):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except:
            return {"books": {}, "users": {}}

    def save(self):
        with open(FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_book(self, book_id, title):
        self.data["books"][book_id] = {"title": title, "issued_to": None}
        self.save()
        print("📘 Book added")

    def add_user(self, user_id, name):
        self.data["users"][user_id] = name
        self.save()
        print("👤 User added")

    def issue_book(self, book_id, user_id):
        if self.data["books"][book_id]["issued_to"] is None:
            self.data["books"][book_id]["issued_to"] = user_id
            self.save()
            print("✅ Book issued")
        else:
            print("❌ Already issued")

lib = Library()
lib.add_book("B1", "Python Basics")
lib.add_user("U1", "Rohit")
lib.issue_book("B1", "U1")
