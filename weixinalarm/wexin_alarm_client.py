# -*- coding:UTF-8 -*-

from wechat_sender import *
import time
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
import ssl
context = ssl._create_unverified_context()
sender = Sender(token='test', receivers=unicode('微信测试'),port=15555)
while True:
    time.sleep(10)
   # sender.send(message=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    sender.send(message='测试数据'+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
