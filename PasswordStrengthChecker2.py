import re

password = input("Enter password: ")

if len(password) < 8:
    print("Weak password")
elif not re.search("[A-Z]", password):
    print("Add uppercase letter")
elif not re.search("[0-9]", password):
    print("Add number")
else:
    print("Strong password")
  
