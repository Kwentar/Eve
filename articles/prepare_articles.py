from bs4 import BeautifulSoup
import os


def get_clear_article_from_url(url):
    soup = BeautifulSoup(open(url).read(), "lxml")

    header_tag = soup.find(class_='b-topic__title')

    body_tag = soup.find(class_='b-text')
    if not header_tag or not body_tag:
        print('bad article {}'.format(url))
        return None
    title = header_tag.text
    article = ''
    for el in body_tag.find_all('p'):
        article += el.text + '\n'
    return title + '\n' + article


def generate_articles(articles_dir='norm_articles'):
    count_bad = count_good = 0
    for root, sub_folders, files in os.walk('/home/kwent/Projects/Eve/articles/lenta.ru/articles'):
        for file in files:
            article = get_clear_article_from_url(os.path.join(root, file))
            if article:
                count_good += 1
                with open(os.path.join(articles_dir, root.replace('/', '_') + '.html'), 'w') as f:
                    f.write(article)
            else:
                count_bad += 1
    print("good/bad {}/{}".format(count_good, count_bad))


def get_articles(articles_dir='norm_articles'):
    files = os.listdir(articles_dir)
    res = ''
    for file in files:
        res += open(os.path.join(articles_dir, file)).read() + '\n'
    return res


def get_text(articles_dir='norm_articles'):
    res = get_articles(articles_dir).lower()
    res = res.replace('ё', 'е').replace('!', '.').replace('?', '.')
    res = "".join(filter(lambda x: x in '0123456789абвгдежзийклмнопрстуфхцчшщъыьэюя.,-\n ', res))
    while '  ' in res:
        res = res.replace('  ', ' ')
    return res
