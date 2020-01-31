#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 上午10:59
# @Author  : 张新礼
# @File    : 钉钉自动发消息.py
# @Software: PyCharm
import json
import requests


def message(value):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=5fdf641cc4316c8046c97497611d3c254af7bd12dad99b285234d03707b9ad12'
    result=value.split('\n')
    data = {
        "msgtype": "link",
        "link": {
            "title": "测试",
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
    data = json.dumps(data)
    print(data)
    abc=requests.post(url, data=data, headers=headers)
    return abc



if __name__ == "__main__":
    abc = "ceshi_1:"+'\n'+"ceshi_2"
    result=message(abc)
    print(result)
    # result=message1()
    # print(result)