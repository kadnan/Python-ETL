import bonobo
import requests
from bs4 import BeautifulSoup


def scrape_zillow():
    price = ''
    status = ''
    url = 'https://www.zillow.com/homedetails/41-Norton-Ave-Dallas-PA-18612/2119501298_zpid/'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = r.text.strip()
        soup = BeautifulSoup(html, 'lxml')
        price_status_section = soup.select('.home-summary-row')
        if len(price_status_section) > 1:
            price = price_status_section[1].text.strip()
    return price


def scrape_redfin():
    price = ''
    status = ''
    url = 'https://www.redfin.com/TX/Dallas/2619-Colby-St-75204/unit-B/home/32251730'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = r.text.strip()
        soup = BeautifulSoup(html, 'lxml')
        price_section = soup.find('span', {'itemprop': 'price'})
        if price_section:
            price = price_section.text.strip()
    return price


def extract():
    yield scrape_zillow()
    yield scrape_redfin()


def transform(price: str):
    t_price = price.replace(',', '').lstrip('$')
    return float(t_price)


def load(price: float):
    with open('pricing.txt', 'a+', encoding='utf8') as f:
        f.write((str(price) + '\n'))


if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'referrer': 'https://google.com'
    }
    # scrape_redfin()
    graph = bonobo.Graph(
        extract,
        transform,
        load,
    )
    bonobo.run(graph)
