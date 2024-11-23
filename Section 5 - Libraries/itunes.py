'''
Itunes
'''



import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# limit request is set to 50 instead of 1
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
# requesting only track names
for result in o["results"]:
    print(result["trackName"])



'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# more readable format
print(json.dumps(response.json(), indent=2))




import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
# converting to a standardized as a python dictionary    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
'''