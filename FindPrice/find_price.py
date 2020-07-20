import requests
from bs4 import BeautifulSoup
import logging

URL = 'https://www.americanas.com.br/busca/'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

def extract_infos(product_cards):
    products = []
    
    for div in product_cards:
        indexes = {}
        href = div.get('href')
        try:
            scope = div.find("div",{"class":"Info-bwhjk3-5 gWiKbT ViewUI-sc-1ijittn-6 iXIDWU"})
            title = scope.find("h2",{"class": re.compile("TitleUI-bwhjk3-15 khKJTM*")}).get_text()
            price = scope.find("span", {"class": re.compile("PriceUI-bwhjk3-11*")}).get_text()
            indexes['link'], indexes['title'], indexes['price'] = href, title, price
            products.append(indexes)
        except Exception as e:
            logging.error("Exception: %s" % e)
        
    return products

def find_product(search):
    search.lower().replace(' ', '-')
    try:
        page = requests.get(URL + search, headers=headers)
    except Exception as e:
        logging.error("Exception: %s" % e)
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.title)
        titles = soup.findAll("a", {"class": "Link-bwhjk3-2 iDkmyz TouchableA-p6nnfn-0 joVuoc"})
        if titles:
            products = extract_infos(titles)
            return products
        else:
             logging.error("Product query error")

