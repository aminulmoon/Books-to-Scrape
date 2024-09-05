import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import csv

with open('All Books Url.txt', 'r') as f:
    url_list = f.readlines()

for url in url_list:
    url = url.strip('\n')
    s = requests.session()
    res = s.get(url)
    soup = bs(res.text, 'html.parser')

    book_name = soup.find('h1').text
    price_div = soup.find('div', {'class':'col-sm-6 product_main'})
    price = price_div.find('p',{'class':'price_color'}).text
    product_description_h2 = soup.find('div',{'class':'sub-header'}).find('h2').text
    product_description = soup.find('article',{'class':'product_page'}).findAll('p')[3].text
    image = soup.find('div',{'class':'item active'}).find('img').get('src').split('/')[2:]
    image_url = 'https://books.toscrape.com/'+'/'.join(image)

    table_heading = soup.findAll('h2')[1].text

    table_data = soup.find('table',{'class':'table table-striped'})

    book = {'Book Name': book_name, 'Price': price, 'Product Description Heading': product_description_h2, 'Product Description': product_description, 'Image': image_url}

    with open('BookData.csv', 'a', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=book.keys())
        writer.writeheader()
        i = 0
        while i < 20:
            writer.writerow(book)

