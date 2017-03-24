#-*-coding:utf-8 -*-
import sys

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding( "utf-8" )

class Url_Parser(object):
    def __init__(self):
        pass
    def Parser_Point_Urls(self, htmlPage):
        point_urls = dict()
        soup = BeautifulSoup(htmlPage, 'html.parser', from_encoding='utf-8')
        fra=soup.find_all('div',id='content_left')
        if len(fra)==0:
            print 'fra empty!'
        soupF=BeautifulSoup(str(fra), 'html.parser', from_encoding='utf-8')
        #links=soupF.find_all("div",srcid="1599")
        links=soupF.find_all("div",{'class':'result c-container '})

        for link in links:
            real_url=str(link.find(style="text-decoration:none;").text)
            if real_url.find("gov")!=-1:
                soupL = BeautifulSoup(str(link), 'html.parser', from_encoding='utf-8')
                diction=soupL.find('a',target="_blank")
                #print diction["href"]
                #print diction.text
                key=str(diction.text).strip()
                point_urls[key]=diction['href']
        return point_urls