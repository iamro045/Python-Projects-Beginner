documents = {
    1: "python is powerful language",
    2: "python is used for backend development",
    3: "machine learning uses python"
}

def search(query):
    scores = {}

    for doc_id, text in documents.items():
        score = 0
        for word in query.split():
            score += text.lower().split().count(word.lower())
        if score > 0:
            scores[doc_id] = score

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked

while True:
    q = input("Search: ")
    print(search(q))
