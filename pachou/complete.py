#调用urllib.request模块
import time
import urllib.request
from bs4 import BeautifulSoup
#定义一个名为get_webInfo的函数，传入参数url
# url_list=['http://wz.lanzh.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.lanzh.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.cd-rail.com/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.cd-rail.com/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.xian.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.xian.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.huhht.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.huhht.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.qingz.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.qingz.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1']
url_list=['https://www.freebuf.com/news','https://www.freebuf.com/vuls','https://github.com/scrapinghub/splash/issues','https://www.77169.net/hacker']
def get_webInfo(url):
    req = urllib.request.Request(url)
    # 将服务器返回的页面放入rsp变量
    rsp = urllib.request.urlopen(req)
    # 读取这个页面，并解码成utf-8格式，忽略错误,放入变量html中
    html = rsp.read().decode('utf-8', 'ignore')
    # 使用BeautifulSoup模块解析变量中的web内容
    html = BeautifulSoup(html, 'html.parser')
    # 循环找出所有的a标签，并赋值给变量 link
    result = []
    for link in html.find_all('a'):
        # 把href中的内容赋值给info_link
        info_link = link.get('href')
        title = link.get("title")
        # 把a标签中的文字赋值给info_text,并去除空格
        info_text = link.get_text(strip=True)
        # 打印出info_text和info_link，并换行
        if (title == info_text):
            result.append(info_text + '\n' + info_link+'\n')
    return result[0]
def get_webGitHubInfo(url):
    req = urllib.request.Request(url)
    # 将服务器返回的页面放入rsp变量
    rsp = urllib.request.urlopen(req)
    # 读取这个页面，并解码成utf-8格式，忽略错误,放入变量html中
    html = rsp.read().decode('utf-8', 'ignore')
    # 使用BeautifulSoup模块解析变量中的web内容
    html = BeautifulSoup(html, 'html.parser')
    # 循环找出所有的a标签，并赋值给变量 link
    result = []
    for link in html.find_all('a'):
        # 把href中的内容赋值给info_link
        info_link = link.get('href')
        title = link.get("title")
        id = link.get("id")
        info_text = link.get_text(strip=True)
        if (id is not None):
            if (("issue_" in id) and ("_link" in id)):
                # 打印出info_text和info_link，并换行
                result.append(info_text + '\n' + "https://github.com"+info_link + '\n')
    return result[0]
def get_webHuaMengInfo(url):
    req = urllib.request.Request(url)
    # 将服务器返回的页面放入rsp变量
    rsp = urllib.request.urlopen(req)
    # 读取这个页面，并解码成utf-8格式，忽略错误,放入变量html中
    html = rsp.read().decode('utf-8', 'ignore')
    # 使用BeautifulSoup模块解析变量中的web内容
    html = BeautifulSoup(html, 'html.parser')
    # 循环找出所有的a标签，并赋值给变量 link
    result = []
    for link in html.find_all('a'):
        # 把href中的内容赋值给info_link
        info_link = link.get('href')
        title = link.get("title")
        # 把a标签中的文字赋值给info_text,并去除空格
        info_text = link.get_text(strip=True)
        # 打印出info_text和info_link，并换行
        # print(info_text+'\n'+info_link)
        if ((title == info_text) and (len(title) > 1) and (title != "congtou") and (title != "返回顶部")
                and (title != "SIREN") and (title != "忘记密码") and (title != "华盟网")):
            result.append(info_text+'\n'+info_link)
    return result[0]
def parseWeb(url_list):
    # 初始化result为一个列表
    result = []
    for url in url_list:
        if("github" in url):
            webInfo = get_webGitHubInfo(url)
        #每循环一次，就调用get_webInfo，传入参数url，解析出结果，存入变量webInfo
        elif("77169" in url):
            webInfo = get_webHuaMengInfo(url)
        else:
            webInfo=get_webInfo(url)
        # print(webInfo)
        #每循环一次，就将解析结果放入result列表中
        result.append(webInfo)
    # 函数执行结束后，return(输出) result
    return result
import json
import requests

def message(value):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=5fdf641cc4316c8046c97497611d3c254af7bd12dad99b285234d03707b9ad12'
    result=value.split('\n')
    data = {
        "msgtype": "link",
        "link": {
            "title": "测试complete",
            "text": result[0],
            "picUrl": result[1],
            "messageUrl": result[1]
            # "picUrl": "https://vpic.video.qq.com/71193249/k08847ssbvm.png",
            # "messageUrl": "https://www.cnblogs.com/tjp40922/p/11299023.html"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps(data).encode("utf-8")
    print(data)
    abc=requests.post(url, data=data, headers=headers)
    return abc
#定义一个字典，包含一个空元素history
tmp = {'history':None}
#定义一个比对函数check()
def check():
    #判断字典内的元素history不为空
    if (tmp['history']):
        #把临时值给tmp字典内的history元素 用于循环比较
        history = tmp['history']
        now = parseWeb(url_list)
        # 大前提，history的列表长度等于now的列表长度
        if len(history) == len(now):
            # 定义一个空的变量 result
            result = ''
            # 使用zip函数，对history和now函数按顺序进行对比
            for a, b in zip(history, now):
                # print(b)
                if a == b:
                    print('未发现更新！')
                else:
                    print('发现更新')
                    # 等价于result=result+b 发现更新就在变量result内添加内容，不会覆盖
                    result += b
                    message(b)

                    # ...
                    # 发送邮件...

            # 注意空格，上面for循环执行后才会执行下面的if判断
            # 为防止误判，两次获取内容都为空也满足len(history)==len(now),对result进行非空判断
            if result != '':
                # 输出结果
                print('更新内容如下:' + result)
        else:
            print('数据错误！')
            # ...比较过程...
        #比较完成后把值覆盖传递
        tmp["history"] = now
    else:
        #如果tmp里的history元素为空则判定第一次运行
        tmp['history'] = parseWeb(url_list)
#无限循环
while True:
    check()
    print('\n休息20秒继续运行！')
    time.sleep(20)
    print('继续工作...')