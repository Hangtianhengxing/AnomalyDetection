#调用urllib.request模块
import time
import urllib.request
from bs4 import BeautifulSoup
#定义一个名为get_webInfo的函数，传入参数url
url_list=['http://wz.lanzh.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.lanzh.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.cd-rail.com/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.cd-rail.com/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.xian.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.xian.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.huhht.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.huhht.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1','http://wz.qingz.95306.cn/mainPageNoticeList.do?method=init&id=2000001&cur=1','http://wz.qingz.95306.cn/mainPageNoticeList.do?method=init&id=2200001&cur=1']
def get_webInfo(url):
    req = urllib.request.Request(url)
    rsp = urllib.request.urlopen(req)
    html = rsp.read().decode('utf8','ignore')
    html = BeautifulSoup(html,'html.parser')
    for link in html.find_all('a',limit=3):
        info_link = link.get('href')
        info_text = link.get_text(strip=True)
    #函数执行完后，return(输出)执行的结果
    return info_text+'\n'+url[:-50]+info_link+'\n'
def parseWeb(url_list):
    # 初始化result为一个列表
    result = []
    for url in url_list:
        #每循环一次，就调用get_webInfo，传入参数url，解析出结果，存入变量webInfo
        webInfo = get_webInfo(url)
        print(webInfo)
        #每循环一次，就将解析结果放入result列表中
        result.append(webInfo)
    # 函数执行结束后，return(输出) result
    return result
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
                if a == b:
                    print('未发现更新！')
                else:
                    print('发现更新')
                    # 等价于result=result+b 发现更新就在变量result内添加内容，不会覆盖
                    result += b

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
    print('\n休息3秒继续运行！')
    time.sleep(3)
    print('继续工作...')