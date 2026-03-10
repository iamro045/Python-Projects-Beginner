def calculate(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        return "Cannot divide by zero" if b == 0 else a / b
    return "Invalid operator"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

print("Result is:", calculate(a, b, op))

