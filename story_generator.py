import random

characters = ["wizard", "robot", "detective", "alien"]
places = ["forest", "city", "space station", "castle"]
actions = ["found a treasure", "saved the world", "lost their memory"]

def generate_story():
    char = random.choice(characters)
    place = random.choice(places)
    action = random.choice(actions)

    return f"One day a {char} in a {place} suddenly {action}."

for _ in range(3):
    print(generate_story())
