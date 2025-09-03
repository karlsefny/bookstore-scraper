import requests
from scraper import scr
from bs4 import BeautifulSoup


# url = f'http://books.toscrape.com/catalogue/page-{c}.html'
def pager():
    for c in range(50) :
        url = f'http://books.toscrape.com/catalogue/page-{c}.html'
        response = requests.get(url)
        page = BeautifulSoup(response.content,'html.parser')
    yield from scr(page)
        
    
