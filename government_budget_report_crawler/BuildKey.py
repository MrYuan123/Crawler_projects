#-*-coding:utf-8 -*-
import urllib,sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class Build_key(object):
    def __init__(self):
        pass
    def Build_Url(self, address,year):
        common_url='https://www.baidu.com/s?ie=UTF-8&tn=null&wd='
        unique_url=(u"%s%d年预算执行情况和%d年财政预算草案"%(address,year,year+1)).strip()
        print unique_url
        #final_url=u"%s%s"%(common_url,unique_url)
        final_url= "http://www.baidu.com/s?wd=" + urllib.quote(unique_url.decode(sys.stdin.encoding).encode('gbk'))
        return final_url,unique_url