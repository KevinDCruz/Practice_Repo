import requests  # connecting to a ewbpage
from bs4 import BeautifulSoup  # allows to sort through data


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.jabong.com/Us_Polo_Assn/?gender=Men'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")

        for link in soup.findAll('a', {'class': 'data-imagename'}):  # a is for links(anchors)
            src = link.get('src')
            print(src)
        page = page + 1


trade_spider(1)
