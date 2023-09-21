import requests

page = requests.get('http://google.com')
page2 = requests.get('http://google.com?q=cats')
page3 = requests.get('http://google.com', params={
    
    'q': 'cats dogs pigs'
    
})

print(page)
print(page.status_code)
# 200 - ok
# 404 - not found
# 500 internal server error

print(page.content) # binary data
print(page.content.decode(page.encoding))  # utf-8

print(page.text)

print(page3.url)

print(page3.headers['Content-Type'])
