import requests

page  = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = page.json()

print(data['title'])
print(page.headers['Content-Type'])