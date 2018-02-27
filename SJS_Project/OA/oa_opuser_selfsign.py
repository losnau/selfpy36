#-*-coding:utf-8
import requests
from bs4 import BeautifulSoup
import re
#一个OA，admin用户快速填写我的任务，非自动
'''
可以优化部分
把代码细化，将很多共有部分写成小函数，快速调用，防止写重复代码
例如访问页面返回页面源代码（传入url，返回content）
例如正则解析页面(传入pattern，和content，返回items)
'''
requests.packages.urllib3.disable_warnings()
'''
一个OA的类，快速从网页拉去我的任务，手动填写进出操作间的时间，然后是否提交
'''
class OA_Admin:
    def __init__(self):
        self.headers={
            "Host": "oa.shijinshi.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0",
        }
        self.login_data = {
            "username": "opadmin",
            "password": "xxxxxx"
        }
        self.login_url = 'http://oa.shijinshi.cn/sjsinfo/main/login'
        self.s = requests.Session()
        self.response = self.s.post(self.login_url, data=self.login_data)
        self.begin_url = 'http://oa.shijinshi.cn'
        self.update_date={
            "id":"",
            "multiActs[0].taskId":"",
            "multiActs[0].taskName":"操作间管理员登记",
            "multiActs[0].taskDefKey":"caozuojian_manage",
            "multiActs[0].procInsId":"",
            "multiActs[0].procDefId":"",
            "multiActs[0].flag":"yes",
            "realInDate":"",
            "realOutDate":"",
        }

        self.liuzhuan_url = 'http://oa.shijinshi.cn/sjsinfo/main/act/task/histoicFlow?'
        self.tijiao_url='http://oa.shijinshi.cn/sjsinfo/main/oa/operationAccess/update'
        self.num=0
    #抓去我的任务里面所有任务的连接,返回所有工单的练级
    def handle_allworks(self):
        url = 'http://oa.shijinshi.cn/sjsinfo/main/act/task/todo/?pageNo=1&pageSize=300'
        allworks_response = self.s.get(url)
        allworks_pattern = re.compile('tr.*?td.*?a.*?href="(.*?)">(.*?)</a>', re.S)
        allworks_items = re.findall(allworks_pattern, allworks_response.content)
        allworks_url=[]
        for allworks_item in allworks_items:
            # 访问工单详细页面
            temp = self.begin_url + allworks_item[0]
            allworks_url.append(temp)
            self.num=self.num+1
        return allworks_url
    #进入单个任务界面，抓去data,并且提交
    def work(self):
        allworks_url=self.handle_allworks()
        for url in allworks_url:
            print '当前工单的地址：'+url
            work_response=self.s.get(url)
            ##获取每个表单信息的正则表达式
            urlpattern = re.compile(
                'id="inputForm".*?value="(.*?)".*?value="(.*?)".*?value="(.*?)".*?value="(.*?)".*?value="(.*?)".*?value="(.*?)"',
                re.S)
            form_items = re.findall(urlpattern, work_response.content)
            self.update_date['id'] =form_items[0][0]
            self.update_date['multiActs[0].taskId']=form_items[0][1]
            #self.update_date['multiActs[0].taskName']=form_items[0][2]
            self.update_date['multiActs[0].taskDefKey']=form_items[0][3]
            self.update_date['multiActs[0].procInsId']=form_items[0][4]
            self.update_date['multiActs[0].procDefId']=form_items[0][5]

            ##获取当前任务的流转url，并且访问
            liuzhuan_url_pattern = re.compile('/fieldset.*?get\("(.*?)&startAct',re.S)
            liuzhuan_url_items = re.findall(liuzhuan_url_pattern, work_response.content)
            for  liuzhuan_url_item in  liuzhuan_url_items:
                #打印流转页面
                print '打印流转页面：'+self.begin_url+liuzhuan_url_item
                liuzhuan_response=self.s.get(self.begin_url+liuzhuan_url_item)
                # print liuzhuan_response.content
                # print liuzhuan_response.request.headers
                # exit(9)
            ##确定这个任务是否与工单相关联
            urlpattern = re.compile('工单编号：(.*?)）', re.S)
            gdhao_items = re.findall(urlpattern, work_response.content)
            n=0
            for gdhao_item in gdhao_items:
                if gdhao_item:
                    print '跟工单相关联,工单号为：', gdhao_item
                    liuzhuan_pattern= re.compile('技术开发组评审.*?<td>.*?<td>.*?<td>(.*?)</td>',re.S)
                else:
                    print '没有跟工单号相关联'
                    liuzhuan_pattern = re.compile('IT部负责人审批.*?<td>.*?<td>.*?<td>(.*?)</td>', re.S)
                    n=n+1
                liuzhuan_items = re.findall(liuzhuan_pattern, liuzhuan_response.content)
                print '最后时间：',
                print liuzhuan_items
            self.update_date['realInDate']=raw_input('第一次时间：')
            self.update_date['realOutDate'] = raw_input('第二次时间：')
            print '第一次时间：'+ self.update_date['realInDate']
            print '第二次时间：'+self.update_date['realOutDate']
            #验证提交信息
            # print self.update_date
            conti=raw_input('\n是否提交？输入任意数字表示退出，直接回车表示提交：')
            if not conti:
                print '为空，将会提交。'
            else:
                print '程序退出'
                exit(9)
            tijiao_response = self.s.post(self.tijiao_url,data=self.update_date)
            print tijiao_response.status_code
            self.num=self.num-1
            #print tijiao_response.content
            print
            print '--------下一个--------'+'还有'+str(self.num)+'-----------'

admin=OA_Admin()
admin.work()
