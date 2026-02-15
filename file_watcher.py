import os
import time

def snapshot(folder):
    files = {}
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            files[file] = os.path.getmtime(path)
    return files

def monitor(folder):
    before = snapshot(folder)

    while True:
        time.sleep(2)
        after = snapshot(folder)

        added = after.keys() - before.keys()
        removed = before.keys() - after.keys()
        modified = {f for f in before if f in after and before[f] != after[f]}

        for f in added:
            print("📂 Added:", f)

        for f in removed:
            print("🗑 Removed:", f)

        for f in modified:
            print("✏ Modified:", f)

        before = after

monitor("test_folder")
