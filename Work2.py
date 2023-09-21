import requests

url = 'https://www.ukrlib.com.ua/books/printit.php?tid=752'

response = requests.get(url)

with open('story.txt', 'w') as file:
    file.write(response.text)