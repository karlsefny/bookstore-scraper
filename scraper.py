import requests
from bs4 import BeautifulSoup
from main_scr import *

def scr(page:BeautifulSoup):
    li_list = page.find('ol',class_='row').find_all('li',class_=True)
    for li in li_list:
        link = li.a['href']
        main_page = BeautifulSoup(requests.get("http://books.toscrape.com/"+link).content,'html.parser')
        yield from main_scr(main_page)
# scr(BeautifulSoup(requests.get('http://books.toscrape.com/').content,'html.parser'))