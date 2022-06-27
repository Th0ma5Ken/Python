# Coding = utf-8
# By Th0ma5K3n

import re
import requests
from bs4 import BeautifulSoup


class Scrap:
    def __init__(self):
        '''
        阳光电影爬虫练习
        '''
        self.url_index_slice = 'https://www.ygdy8.com/html/gndy/dyzz/list_23_'#阳光电影的热门电影分类都是以list_23_数字.html结尾的静态网页,所以以这个为范本
        self.headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        self.list_name = []
        self.mag_dic = {}
        self.trash = ['经典影片','最新影片','国内电影','欧美电影','日韩电影','华语电视',\
                      '日韩电视','欧美电视','最新综艺','旧版综艺','动漫资源','游戏下载',\
                      '高分经典','收藏本站','APP下载','本站首页','电影','最新电影','综合电影']

    def get_slice(self,index):
        '''
        :param index:重新定向的页码
        :return: 重新定向的网页
        '''
        return self.url_index_slice + str(index) + ".html"

    def get_url(self,url):
        r = requests.get(url, headers=self.headers)
        r.encoding = 'gb2312'
        soup = BeautifulSoup(r.text, features="html.parser")
        return soup

    def pull_out(self,url):
        '''
        输出电影名称，网页链接，磁力链接到list_name表与mag_dic字典
        '''
        b = self.get_url(url).find_all("b")
        for a in b:
            a = a.find_all("a")
            for href in a:
                self.list_name.append(href.string)
                self.mag_dic[href.string] = 'https://www.ygdy8.com'+href.attrs['href']

    def get_mag(self,url):
        '''
        :return: 给定网页返回网页中的磁力链接
        '''
        soup = self.get_url(url)
        a = soup.find_all('a',{"href":re.compile('magnet')})
        for href in a:
            mag = href.attrs['href']
            return mag

    def print_move(self):

        for index in self.list_name:
            print(index)
            print(self.mag_dic.get(index)+"\n")
            if self.mag_dic.get(index) != None:
                print(self.get_mag(self.mag_dic.get(index))+'\n')
            else:
                pass

    def main(self,page=int):
        '''
        :param time: 页码
        :return:
        '''
        for i in range(1,page):
            self.pull_out(self.get_slice(i))
            self.print_move()

if __name__ == '__main__':
    demo = Scrap()
    demo.main(3)

