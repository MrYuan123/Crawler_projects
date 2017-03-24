#-*-coding:utf-8 -*-
import re
import os
import urllib2

import requests

from governmet_websites_spider import __init__
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class Download_Branch(object):
    def __init__(self):
        self.headers = {'User-Agent':'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    def PDF_Download(self,filename,now_url,keyS):
        pattern=re.compile(r'.*\.pdf',re.I)
        match=pattern.match(now_url)
        if match:
            print 'Have PDF file!'
            res = requests.get(now_url)
            res.raise_for_status()
            tit = u'%s(%s).pdf' % (filename.strip().encode('utf-8'),keyS)
            playFile = open(tit, 'wb')
            for chunk in res.iter_content(100000):
                playFile.write(chunk)
            playFile.close()

            return '1'
        else:
            return None
    def DOC_Download(self,filename,now_url,keyS):
        pattern = re.compile(r'.*\.doc', re.I)
        match = pattern.match(now_url)
        if match:
            print 'Have doc file!'
            res = requests.get(now_url)
            res.raise_for_status()
            tit = u'%s(%s).doc' % (filename.strip().encode('utf-8'),keyS)
            playFile = open(tit, 'wb')
            for chunk in res.iter_content(100000):
                playFile.write(chunk)
            playFile.close()

            return '1'
        else:
            pattern = re.compile(r'.*\.docx', re.I)
            match = pattern.match(now_url)
            if match:
                print 'have docx file!'
                res = requests.get(now_url)
                res.raise_for_status()
                tit = u'%s(%s).docx' % (filename.strip().encode('utf-8'),keyS)
                playFile = open(tit, 'wb')
                for chunk in res.iter_content(100000):
                    playFile.write(chunk)
                playFile.close()
                return '1'
            else:
                return None

    def Rar_Download(self, filename, now_url,keyS):
        pattern = re.compile(r'.*\.rar', re.I)
        match = pattern.match(now_url)
        if match:
            print 'have rar file!'
            res = requests.get(now_url)
            res.raise_for_status()
            tit = u'%s(%s).rar' % (filename.strip().encode('utf-8'),keyS)
            playFile = open(tit, 'wb')
            for chunk in res.iter_content(100000):
                playFile.write(chunk)
            playFile.close()

            return '1'
        else:
            return None


    def Xls_Download(self, filename, now_url,keyS):

        pattern = re.compile(r'.*\.xls', re.I)
        match = pattern.match(now_url)
        if match:
            print 'have xls file!'
            res = requests.get(now_url)
            res.raise_for_status()
            tit = u'%s(%s).xls' % (filename.strip().encode('utf-8'),keyS)
            playFile = open(tit, 'wb')
            for chunk in res.iter_content(100000):
                playFile.write(chunk)
            playFile.close()

            return '1'
        else:
            pattern = re.compile(r'.*\.xlsx', re.I)
            match = pattern.match(now_url)
            if match:
                print 'have xlsx file!'
                res = requests.get(now_url)
                res.raise_for_status()
                tit = u'%s(%s).xlsx' % (filename.strip().encode('utf-8'),keyS)
                playFile = open(tit, 'wb')
                for chunk in res.iter_content(100000):
                    playFile.write(chunk)
                playFile.close()
                return '1'
            else:
                return None


    def Zip_Download(self, filename, now_url,keyS):
        pattern = re.compile(r'.*\.zip', re.I)
        match = pattern.match(now_url)
        if match:
            print 'have zip file!'
            res = requests.get(now_url)
            res.raise_for_status()
            tit = u'%s(%s).zip' % (filename.strip().encode('utf-8'),keyS)
            playFile = open(tit, 'wb')
            for chunk in res.iter_content(100000):
                playFile.write(chunk)
            playFile.close()

            return '1'
        else:
            return None