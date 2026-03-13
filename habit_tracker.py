import json
from datetime import date

FILE = "habits.json"

def load():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

habits = load()

habit_name = input("Enter habit name: ")
today = str(date.today())

if habit_name not in habits:
    habits[habit_name] = []

if today not in habits[habit_name]:
    habits[habit_name].append(today)

# Calculate streak
streak = len(habits[habit_name])

save(habits)

print(f"🔥 Current streak of '{habit_name}': {streak} days")
