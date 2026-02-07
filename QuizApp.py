import time

questions = [
    {"q": "Capital of India?", "a": "Delhi"},
    {"q": "5 + 7?", "a": "12"}
]

score = 0

for q in questions:
    start = time.time()
    ans = input(q["q"] + " ")
    end = time.time()

    if end - start > 10:
        print("⏰ Too slow!")
    elif ans.lower() == q["a"].lower():
        score += 1

print("Final Score:", score)
