import aiohttp
import lxml
import pyquery
import pymysql
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello World</p>', 'lxml')
print(soup.p.string)
print(pymysql.VERSION)
