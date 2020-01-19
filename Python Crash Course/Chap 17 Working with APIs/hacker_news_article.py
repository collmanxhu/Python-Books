"""
To explore how to use API calls on other sites, quick look at Hacker News
( http://news.ycombinator.com/ ). On Hacker News, people share articles about
 programming and technology, and engage in lively discussions about those articles.
 The Hacker News API provides access to data about all submissions and comments on
 the site, and you can use the API without having to register for a key.
"""
import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

