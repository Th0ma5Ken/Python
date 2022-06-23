import re
import urllib.request
import requests
from bs4 import BeautifulSoup
all_List = []
lh = []
def get_url():
    url = "https://m.dytt8.net/html/gndy/dyzz/index.html"
    headers = headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    r = requests.get(url,headers= headers)
    r.encoding = 'gb2312'
    req = urllib.request.Request()
    req.add_header()
    soup = BeautifulSoup(r.text,features="html.parser")
    return soup
a = get_url().find_all("ul")
for data in a:
    la = data.find_all("a")
    for herf in la:
        lh.append(herf.string)
for i in range(45):
    lh.remove(lh[0])
for index in lh:
    print(index)

