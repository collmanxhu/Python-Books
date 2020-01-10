import requests
import sys

r = requests.get('https://REDACTED.zportal.nl/api/v3/appointments?user=~me&start=1542006900&end=1542009900&access_token=REDACTED')

print(r.json())

location = r.json()["response"]["data"][0]["location"]
print(location)