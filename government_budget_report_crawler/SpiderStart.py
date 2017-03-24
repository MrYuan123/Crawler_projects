#-*-coding:utf-8 -*-
import os
import time,random

from Baidu_Search_Spider import BuildKey,CatDownload,UrlParser,UrlDownload

class Spider_Start(object):
    def __init__(self):
        self.Build=BuildKey.Build_key()
        self.Cat=CatDownload.Cat_Download()
        self.Parser=UrlParser.Url_Parser()
        self.download=UrlDownload.Url_Download()

    def Spider(self,address,year):
        now_url,cat_name=self.Build.Build_Url(address,year)
        print 'Get the now_url'
        htmlPage=self.Cat.Download_cat(now_url)

        print 'Get point cat page'
        if len(htmlPage)==0:
            print 'Can`t download '+address+' catogery'
            return
        point_urls=self.Parser.Parser_Point_Urls(htmlPage)
        print 'Get point urls'
        print '============================================================================'
        for key in point_urls:
            print key
        print '============================================================================'
        if len(point_urls)==0:
            print address+' doesn`t have point pages!'
            return
        self.download.Point_Pages_Download(point_urls,cat_name,address)
        print address+' sucess!'
        return


if __name__=='__main__':
   prov=u'衡水市'
   ADD = open("name.txt", "r")
   if os.path.exists(prov):
       os.chdir(prov)
   else:
       os.mkdir(prov)
       os.chdir(prov)

   for address in ADD:
       addr = address.decode("gbk").strip()
       addr=prov+addr
       if os.path.exists(addr):
           os.chdir(addr)
       else:
           os.mkdir(addr)
           os.chdir(addr)

       for year in range(2010,2016):
           obj_spider=Spider_Start()
           obj_spider.Spider(addr,year)
           os.chdir(u'F:\编程\Spider_Project\Baidu_Search_Spider\%s\%s'%(prov,addr))
           #print addr+'has finished!'
       os.chdir(u'F:\编程\Spider_Project\Baidu_Search_Spider\%s'%prov)
   print 'Have stoped the system!'
