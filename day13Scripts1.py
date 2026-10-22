# Author : Archana Zhope
# Date : 22 October 2026
# Script : API call

import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)

print(response.json())
if response.status_code == 200:
        data= response.json()
        print(data["title"])
        print(data["completed"])
else:
       print(f"Request failed with status {response.status_code}")
        