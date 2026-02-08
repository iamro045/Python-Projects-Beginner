movies = {
    "Action": ["Avengers", "Batman"],
    "Comedy": ["Hangover", "Superbad"]
}

genre = input("Choose genre: ")
print("Recommended:", movies.get(genre, []))
