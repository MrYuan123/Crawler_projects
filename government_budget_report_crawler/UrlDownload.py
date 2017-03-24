#-*-coding:utf-8 -*-
import os
import sys
import urllib2
import urllib
import urlparse
from Baidu_Search_Spider import DownloadBranch
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding( "utf-8" )

class Url_Download(object):
    def __init__(self):
        self.headers = {'User-Agent':'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        self.Branch=DownloadBranch.Download_Branch()
    def point_page(self,down_url):
        request = urllib2.Request(down_url, headers=self.headers)
        response = urllib2.urlopen(request)
        return response.read()

    def Point_Pages_Download(self, point_urls,cat_name,address):
        if os.path.exists(cat_name):
            os.chdir(cat_name)
        else:
            os.mkdir(cat_name)
            os.chdir(cat_name)

        for key in point_urls:
            keyS = str(key)
            print keyS
            print point_urls[key]
            request = urllib2.Request(point_urls[key], headers=self.headers)
            try:
                try:
                    response = urllib2.urlopen(request,timeout=60)
                    content_download = response.read()
                    now_url=response.geturl()
                    # if keyS.find(address)!=-1 and keyS.find('预算')!=-1:
                except:
                    continue

                tit = u'%s.htm' % keyS.strip().encode('utf-8')
                with open(tit, 'w') as f:
                    f.write(content_download)


                soup = BeautifulSoup(content_download, 'html.parser', from_encoding='utf-8')
                links = soup.find_all('a')

                #print 'To find the accessory:====================================================='
                #for link in links:
                #    print link.text
                #print '==========================================================================='

                for link in links:
                    try:
                        part_url = link['href']
                        new_full_url = urlparse.urljoin(now_url, part_url)
                        print link.text,new_full_url
                        page_tit = str(link.text)
                        page_title = page_tit.strip()

                        pFlag = self.Branch.PDF_Download(page_title, new_full_url,keyS)
                        dFlag = self.Branch.DOC_Download(page_title, new_full_url,keyS)
                        xFlag = self.Branch.Xls_Download(page_title, new_full_url,keyS)
                        zFlag = self.Branch.Zip_Download(page_title, new_full_url,keyS)
                        rFlag = self.Branch.Rar_Download(page_title, new_full_url,keyS)

                        if pFlag=='1' or dFlag=='1' or xFlag=='1' or zFlag=='1' or rFlag=='1':
                            print 'Find accessory!'
                    except:
                        continue

            except:
                continue
        return