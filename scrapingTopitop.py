import urllib.request, urllib.parse, urllib.error
import ssl
import sqlite3
from bs4 import BeautifulSoup
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open('url.data')
for line in fh:
    url = line.strip()
    #url = "https://www.topitop.pe/xiomi-vestido-mujer-somalia-acero-denim-1929422/p"
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html,'html.parser')

    listDiv = list()
    name = url.split("/")[3]
    price = float(soup.find("strong", {"class": "skuBestPrice"}).contents[0].split(" ")[1])
    image = soup.find("a", {"id": "botaoZoom"}).contents[1].get('src',None)

    print(image,name,price)
