import re
import warnings

import requests
from requests.packages import urllib3
from bs4 import BeautifulSoup

allUniv = []


def get_HTMLText(url):
    try:
        r = requests.get(url, timeout=50)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return "false"


'''
tr/td
'''


def fillUniv_List(soup):
    data = soup.find_all("tr")
    for tr in data:
        singleUniv = []
        ltd = tr.find_all('td')
        for p in ltd:
            singleUniv.append(p.string.replace("\xa0", ' '))
        allUniv.append(singleUniv)
    # print(allUniv)


def print_Univ(num):
    t = allUniv[0]
    print("{1:{0}^4}{2:{0}^15}{3:^56}{4:{0}^14}".format(chr(12288), t[0], t[1], t[2], t[3]))
    allUniv.pop(0)
    for i in range(num):
        u = allUniv[i]
        print("{1:^6}{2:{0}^15}{3:^60}{4:{0}^14}".format(chr(12288), u[0], u[1], u[2], u[3]))


def main(num):
    url = "http://heucice.hrbeu.edu.cn/4017/list.htm"
    html = get_HTMLText(url)
    soup = BeautifulSoup(html, features="html.parser")
    fillUniv_List(soup)
    print_Univ(num)


def get_country(country=""):
    if country == str:
        warnings.warn(
            "country must be string"
        )
    for data in allUniv:
        if data[3] == country:
            print("{1:^6}{2:{0}^15}{3:^60}{4:{0}^14}".format(chr(12288), data[0], data[1], data[2], data[3]))


main(10)
# get_country("中国")