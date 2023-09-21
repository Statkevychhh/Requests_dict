import requests

url = 'https://www.ukrlib.com.ua/books/printit.php?tid=752'

response = requests.get(url, stream=True)
#print(response.encoding)

with open('story2.txt', 'w') as file:
    for piece in response.iter_content(chunk_size=5000):
        print('Кусочок  записаний!')
        file.write(piece.decode('CP1251'))