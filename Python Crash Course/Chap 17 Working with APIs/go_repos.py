"""
17-1 modify python_repos.py to generates a chart showing other languages, such as
javascript, ruby, C, java, perl, haskell and Go
https://2.python-requests.org//en/latest/user/quickstart/
"""
import json
import requests
from plotly import offline

# Make an API call and store the response
url = 'http://api.github.com/search/repositories?q=language:go&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# print(r)
# print(dir(r))
# print(help(r))
print(r.text)

response_dicts = r.json()
"""In case the JSON decoding fails, r.json() raises an exception. For example,
if the response gets a 204 (No Content), or if the response contains invalid JSON,
attempting r.json() raises ValueError: No JSON object could be decoded."""
readable_file = 'data/readable_go_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dicts, f, indent=4)

repo_dicts = response_dicts['items']
# readable_file = 'data/readable_go_items_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(repo_dicts, f, indent=4)
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    labels.append(f"{owner}<br />{description}")

# Make visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'},
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most-Starred Go Projects on GitHub',
    'titlefont': {'size': 24},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='go_repos.html')
