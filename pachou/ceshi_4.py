#coding=utf-8
#调用urllib.request模块
import urllib.request
from bs4 import BeautifulSoup
#freebuf
#https://www.freebuf.com/vuls    （漏洞信息）
#https://www.freebuf.com/news    （安全事件）
#定义url地址
url0='https://www.freebuf.com/news'
url1='https://www.freebuf.com/vuls'
url='https://securityaffairs.co/wordpress/'
#定义发送的请求
req=urllib.request.Request(url)
#将服务器返回的页面放入rsp变量
rsp=urllib.request.urlopen(req)
#读取这个页面，并解码成utf-8格式，忽略错误,放入变量html中
html=rsp.read().decode('utf-8','ignore')
#使用BeautifulSoup模块解析变量中的web内容
html=BeautifulSoup(html,'html.parser')
#循环找出所有的a标签，并赋值给变量 link
result = []
for link in html.find_all('a'):
    #把href中的内容赋值给info_link
    info_link=link.get('href')
    title = link.get("title")
    info_text = link.get_text(strip=True)
    print(info_text + '\n' + info_link)
    if(title==info_text):
        print(info_text + '\n' + info_link)
        result.append(info_text+'\n'+info_link)
    # print(result[0])
    # print(url[:-50]+info_link+'\n')
