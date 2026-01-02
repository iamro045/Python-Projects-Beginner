import re

password = input("Enter password: ")

length = len(password) >= 8
upper = bool(re.search(r"[A-Z]", password))
lower = bool(re.search(r"[a-z]", password))
digit = bool(re.search(r"\d", password))
symbol = bool(re.search(r"[@$!%*?&#]", password))

score = sum([length, upper, lower, digit, symbol])

if score == 5:
    print("Strong Password 💪")
elif score >= 3:
    print("Medium Password 😐")
else:
    print("Weak Password ❌")
