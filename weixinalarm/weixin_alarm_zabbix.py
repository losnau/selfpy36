# coding=utf-8
import requests
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def gettoken(corpid, corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    response = requests.get(gettoken_url)
    token_json = json.loads(response.content)
    print 'accesstoken=' + token_json['access_token']
    return token_json['access_token']

def get_pic_id(accesstoken, path):  ##上传到临时素材  图片ID
    img_url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={}&type=image".format(accesstoken)
    files = {'image': open(path, 'rb')}
    response = requests.post(img_url, files=files)
    pic_json = json.loads(response.content)
    print '上传图片返回网页内容:' + response.content
    return pic_json['media_id']

def send_weixin(accesstoken, pic_id):
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + accesstoken
    post_data = {
        "toparty": "2",
        "msgtype": "mpnews",
        "agentid": "1000002",
        "mpnews": {
            "articles": [
                {
                    "title": "图片标题",
                    "thumb_media_id": pic_id,
                    "author": "作者",
                    "content": "文章内容",
                    "digest": "图片描述",
                    "show_cover_pic": "0"
                },
            ]
        },
        "safe": 0
    }
    #在这里必须对整个json.dumps之后的unicon编码变成utf-8的编码企业微信接口只支持utf-8编码
    send_data = json.dumps(post_data, ensure_ascii=False).encode('utf-8')
    print 2, type(send_data)
    print 1, send_data
    send_response = requests.post(send_url, send_data)
    print '返回状态：',
    print send_response.status_code
    print '返回内容',
    print send_response.content

path = '1.jpg'
corpid = 'xxxx'  # CorpID是企业号的标识
corpsecret = 'xxxxxx'  # '这里填写应用对应的secret
accesstoken = gettoken(corpid, corpsecret)
pic_id = get_pic_id(accesstoken, path)
send_weixin(accesstoken, pic_id)
