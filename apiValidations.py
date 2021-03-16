import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'Shweta'},)
print(response.text)
print(type(response.text))
json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
for actualBook in json_response:
    if actualBook['isbn'] == 'bcd':
        print(actualBook)
        break
print(actualBook)
expectedBook = {'book_name': 'Moral Science', 'isbn': 'bcd', 'aisle': '589'}

assert actualBook == expectedBook





