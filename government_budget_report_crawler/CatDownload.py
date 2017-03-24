#-*-coding:utf-8 -*-
import urllib2


class Cat_Download(object):
    def __init__(self):
        self.headers = {'User-Agent':'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    def Download_cat(self, now_url):
        request = urllib2.Request(now_url, headers=self.headers)
        response = urllib2.urlopen(request)
        return response.read()