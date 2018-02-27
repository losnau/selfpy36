#-*-coding:utf-8
'''
优化第一版：类实现
'''
import requests
import re
Base_URL = "http://cmdb.shijinshi.cn/login/?next=/"
Login_URL = "http://cmdb.shijinshi.cn/login/?next=/"

def get_github_html(url):
    '''
    这里用于获取登录页的html，以及cookie
    :param url: https://github.com/login
    :return: 登录页面的HTML,以及第一次的cooke
    '''
    response = requests.get(url)
    first_cookie = response.cookies.get_dict()
    return response.text,first_cookie



def get_token(html):
    '''
    处理登录后页面的html
    :param html:
    :return: 获取csrftoken
    '''
    #print html
    pattern = re.compile('<input name="authenticity_token".*?value="(.*?)" />', re.S)
    result = re.search(pattern, html)

    if result:
        print result.group(1).strip()
        return result.group(1).strip()
    else:
        print "None"
        return None

def gihub_login(url,token,cookie):
    '''
    这个是用于登录
    :param url: https://github.com/session
    :param token: csrftoken
    :param cookie: 第一次登录时候的cookie
    :return: 返回第一次和第二次合并后的cooke
    '''

    data= {
        "csrfmiddlewaretoken":token,
        "login":"admin",
        "password":"xxxx"
    }
    response = requests.post(url,data=data,cookies=cookie)
    print(response.status_code)
    cookie = response.cookies.get_dict()
    #这里注释的解释一下，是因为之前github是通过将两次的cookie进行合并的
    #现在不用了可以直接获取就行
    # cookie.update(second_cookie)
    return cookie


if __name__ == '__main__':
    html,cookie = get_github_html(Base_URL)
    token = get_token(html)
    cookie = gihub_login(Login_URL,token,cookie)
    response = requests.get("http://cmdb.shijinshi.cn/data_center/datacenterasset/?all",cookies=cookie)
    print(response.text)
