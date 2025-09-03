from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def main_scr(page:BeautifulSoup):
    data = list()
    row = list()
    main =page.find('div',class_="product_main")
    row.append(main.find('h1').string)
    row.append(main.find('p',class_='price_color').string)
    row.append(list(main.find('p',class_='instock availability').strings)[1].strip())
    row.append(main.find('p',class_='star-rating')['class'][1])
    row.append(page.find('div',id='product_description').next_sibling.next_sibling.string)
    yield row

