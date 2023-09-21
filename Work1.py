import requests

url = 'https://httpbin.org/post'
query = {'search_query': 'audi'}

response = requests.get(url)
response2 = requests.post(url, data=query)

print(response.content)
print(response.text)
print(response.json())

response = requests.put(url, data=query)
response = requests.patch(url, data=query)
response = requests.delete(url)
response = requests.head(url)
response = requests.options(url)