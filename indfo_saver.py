import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from pager import pager


info=list()
def info_saver():
    rows=pager()
    for row in rows:
        info.append(row)
info_saver()
df = pd.DataFrame(info,columns=['name','price','availabality','rating','description'])
df.to_csv('data.csv')