#!/usr/bin/env python
# coding: utf-8
import json
import requests
import time
from datetime import datetime

def dingding_robot(data):
    # 机器人的webhooK 获取地址参考：https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq
    #https://oapi.dingtalk.com/robot/send?access_token=5fdf641cc4316c8046c97497611d3c254af7bd12dad99b285234d03707b9ad12
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=5fdf641cc4316c8046c97497611d3c254af7bd12dad99b285234d03707b9ad12"
    headers = {'content-type': 'application/json'} # 请求头
    r = requests.post(webhook, headers=headers, data=json.dumps(data))
    r.encoding = 'utf-8'
    return (r.text)


if __name__ == "__main__":
    # 请求参数 可以写入配置文件中
    data = {
        "msgtype": "link",
        "link": {
            "title": "FreeBuf早报 | 工信部发布《网络安全漏洞管理规定 (征求意见稿) 》公开征求意见；Linux 和 FreeBSD 被曝多个 DoS 漏洞；谷歌日历出现故障，持续数小时后才恢复 - FreeBuf互联网安全新媒体平台</title>",
            "text": "FreeBuf互联网安全新媒体平台",
            "picUrl": "https://vpic.video.qq.com/71193249/k08847ssbvm.png",
            "messageUrl": "https://www.freebuf.com/news/*.html"
        }
    }
    res = dingding_robot(data)
    print(res) # 打印请求结果

# while True:
#  if datetime.now() < datetime(2088, 9,4, 23, 59, 59):  # 查询截止时间为2088-9-4 23:59:59
#     post_data()
#     time.sleep(1)  # 每隔一分钟查询一次
#  else:
#     print("已到截止时间，停止取数。")
#     break