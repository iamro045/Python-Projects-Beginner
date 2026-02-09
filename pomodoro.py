import time

WORK_TIME = 5   # change to 1500 for real 25 mins
BREAK_TIME = 3  # change to 300 for real 5 mins

def countdown(seconds, label):
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{label} {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print(f"\n✅ {label} session completed!")

sessions = 0

while True:
    input("\nPress Enter to start Work session...")
    countdown(WORK_TIME, "Work")
    sessions += 1

    print("Time for a break ☕")
    countdown(BREAK_TIME, "Break")

    print(f"🔥 Sessions completed: {sessions}")
  
