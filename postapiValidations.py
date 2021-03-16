import requests
import configparser
from utilities.resources import APIResources
from utilities.configurations import *
from payload import *
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

#post and delete
url = getConfig()['API']['endpoint'] + APIResources.addBook
headers = {'Content-Type': 'application/json'}
query = 'select * from Books'
addbook_response = requests.post(url, json=buildPayLoadFromDB(query), headers=headers, )
#
print(addbook_response.json())
bookID = addbook_response.json()['ID']
#delete
url1 = getConfig()['API']['endpoint'] + APIResources.deleteBook
deleteBook_response = requests.post(url1, json=deleteBookPayload(bookID), headers=headers, )
#
assert deleteBook_response.status_code == 200
#
res_json = deleteBook_response.json()
print(res_json['msg'])
assert res_json['msg'] == 'book is successfully deleted'

# session
se = requests.session()
se.auth = auth=HTTPBasicAuth('SahniShweta', 'token')

url = 'https://api.github.com/user'
response = requests.get(url, verify=False, auth=HTTPBasicAuth('SahniShweta', 'token'))
print(response.status_code)

url2 = 'https://api.github.com/user/repos'
response = se.get(url2)
print(response.status_code)
