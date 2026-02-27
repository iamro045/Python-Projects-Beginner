import requests

API_KEY = "api_key"
base = input("Base currency (e.g., USD): ").upper()
target = input("Target currency (e.g., INR): ").upper()
amount = float(input("Amount: "))

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
data = requests.get(url).json()

if data["result"] == "success":
    rate = data["conversion_rates"][target]
    print(f"{amount} {base} = {amount * rate} {target}")
else:
    print("Invalid currency or API problem")

