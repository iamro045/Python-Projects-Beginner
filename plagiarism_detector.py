from difflib import SequenceMatcher

def read_file(file):
    with open(file, "r") as f:
        return f.read()

def similarity(file1, file2):
    text1 = read_file(file1)
    text2 = read_file(file2)

    ratio = SequenceMatcher(None, text1, text2).ratio()
    return ratio * 100

file1 = input("First file: ")
file2 = input("Second file: ")

score = similarity(file1, file2)
print(f"Similarity: {score:.2f}%")
