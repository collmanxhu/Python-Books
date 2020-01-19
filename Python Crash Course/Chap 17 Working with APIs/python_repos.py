import requests

# Make an API call and store the response
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")   # Status code tell the request is success or not
                                         # 200 is successful
# Store API response in a variable       # incomplete_results = false, means successful
response_dict = r.json()                 # incomplete_results = false, means unable to fully process
# Process results
# print(response_dict.keys())
# print(f"incomplete_results: {response_dict['incomplete_results']}")
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")

# Examine the first repository
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)
#
# print("\nSelected information about first repository:")
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")