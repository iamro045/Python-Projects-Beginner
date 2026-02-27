import hashlib
import time

SECRET = "my_secret_key"

def generate_token(username):
    expiry = str(int(time.time()) + 60)
    data = username + expiry + SECRET
    signature = hashlib.sha256(data.encode()).hexdigest()
    return f"{username}:{expiry}:{signature}"

def verify_token(token):
    username, expiry, signature = token.split(":")
    data = username + expiry + SECRET
    expected = hashlib.sha256(data.encode()).hexdigest()

    if expected == signature and int(expiry) > time.time():
        return True
    return False

token = generate_token("Rohit")
print("Token:", token)
print("Valid:", verify_token(token))
