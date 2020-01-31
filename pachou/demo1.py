#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 上午10:59
# @Author  : 张新礼
# @File    : 钉钉自动发消息.py
# @Software: PyCharm
import json
import requests

def message(link=1):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=5fdf641cc4316c8046c97497611d3c254af7bd12dad99b285234d03707b9ad12'
    abc = "ceshi_1" + '\n' + "ceshi_2"
    value = abc.split("\n")
    data = {
        "msgtype": "link",
        "link": {
            "title": "ceshi_1:"+value[0],
            "text": "ceshi_1:"+value[0],
            "picUrl": "ceshi_1:"+value[1],
            "messageUrl": "ceshi_1:"+value[1]
        }
    }
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "您的自动化测试报告已生成：%s " % (link)
        },
        "at": {
            "atMobiles": [
                "14755721700"  # 需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": False  # 是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    print(data)
    abc=requests.post(url, data=data, headers=headers)
    return abc
def message(link=1):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=5fdf641cc4316c8046c97497611d3c254af7bd12dad99b285234d03707b9ad12'

    data = {
        "msgtype": "link",
        "link": {
            "title": "测试",
            "text": "abc",
            "picUrl": "abc",
            "messageUrl": "abc"
            # "picUrl": "https://vpic.video.qq.com/71193249/k08847ssbvm.png",
            # "messageUrl": "https://www.cnblogs.com/tjp40922/p/11299023.html"
        }
    }
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "您的自动化测试报告已生成：%s " % (link)
        },
        "at":{
            "atMobiles":[
                "14755721700"       #需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": False        #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    print(data)
    abc=requests.post(url, data=data, headers=headers)
    return abc