from bs4 import BeautifulSoup


soup = BeautifulSoup(open('ria.ru/world/20161101/1480490266.html').read())

tag = soup.find(class_='b-article__body')
article = ''
for el in tag.find_all('p'):
    article += el.text + '\n'
    print(el)
print(article)