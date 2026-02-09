import json

FILE = "expenses.json"

KEYWORDS = {
    "Food": ["zomato", "swiggy", "restaurant", "dinner", "lunch"],
    "Travel": ["uber", "ola", "flight", "bus", "train"],
    "Shopping": ["amazon", "flipkart", "mall"],
    "Bills": ["electricity", "rent", "water", "wifi"]
}

def detect_category(description):
    desc = description.lower()
    for category, words in KEYWORDS.items():
        for word in words:
            if word in desc:
                return category
    return "Other"

def load():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

expenses = load()

desc = input("Enter expense description: ")
amount = float(input("Enter amount: "))

category = detect_category(desc)

expenses.append({
    "description": desc,
    "amount": amount,
    "category": category
})

save(expenses)

print(f"✅ Saved under category: {category}")
