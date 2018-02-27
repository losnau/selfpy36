# -*- coding:utf-8
'''
填写年月，用户名和密码，自动签到一个月
'''
import calendar,datetime,time
import requests

requests.packages.urllib3.disable_warnings()
class OA():
    def __init__(self):
        #用户名和密码
        self.login_data = {
            "username": "xxxxx",
            "password": "xxxxx"
        }
        self.login_url = 'https://oa.shijinshi.cn/sjsinfo/main/login'
        self.gs_url = 'https://oa.shijinshi.cn/sjsinfo/main/oa/timeSheet/insertTimeSheet'
        self.gs_data = {
            "workType": "63",
            "name": "系统运维",
            "type.id": "63",
            "workTime": "",
            "project.id": "",
            "duration": "7",
            "remarks": "运维",
            "overTime": "0"
        }
        self.s = requests.Session()
        login_url = 'https://oa.shijinshi.cn/sjsinfo/main/login'
        r=self.s.post(self.login_url, data=self.login_data, verify=False)
        #print(r.status_code) 

    def getstmap(self,year, month):
        li = [0, 1, 2, 3, 4]
        tm10=[1506873600000,1506960000000,1507046400000,1507132800000,1507219200000,1507478400000,1507564800000,1507651200000]
        hms = ' 00:00:00'
        # 返回两个参数，第一个参数是这个月第一天是星期几，第二个参数是这个月有多少天
        key, days = calendar.monthrange(year, month)
        for day in range(days):
            # 传入某年某月某日,返回时星期几,返回值有0，1，2，3，4，5，6
            s = datetime.datetime(year, month, day + 1).weekday()
            if s in li:
                sj = str(year) + '-' + str(month) + '-' + str(day + 1) + hms
                #print(sj)
                # 转换成时间数组
                timeArray = time.strptime(sj, "%Y-%m-%d %H:%M:%S")
                # 将时间数组转换成时间戳
                timestamp = time.mktime(timeArray)
                self.gs_data['workTime']= long(timestamp * 1000)
                if self.gs_data['workTime'] in tm10:
                    continue
                print(sj+'------',) 
                print(self.gs_data['workTime']) 
                #self.gs_data['workTime'] = 1506614400000
                response2 = self.s.post(self.gs_url, data=self.gs_data, verify=False)

                #exit(0)
                print(response2.status_code) 
                # print(response2.content) 
                # print("%Ld" % (timestamp * 1000)) 
oa=OA()
oa.getstmap(2018,01)
