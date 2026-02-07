people = ["Rohit", "Amit", "Neha"]
expenses = {
    "Rohit": 1200,
    "Amit": 800,
    "Neha": 1000
}

total = sum(expenses.values())
equal_share = total / len(people)

for person in people:
    balance = expenses[person] - equal_share
    if balance > 0:
        print(f"{person} should receive ₹{balance:.2f}")
    else:
        print(f"{person} should pay ₹{abs(balance):.2f}")
      
