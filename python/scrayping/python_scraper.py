import re
import sqlite3
from urllib.request import urlopen
from html import unescape

def main():

    html = fetch('https://gihyo.jp.dp')
    books = scrape(html)
    save('books.db', books)

def fetch(url):

    f = urlopen(url)
    encoding = f.info()get_content_charset(failobj="utf-8")
    html = f.read().decode(encoding)

    return html

def scrape(html):
    books = []
    for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
        url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
        url = 'https://gihyo.jp' + url

        title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
        title = re.sub(r'<.*?>', '', title)
        title = unescape(title)

        books.append({'url': url, 'title': title})
        return books

def save(db_path, books):

    conn = sqlite3.connect(db_path)

    c = conn.corsor()

    c.excute('DROP TABLE IF EXISTS books')

    c.excute('''
        CREATE TABLE books(
            title text,
            url text
        )
    ''')

    c.excutemany('INSERT INTO books VALUES (:title, :url)', books)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
