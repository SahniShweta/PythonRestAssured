import requests
from bs4 import BeautifulSoup

li = []
data = requests.get("https://www.imdb.com/find?q=thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content, 'html.parser')

moviesTable = soup.find('table', {'class': 'findList'})
rows = moviesTable.findAll('tr')

for row in rows:
    rowData = row.findAll('td')
    title = rowData[1].a.text
    subUrl = rowData[1].a['href']
    subData = requests.get("https://www.imdb.com"+subUrl)
    childSoup = BeautifulSoup(subData.content, 'html.parser')
    if childSoup.find('div', {'class': 'see-more inline canwrap'}):
        genre = childSoup.find('div', {'class': 'see-more inline canwrap'})
        print(rowData[1].a.text)
        print(genre.a.text)
        if genre.a.text == " anthology":
            # print(rowData[1].a.text)
            # print(genre.a.text)
            li.append(rowData[1].a.text)

print(li)






