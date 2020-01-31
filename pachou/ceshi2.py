#调用urllib.request模块
import urllib.request
from bs4 import BeautifulSoup
url_list=['http://wz.lanzh.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.lanzh.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.cd-rail.com/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.cd-rail.com/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.xian.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.xian.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.huhht.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.huhht.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.qingz.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.qingz.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1']
#第一层循环，把url都导出来
for url in url_list:
    #定义发送的请求
    req=urllib.request.Request(url)
    #将服务器返回的页面放入rsp变量
    rsp=urllib.request.urlopen(req)
    #读取这个页面，并解码成utf-8格式，忽略错误,放入变量html中
    html=rsp.read().decode('utf-8','ignore')
    #使用BeautifulSoup模块解析变量中的web内容
    html=BeautifulSoup(html,'html.parser')
    #第二层循环，找出所有的a标签，并赋值给变量 link
    for link in html.find_all('a',limit=3):
        #把href中的内容赋值给info_link
        info_link=link.get('href')
        #把a标签中的文字赋值给info_text,并去除空格
        info_text=link.get_text(strip=True)
    #打印出info_text和info_link，并换行
    print(info_text)
    print(url[:-50]+info_link+'\n')