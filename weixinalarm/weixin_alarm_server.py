#-* coding:utf-8
from wechat_sender import *
from wxpy import *
import logging

import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
bot = Bot(qr_path="qr.png")
group = bot.groups().search(unicode('微信测试'))[0]
logging.basicConfig(level=logging.DEBUG)
group.send("接入成功!")
print("微信登陆成功！进行监控报警功能！")
print(group)
listen(bot, token='test', receivers=[group],port=15555)
