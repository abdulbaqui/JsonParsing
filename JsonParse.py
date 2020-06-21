import json
import requests
print('Json Parse')

response = requests.get("https://jsonplaceholder.typicode.com/posts")
#print(response.status_code)

x = response.content.decode("utf-8")
y = json.loads(x)
print(y)
array = []
for key in y:
    array.append(key["title"])
print(array[5])