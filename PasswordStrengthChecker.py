import re

password = input("Enter password: ")

length = len(password) >= 10
upper = bool(re.search(r"[A-Z]", password))
lower = bool(re.search(r"[a-z]", password))
digit = bool(re.search(r"\d", password))
symbol = bool(re.search(r"[@$!%*?&#]", password))

score = sum([length, upper, lower, digit, symbol])

if score == 7:
    print("Strong Password 💪")
elif score >= 5:
    print("Medium Password 😐")
else:
    print("Weak Password ❌")

