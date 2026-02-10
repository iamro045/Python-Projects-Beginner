import time

LOG_FILE = "app.log"
THRESHOLD = 3

def monitor():
    error_count = 0

    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)  # Move to end of file

        while True:
            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            if "ERROR" in line:
                error_count += 1
                print("⚠ Error detected")

            if error_count >= THRESHOLD:
                print("🚨 ALERT: Too many errors!")
                error_count = 0

monitor()
