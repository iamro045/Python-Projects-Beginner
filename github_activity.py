import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}/events"

response = requests.get(url)
events = response.json()

repo_counts = {}

for event in events:
    repo = event["repo"]["name"]
    repo_counts[repo] = repo_counts.get(repo, 0) + 1

print("\nActivity Summary:")
for repo, count in repo_counts.items():
    print(repo, "->", count, "events")
