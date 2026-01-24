documents = {
    1: "python is a great programming language",
    2: "python is used for data science",
    3: "machine learning uses python"
}

index = {}

for doc_id, text in documents.items():
    for word in text.lower().split():
        index.setdefault(word, set()).add(doc_id)

def search(query):
    words = query.lower().split()
    result = None

    for word in words:
        if word in index:
            result = index[word] if result is None else result & index[word]
        else:
            return []

    return result

while True:
    q = input("\nSearch (or exit): ")
    if q == "exit":
        break

    results = search(q)
    for r in results:
        print(f"Doc {r}: {documents[r]}")
