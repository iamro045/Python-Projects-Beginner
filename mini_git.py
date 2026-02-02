import hashlib
import os
import shutil

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()

def commit(file):
    h = file_hash(file)
    os.makedirs("versions", exist_ok=True)
    shutil.copy(file, f"versions/{h}")
    print("✅ Committed:", h)

commit("test.txt")
