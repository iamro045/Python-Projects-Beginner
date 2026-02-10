import os
import hashlib

def file_hash(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def remove_duplicates(folder):
    hashes = {}
    
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            filehash = file_hash(path)

            if filehash in hashes:
                print("🗑 Removing duplicate:", path)
                os.remove(path)
            else:
                hashes[filehash] = path

remove_duplicates("test_folder")
