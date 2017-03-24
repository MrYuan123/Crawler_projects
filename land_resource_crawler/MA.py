#! /usr/bin/env python
# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup

#用于进行土地资源网中的资料整理，汇总成csv文件

def start(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    headers = {
        "Host": "www.landchina.com",
        "User_Agent": user_agent,
        "Cookie": "ASP.NET_SessionId=euv1yzpbfmg33qvph1puvrfr; Hm_lvt_83853859c7247c5b03b527894622d3fa=1488272101,1488353609,1488453589,1488551017; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1488551678",
        # "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8",
        # "Accept - Encoding": "gzip, deflate, sdch",
        # "Accept - Language": "zh - CN, zh;q = 0.8",
        # "Cache - Control":"max - age = 0",
        "Connection":"keep - alive",
        # "Upgrade - Insecure - Requests": "1",
    }
    try:
        req = requests.get(url, headers=headers,timeout=60)
    except:
        print(u"下载信息网页失败："+url)
        return None

    soup = BeautifulSoup(req.text, "html.parser")
    items = soup.find( 'table', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1")

    D=[]
    for i in range(0,26):
        D.append(0)
    info = {}

    try:
        # 行政区
        division = items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c2_ctrl").get_text().encode('utf-8')
        info['XingZhengQu'] = division
        D[0]=info['XingZhengQu']

        #电子监管号
        info["dianzijianguanhao"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c4_ctrl").get_text().encode('utf-8')
        D[1]=info["dianzijianguanhao"]

        #项目名称
        info["xiangmumingcheng"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r17_c2_ctrl").get_text().encode('utf-8')
        D[2]= info["xiangmumingcheng"]
        # 项目位置
        location = items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r16_c2_ctrl").get_text().encode('utf-8')
        info['XiangMuWeiZhi'] = location
        D[3]=info['XiangMuWeiZhi']

        # 面积(公顷)
        square = items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c2_ctrl").get_text().encode('utf-8')
        info['MianJi'] = square
        D[4] =info['MianJi']
        #土地来源
        info["tudilaiyuan"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c4_ctrl").get_text().encode('utf-8')
        D[5] =info["tudilaiyuan"]
        # 土地用途
        purpose = items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c2_ctrl").get_text().encode('utf-8')
        info['TuDiYongTu'] = purpose
        D[6] =info['TuDiYongTu']
        # 供地方式
        source = items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c4_ctrl").get_text().encode('utf-8')
        info['GongDiFangShi'] = source
        D[7] =info['GongDiFangShi']
        #土地使用年限
        info["shiyongnianxian"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r19_c2_ctrl").get_text().encode('utf-8')
        D[8] =info["shiyongnianxian"]
        #行业分类
        info["hangyefenlei"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r19_c4_ctrl").get_text().encode('utf-8')
        D[9] =info["hangyefenlei"]
        #土地级别
        info["tudijibie"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c2_ctrl").get_text().encode('utf-8')
        D[10] =info["tudijibie"]
        # 成交价格(万元)
        price = items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c4_ctrl").get_text().encode('utf-8')
        info['ChengJiaoJiaGe'] = price
        D[11] =info['ChengJiaoJiaGe']
        #支付期号
        try:
            info["zhifuqihao"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c1_0_ctrl").get_text().encode('utf-8')
        except:
            info["zhifuqihao"] =""
        D[12] =info["zhifuqihao"]
        #约定支付时间
        try:
            info["YDZFRQ"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c2_0_ctrl").get_text().encode('utf-8')
        except:
            info["YDZFRQ"]=""
        D[13] =info["YDZFRQ"]

        #约定支付金额
        try:
            info["YDZFJE"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c3_0_ctrl").get_text().encode('utf-8')
        except:
            info["YDZFJE"]=""
        D[14] =info["YDZFJE"]
        #备注
        try:
            info["beizhu"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c4_0_ctrl").get_text().encode('utf-8')
        except:
            info["beizhu"]=""
        D[15] =info["beizhu"]

        #土地使用权人
        info["TDSYQR"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r9_c2_ctrl").get_text().encode('utf-8')
        D[16] =info["TDSYQR"]

        #约定容积率(下限)
        info["XIAXIAN"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f2_r1_c2_ctrl").get_text().encode('utf-8')
        D[17] =info["XIAXIAN"]

        #约定容积率(上限)
        info["SHANGXIAN"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f2_r1_c4_ctrl").get_text().encode('utf-8')
        D[18] =info["SHANGXIAN"]

        #约定交地时间
        info["YDJDSJ"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r21_c4_ctrl").get_text().encode('utf-8')
        D[19] =info["YDJDSJ"]

        #约定开工时间
        info["YDKGSJ"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c2_ctrl").get_text().encode('utf-8')
        D[20] =info["YDKGSJ"]

        #约定竣工时间
        info["YDJGSJ"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c4_ctrl").get_text().encode('utf-8')
        D[21] =info["YDJGSJ"]

        #实际开工时间
        info["SJKGSJ"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r10_c2_ctrl").get_text().encode('utf-8')
        D[22] =info["SJKGSJ"]

        #实际竣工时间
        info["SJJGSJ"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r10_c4_ctrl").get_text().encode('utf-8')
        D[23] =info["SJJGSJ"]

        #批准单位
        info["PZDW"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c2_ctrl").get_text().encode('utf-8')
        D[24] =info["PZDW"]

        #合同签订日期
        info["HTQDRQ"]=items.find('span', id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c4_ctrl").get_text().encode('utf-8')
        D[25] =info["HTQDRQ"]
    except:
        return None

    # for key in info:
    #     if info[key]=="":
    #         print(key+" : "+info[key])
    #     else:
    #         print(key+" : "+str(info[key],"utf-8"))
    try:
        m=float(info["tudilaiyuan"])
    except:
        D[5]=info["tudilaiyuan"]
        return D

    if float(info["tudilaiyuan"])==0:
        #print(u"新增建设用地")
        info["tudilaiyuan"]=u"新增建设用地".encode("utf-8")
    else:
        if info["tudilaiyuan"]==info["MianJi"]:
            #print(u"现有建设用地")
            info["tudilaiyuan"] = u"现有建设用地".encode("utf-8")
        else:
            #print(u"库存用地")
            info["tudilaiyuan"] = u"新增建设用地(来自存量库)".encode("utf-8")

    D[5]=info["tudilaiyuan"]
    return D

if __name__=="__main__":
    #now_url="http://www.landchina.com/default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=497E1DE69C8C2F94E055000000000001"
    #now_url="http://www.landchina.com/default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=20e8af8e-7249-4841-aa42-cb495582774f"
    now_url="http://www.landchina.com/default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=908df55f-97e1-4d33-8e34-0f518269e870"
    start(now_url)