import time

text = "Python is powerful and easy to learn"
print("Type this sentence exactly:\n")
print(text)

input("Press Enter when ready...")

start = time.time()
typed = input("\nStart typing:\n")
end = time.time()

time_taken = end - start
words = len(typed.split())
wpm = words / (time_taken / 60)

correct_chars = sum(1 for i in range(min(len(text), len(typed))) if text[i] == typed[i])
accuracy = (correct_chars / len(text)) * 100

print(f"\n⏱ Time: {time_taken:.2f} seconds")
print(f"🚀 WPM: {wpm:.2f}")
print(f"🎯 Accuracy: {accuracy:.2f}%")
