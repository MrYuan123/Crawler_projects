import urllib

from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import requests

class spider(object):
    def __init__(self):
        self.requrl = "http://www.landchina.com/default.aspx?tabid=263&ComName=default"
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        self.cookie = "ASP.NET_SessionId=sqnivjhrima0lfmkqcfovrif; Hm_lvt_83853859c7247c5b03b527894622d3fa=1488201130,1488272101; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1488272201"
        self.headers={
            # "Accept":"text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8",
            # "Accept - Encoding": "gzip, deflate",
            # "Accept - Language":"zh - CN, zh;q = 0.8",
            # "Cache - Control":"max - age = 0",
            # "Connection":"keep - alive",
            # "Content - Length":"3119",
            # "Content - Type":"application / x - www - form - urlencoded",
            # "Referer":"http: // www.landchina.com / default.aspx?tabid = 263 & ComName = default",
            # "Upgrade - Insecure - Requests":"1",
            "Host":"www.landchina.com",
            #"Origin":"http:// www.landchina.com",
            "User_Agent":self.user_agent,
            #"Cookie":self.cookie
        }

    def spider_start(self):

        requrl = "http://www.landchina.com/default.aspx?tabid=263&ComName=default"

        Mdata = {
            "TAB_QuerySubmitConditionData":"9f2c3acd-0256-4da2-a659-6949c4671a2a: 2014-1-1~2014-12-31",
            "TAB_QuerySubmitPagerData": "1",

            "__VIEWSTATE": "/ wEPDwUJNjkzNzgyNTU4D2QWAmYPZBYIZg9kFgICAQ9kFgJmDxYCHgdWaXNpYmxlaGQCAQ9kFgICAQ8WAh4Fc3R5bGUFIEJBQ0tHUk9VTkQtQ09MT1I6I2YzZjVmNztDT0xPUjo7ZAICD2QWAgIBD2QWAmYPZBYCZg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHgRUZXh0ZWRkAgEPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFhgFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bC9VcGxvYWQvc3lzRnJhbWVJbWcveF90ZHNjd19zeV9qaGdnXzAwMC5naWYpOx4GaGVpZ2h0BQEzFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgRmD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAICD2QWAmYPZBYEZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYCZg8WBB8BBSBDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6Ox8AaBYCZg9kFgICAQ9kFgJmDw8WAh8CZWRkAgIPZBYEZg9kFgJmD2QWAmYPZBYCZg9kFgICAQ9kFgJmDxYEHwEFhQFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bC9VcGxvYWQvc3lzRnJhbWVJbWcveF90ZHNjd196eV9qZ2dnXzAxLmdpZik7HwMFAjQ2FgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAQ9kFgJmD2QWAmYPZBYCZg9kFgICAQ9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAw9kFgICAw8WBB4JaW5uZXJodG1sBf0GPHAgYWxpZ249ImNlbnRlciI + PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZTogeC1zbWFsbCI + Jm5ic3A7PGJyIC8 + DQombmJzcDs8YSB0YXJnZXQ9Il9zZWxmIiBocmVmPSJodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vIj48aW1nIGJvcmRlcj0iMCIgYWx0PSIiIHdpZHRoPSIyNjAiIGhlaWdodD0iNjEiIHNyYz0iL1VzZXIvZGVmYXVsdC9VcGxvYWQvZmNrL2ltYWdlL3Rkc2N3X2xvZ2UucG5nIiAvPjwvYT4mbmJzcDs8YnIgLz4NCiZuYnNwOzxzcGFuIHN0eWxlPSJjb2xvcjogI2ZmZmZmZiI + Q29weXJpZ2h0IDIwMDgtMjAxNCBEUkNuZXQuIEFsbCBSaWdodHMgUmVzZXJ2ZWQmbmJzcDsmbmJzcDsmbmJzcDsgPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KdmFyIF9iZGhtUHJvdG9jb2wgPSAoKCJodHRwczoiID09IGRvY3VtZW50LmxvY2F0aW9uLnByb3RvY29sKSA / ICIgaHR0cHM6Ly8iIDogIiBodHRwOi8vIik7DQpkb2N1bWVudC53cml0ZSh1bmVzY2FwZSgiJTNDc2NyaXB0IHNyYz0nIiArIF9iZGhtUHJvdG9jb2wgKyAiaG0uYmFpZHUuY29tL2guanMlM0Y4Mzg1Mzg1OWM3MjQ3YzViMDNiNTI3ODk0NjIyZDNmYScgdHlwZT0ndGV4dC9qYXZhc2NyaXB0JyUzRSUzQy9zY3JpcHQlM0UiKSk7DQo8L3NjcmlwdD4mbmJzcDs8YnIgLz4NCueJiOadg + aJgOaciSZuYnNwOyDkuK3lm73lnJ / lnLDluILlnLrnvZEmbmJzcDsmbmJzcDvmioDmnK / mlK / mjIE65rWZ5rGf6Ie75ZaE56eR5oqA5pyJ6ZmQ5YWs5Y + 4Jm5ic3A75LqR5Zyw572RPGJyIC8 + DQrlpIfmoYjlj7c6IOS6rElDUOWkhzA5MDc0OTky5Y + 3IOS6rOWFrOe9keWuieWkhzExMDEwMjAwMDY2NigyKSZuYnNwOzxiciAvPg0KPC9zcGFuPiZuYnNwOyZuYnNwOyZuYnNwOzxiciAvPg0KJm5ic3A7PC9zcGFuPjwvcD4fAQVjQkFDS0dST1VORC1JTUFHRTp1cmwoaHR0cDovL3d3dy5sYW5kY2hpbmEuY29tL1VzZXIvZGVmYXVsL1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3MjAxM195d18xLmpwZyk7ZGSKTrkQTAldzzgBNdyqvAtA4LQKM1e5pBheP3zSHmiaHw ==",
            "__EVENTVALIDATION":"/ wEWAgLN8MntAQLN3cj / BL0BH + YBXn6d / 09DMzO1 / n + ueLbo9fc7QJL20bwbCaYp",
            "hidComName":"defaul",
            "TAB_QueryConditionItem": "9f2c3acd - 0256 - 4da2 - a659 - 6949c4671a2a",
            "TAB_QuerySortItemList":"282:False",
            "TAB_QuerySubmitOrderData": "282:False",
            "TAB_RowButtonActionControl":"",
            "TAB_QuerySubmitSortData":""
            }
        # data = urllib.parse.urlencode(data)
        # binary_data = data.encode('utf-8')
        #
        # req= request.Request(self.requrl,data=binary_data,headers=self.headers)
        # resHtml=request.urlopen(req)
        # Hcontent=resHtml.read()
        # print(Hcontent)
        req = requests.post(requrl, data=Mdata, headers=self.headers)
        Hcontent=req.text
        print(Hcontent)
        with open("detail.html","wb") as f:
            f.write(Hcontent)

if __name__=="__main__":
    objectS=spider()
    objectS.spider_start()

#暂时存储
# "TAB_QuerySubmitConditionData":"9f2c3acd-0256-4da2-a659-6949c4671a2a: 2014-1-1~2014-12-31",
# "TAB_QuerySubmitPagerData": "1",
#
# "__VIEWSTATE": "/ wEPDwUJNjkzNzgyNTU4D2QWAmYPZBYIZg9kFgICAQ9kFgJmDxYCHgdWaXNpYmxlaGQCAQ9kFgICAQ8WAh4Fc3R5bGUFIEJBQ0tHUk9VTkQtQ09MT1I6I2YzZjVmNztDT0xPUjo7ZAICD2QWAgIBD2QWAmYPZBYCZg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHgRUZXh0ZWRkAgEPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFhgFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bC9VcGxvYWQvc3lzRnJhbWVJbWcveF90ZHNjd19zeV9qaGdnXzAwMC5naWYpOx4GaGVpZ2h0BQEzFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgRmD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAICD2QWAmYPZBYEZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYCZg8WBB8BBSBDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6Ox8AaBYCZg9kFgICAQ9kFgJmDw8WAh8CZWRkAgIPZBYEZg9kFgJmD2QWAmYPZBYCZg9kFgICAQ9kFgJmDxYEHwEFhQFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bC9VcGxvYWQvc3lzRnJhbWVJbWcveF90ZHNjd196eV9qZ2dnXzAxLmdpZik7HwMFAjQ2FgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAQ9kFgJmD2QWAmYPZBYCZg9kFgICAQ9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAw9kFgICAw8WBB4JaW5uZXJodG1sBf0GPHAgYWxpZ249ImNlbnRlciI + PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZTogeC1zbWFsbCI + Jm5ic3A7PGJyIC8 + DQombmJzcDs8YSB0YXJnZXQ9Il9zZWxmIiBocmVmPSJodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vIj48aW1nIGJvcmRlcj0iMCIgYWx0PSIiIHdpZHRoPSIyNjAiIGhlaWdodD0iNjEiIHNyYz0iL1VzZXIvZGVmYXVsdC9VcGxvYWQvZmNrL2ltYWdlL3Rkc2N3X2xvZ2UucG5nIiAvPjwvYT4mbmJzcDs8YnIgLz4NCiZuYnNwOzxzcGFuIHN0eWxlPSJjb2xvcjogI2ZmZmZmZiI + Q29weXJpZ2h0IDIwMDgtMjAxNCBEUkNuZXQuIEFsbCBSaWdodHMgUmVzZXJ2ZWQmbmJzcDsmbmJzcDsmbmJzcDsgPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KdmFyIF9iZGhtUHJvdG9jb2wgPSAoKCJodHRwczoiID09IGRvY3VtZW50LmxvY2F0aW9uLnByb3RvY29sKSA / ICIgaHR0cHM6Ly8iIDogIiBodHRwOi8vIik7DQpkb2N1bWVudC53cml0ZSh1bmVzY2FwZSgiJTNDc2NyaXB0IHNyYz0nIiArIF9iZGhtUHJvdG9jb2wgKyAiaG0uYmFpZHUuY29tL2guanMlM0Y4Mzg1Mzg1OWM3MjQ3YzViMDNiNTI3ODk0NjIyZDNmYScgdHlwZT0ndGV4dC9qYXZhc2NyaXB0JyUzRSUzQy9zY3JpcHQlM0UiKSk7DQo8L3NjcmlwdD4mbmJzcDs8YnIgLz4NCueJiOadg + aJgOaciSZuYnNwOyDkuK3lm73lnJ / lnLDluILlnLrnvZEmbmJzcDsmbmJzcDvmioDmnK / mlK / mjIE65rWZ5rGf6Ie75ZaE56eR5oqA5pyJ6ZmQ5YWs5Y + 4Jm5ic3A75LqR5Zyw572RPGJyIC8 + DQrlpIfmoYjlj7c6IOS6rElDUOWkhzA5MDc0OTky5Y + 3IOS6rOWFrOe9keWuieWkhzExMDEwMjAwMDY2NigyKSZuYnNwOzxiciAvPg0KPC9zcGFuPiZuYnNwOyZuYnNwOyZuYnNwOzxiciAvPg0KJm5ic3A7PC9zcGFuPjwvcD4fAQVjQkFDS0dST1VORC1JTUFHRTp1cmwoaHR0cDovL3d3dy5sYW5kY2hpbmEuY29tL1VzZXIvZGVmYXVsL1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3MjAxM195d18xLmpwZyk7ZGSKTrkQTAldzzgBNdyqvAtA4LQKM1e5pBheP3zSHmiaHw ==",
# "__EVENTVALIDATION": "/ wEWAgLN8MntAQLN3cj / BL0BH + YBXn6d / 09DMzO1 / n + ueLbo9fc7QJL20bwbCaYp",
# "hidComName": "defaul",
# "TAB_QueryConditionItem": "9f2c3acd - 0256 - 4da2 - a659 - 6949c4671a2a",
# "TAB_QuerySortItemList": "282:False",
# "TAB_QuerySubmitOrderData": "282:False",
# "TAB_RowButtonActionControl": "",
# "TAB_QuerySubmitSortData": ""