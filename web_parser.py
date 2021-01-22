import requests
from bs4 import BeautifulSoup
import re


def parse_gastronom():
    URL = 'https://gastronom.com.ua/cat/search/%D0%BA%D1%80%D1%83%D0%BF%D0%B0%20%D0%B3%D1%80%D0%B5%D1%87%D0%BD%D0%B5%D0%B2%D0%B0%D1%8F/'
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='tovar')

    products = []

    for item in items:
        products.append({
            'title': item.find('a', class_ = 'tovar_name').get_text(strip=True),
            'price': re.sub('грн', '', item.find('b').get_text(strip=True)),
            'img': 'https://gastronom.com.ua/' + item.find('img', class_ = 'tovar_img')['data-src']
        })

    return products


def parse_atb():
    URL = 'https://zakaz.atbmarket.com/search/1048?text=%D0%B3%D1%80%D0%B5%D1%87%D0%B0%D0%BD%D0%B0'
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='product-wrap')

    products = []

    for item in items:
        products.append({
            'title': item.find('div', class_ = 'product-detail text-center').get_text(strip=True),
            'price': item.find('span', class_ = 'price').get_text(strip=True)[:2] + '.' + item.find('span', class_ = 'price').get_text(strip=True)[2:],
            'img': item.find('img')['src']
        })
    return products


def parse_vitok():
    URL = 'https://vitok.ua/search/?term=%D0%9A%D1%80%D1%83%D0%BF%D0%B0+%D0%B3%D1%80%D0%B5%D1%87%D0%BD%D0%B5%D0%B2%D0%B0%D1%8F'
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_ = 'product-card')

    products = []

    for item in items:
        products.append({
            'title': item.find('div', class_='product-title').get_text(strip=True),
            'price': item.find('span', class_='price-value').get_text(strip=True),
            'img': item.find('img')['src']
        })

    return products

# float(list[counter]['price'])


def sort(list):
    for counter in range(0, len(list)):
        for element in range(0, len(list)-counter-1):
            if float(list[element]['price']) > float(list[element + 1]['price']):
                list[element], list[element+1] = list[element+1], list[element]
    return list


def parse():
    list = parse_gastronom() + parse_atb() + parse_vitok()
    return sort(list)


