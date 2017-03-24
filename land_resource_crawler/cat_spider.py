#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import re

import codecs
import sys
import csv

import time
from bs4 import BeautifulSoup
import requests
from land_resource_spider import MA

class spiderCat(object):

    #初始化参数
    def __init__(self):
        self.temp=1
        self.antiS=0
        self.EN = 0
        self.SN = 0
        self.requrl = "http://www.landchina.com/default.aspx?tabid=263&ComName=default"
        #self.requrl="http://www.landchina.com/default.aspx?tabid=263"
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        self.headers = {
            "Host": "www.landchina.com",
            "User_Agent": self.user_agent
        }
        self.data={
        }

    #获得post_data的初值
    def get_post_data(self):
        # 访问一次网页,获取post需要的信息
        data = {
            'TAB_QuerySubmitSortData': '',
            'TAB_RowButtonActionControl': '',
        }

        try:
            req = requests.get(self.requrl, headers=self.headers)
        except:
            print('get baseurl failed, try again!')
        try:
            soup = BeautifulSoup(req.text, "html.parser")
            TAB_QueryConditionItem = soup.find(
                'input', id="TAB_QueryConditionItem270").get('value')
            # print TAB_QueryConditionItem
            data['TAB_QueryConditionItem'] = TAB_QueryConditionItem
            TAB_QuerySortItemList = soup.find(
                'input', id="TAB_QuerySort0").get('value')
            # print TAB_QuerySortItemList
            data['TAB_QuerySortItemList'] = TAB_QuerySortItemList
            data['TAB_QuerySubmitOrderData'] = TAB_QuerySortItemList
            __EVENTVALIDATION = soup.find(
                'input', id='__EVENTVALIDATION').get('value')
            # print __EVENTVALIDATION
            data['__EVENTVALIDATION'] = __EVENTVALIDATION
            __VIEWSTATE = soup.find('input', id='__VIEWSTATE').get('value')
            # print __VIEWSTATE
            data['__VIEWSTATE'] = __VIEWSTATE
        except:
            print('get post data failed, try again!')

        self.data=data
        return

    #下载特定目录网页
    def downloadCat(self,Ndata,Ntitle):
        Flag=True
        Npage=1
        Scount=0

        if self.temp==1:   #爬取剩余的
            Npage=1
            self.temp=0

        while Flag==True:
            Mdata=self.data
            Mdata['TAB_QuerySubmitConditionData'] = Mdata['TAB_QueryConditionItem'] + ':' + Ndata
            Mdata['TAB_QuerySubmitPagerData'] = str(Npage)

            #三层访问，保证不会出错
            try:
                req = requests.post(self.requrl, data=Mdata, headers=self.headers)
            except:
                print(u"===========================目录页下载不通，休眠300秒！==============================")
                time.sleep(300)
                try:
                    req = requests.post(self.requrl, data=Mdata, headers=self.headers)
                except:
                    print(u"===========================目录页下载还是不通，休眠60秒！==============================")
                    time.sleep(60)
                    try:
                        req = requests.post(self.requrl, data=Mdata, headers=self.headers)
                    except:
                        with open("detailE.txt", "a") as F:
                            F.write(Durl)
                            F.write("\n")
                        return

            Hcontent=req.content

            # with open("fu.htm","wb") as f:
            #       f.write(Hcontent)

            soup=BeautifulSoup(Hcontent,"html.parser")

            #获取总页数
            if Scount==0:
                nextP = soup.find("td", align="right", class_="pager")
                print(nextP)
                try:
                    Sum=int(re.findall(r"共(.+)页", str(nextP))[0])
                except:
                    print(u"%s 获取错误！"%Ndata)
                    with open("error.txt","a") as f:
                        f.write(Ndata)
                        f.write("\n")
                    return

                print(u"共%d页" % Sum)
                Scount=1


            #处理当前目录页信息
            items = soup.find('table', id="TAB_contentTable").find_all('tr', onmouseover=True)

            #循环处理信息页
            for item in items:
                self.antiS+=1
                if self.antiS>1000:
                    print(u"反爬虫！暂停三分钟")
                    time.sleep(180)
                    self.antiS=0

                # Stime=random.uniform(0,2)
                # print(u"休眠:",Stime)
                # time.sleep(Stime)
                print("=========================================================")
                print("anti-spider flag:%d"%self.antiS)
                print("success:%d error:%d"%(self.SN,self.EN))
                print("=========================================================")
                print(item.find('td').get_text())
                link = item.find('a')
                if link:
                    try:
                        print(item.find('a').text)
                        Durl = 'http://www.landchina.com/' + item.find('a').get('href')
                    except:
                        self.EN+=1
                        continue
                    #info=MA.start(str(Durl))      另外一种
                    D = MA.start(str(Durl))
                    if D==None:
                        print(u"Error!")
                        with open("detailE.txt","a") as F:
                            F.write(Durl)
                            F.write("\n")
                        self.EN+=1
                        continue

                    self.store(D,Ntitle)    #存储结果
                    self.SN+=1
                    #打印结果
                    # for key in info:
                    #     if info[key] == "":
                    #         print(key + " : " + info[key])
                    #     else:
                    #         print(key + " : " + str(info[key], "utf-8"))
                else:
                    print('no content, this ten days over')
                    self.EN+=1

            #用于寻找下一页

            # ALLitem=soup.find_all("a")
            # Flag=False
            # for Nitem in ALLitem:
            #     if Nitem.text==u"下页":
            #         if(str(Nitem).find("onclick")!=-1):     #查找成功的条件
            #             Flag = True
            #             #print("成功！")

            Npage+=1
            if Npage>Sum:
                Flag=False
       # with open("detail.html", "wb") as f:
       # f.write(Hcontent)

    def store(self,D,title):
        M=[]

        for item in D:
            if item=="":
                #print(item)
                M.append(item)
            else:
               #print(str(item,"utf-8"))
               M.append(str(item,"utf-8"))
        print(M)
        # for item in info:
        #     print(item+" : "+str(info[item],"utf-8"))
        #     info[item]=str(info[item],"utf-8")

        #print(info.values())

        # #暂存
        csvfile = open(title, 'a',encoding="utf-8",newline="")
        writer = csv.writer(csvfile,dialect='excel')
        st=[]
        st.append(M)
        writer.writerows(st)
        csvfile.close()

if __name__=="__main__":
    OS=spiderCat()
    OS.get_post_data()
    #print(OS.data)

    firstT=(u"行政区",u"电子监督号",u"项目名称",u"项目位置",u"面积（公顷）",u"土地来源",u"土地用途",u"供地方式",u"土地使用年限",u"行业分类",u"土地级别",u"成交价格（万元）",u"支付期号",u"约定支付时间",u"约定支付金额",u"备注",u"土地使用权人",u"约定容积率（下限）",u"约定容积率（上限）",u"约定交地时间",u"约定开工时间",u"约定竣工时间",u"实际开工时间",u"实际竣工时间",u"批准单位",u"合同签订日期")

    # title="2007-2.csv"
    # csvfile = open(title, 'a',encoding="utf-8",newline="")
    # writer = csv.writer(csvfile,dialect='excel')
    # st = []
    # st.append(firstT)
    # writer.writerows(st)
    # csvfile.close()
    #
    # for num in range(16,29):
    #     #print(num)
    #     date="2007-2-%d~2007-2-%d"%(num,num)
    #     with open("flag.txt","w") as f:
    #         f.write(date)
    #     OS.downloadCat(date,title)

    #11月
    title = "2007-11.csv"
    csvfile = open(title, 'a', encoding="utf-8", newline="")
    writer = csv.writer(csvfile, dialect='excel')
    st = []
    st.append(firstT)
    writer.writerows(st)
    csvfile.close()

    for num in range(1,31):
        # print(num)
        date = "2007-11-%d~2007-11-%d" % (num, num)
        with open("flag.txt", "w") as f:
            f.write(date)
        OS.downloadCat(date, title)

    #12月
    title = "2007-12.csv"
    csvfile = open(title, 'a', encoding="utf-8", newline="")
    writer = csv.writer(csvfile, dialect='excel')
    st = []
    st.append(firstT)
    writer.writerows(st)
    csvfile.close()

    for num in range(1, 31):
        # print(num)
        date = "2007-12-%d~2007-12-%d" % (num, num)
        with open("flag.txt", "w") as f:
            f.write(date)
        OS.downloadCat(date, title)