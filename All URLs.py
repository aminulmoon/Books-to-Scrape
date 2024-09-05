import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

i = 1
while i < 50:
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    i += 1

    s = requests.Session()
    res = s.get(url)
    soup = bs(res.text, 'html.parser')
    data_section = soup.find('ol', {'class':'row'})
    all_h3 = data_section.findAll('h3')

    all_links = []
    for url in all_h3:
        links = url.find('a').get('href')
        all_links.append('https://books.toscrape.com/catalogue/' + links + '\n')

    with open('All Books Url.txt', 'a+') as f:
        f.writelines(all_links)

