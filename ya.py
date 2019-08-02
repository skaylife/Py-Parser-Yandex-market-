import requests
from bs4 import BeautifulSoup
import csv
import re

def get_html(url):
    r = requests.get(url)
    if r.ok: #200 403
        return r.text
    print(r.status_code)

def write_csv(data):
    with open('info.scv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow(([data['name'],
                          data['price_sort3'],
                          data['golos'],
                          data['url']]))

'''def write_csvd(data):
    with open('info.scv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow(([
                          data['price_sort3'],
                          data['golos'],
                                    ]))'''

def refine_price(s):
    return s.split(' ')[0]

def refine_price2(s):
    return s.split(' ')[-1]




def get_page_data(html):
    '''global myVar '''
    soup = BeautifulSoup(html, 'lxml')

    lis = soup.find_all('div', class_='n-snippet-cell2__title')
    pri = soup.find_all('div', class_='n-snippet-cell2__body')


     #<div class="price">35 490 ₽</div>
    #print(len(pri))


    for li in lis:

        try:
            name = li.find('a').text.replace("Смартфон", "").strip()
        except:
            name = ''
        try:
            url = 'https://market.yandex.ru' + li.find('a').get('href')

        except:
            url = ''

        data = {'name': name,
                'url': url}
        print(name)





    for pr in pri:

        try:
            golos = pr.find('div', class_='rating__value').text
        except:
            golos = ''
        try:
            price = pr.find('div', class_='price').text.strip()
            price_sort = refine_price(price)
            price_sort2 = refine_price2(price)
            price_sort3 =  refine_price(price).strip() + refine_price2(price).replace("₽", "").strip()
        except:
            price = ''

        data = {'price': price_sort3,
                'rating': golos}
        print(price_sort3)





'''        data = {'name': name,
                'price': price_sort3,
                'rating': golos,
                'url': url}

        write_csv(data)'''



def main():
    url = 'https://market.yandex.ru/catalog/54726/list?hid=91491&utm_source=adfox_desktop&utm_medium=banner_regular&utm_campaign=electronica_smartfony_305x238&glfilter=4940921%3A13475069&local-offers-first=0&onstock=1'
    get_page_data(get_html(url))




if __name__ == '__main__':
    main()
