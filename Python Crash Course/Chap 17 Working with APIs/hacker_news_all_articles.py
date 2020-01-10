import requests
import json

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
response_id = r.json()
readable_file = 'data/readable_hn_all_id.json'
with open(readable_file, 'w') as f:
    json.dump(response_id, f, indent=4)
