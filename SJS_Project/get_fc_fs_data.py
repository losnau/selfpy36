# -*- coding:utf-8
from selenium import webdriver
from time import sleep
import re
from datetime import datetime

FCFS1={
    "C60A":{
		'fc':'https://xxxxx/OmsPortal/login.jsp',
		'fs':'https://xxxxx/fsportal/src/index.html#/login',
    },
    "C60B":{
		'fc':'https://xxxxx/OmsPortal/login.jsp',
		'fs':'https://xxxxx/fsportal/src/index.html#/login'
    },
    "C60B-DMZ":{
		'fc':'https://xxxxx/OmsPortal/login.jsp',
		'fs':'https://xxxxx/fsportal/src/index.html#/login'
    },
	"分析区":{
		'fc':'https://xxxxx/OmsPortal/login.jsp',
		'fs':'https://xxxxx/fsportal/src/index.html#/login'
    }
}
FCFS2={
	"DTSP":{
		'fc':'https://172.16.248.1:8443/OmsPortal/login.jsp',
		'fs':'https://172.16.248.4/fsportal/src/index.html#/login'
    }
}
USERINFO={
		"username":"xxxxx",
		"password":"xxxxx"
	}


def DRIVERS():
    options=webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    driver = webdriver.Chrome(executable_path='C:\\Users\\lizuofang\\Desktop\\fcfsinfo\\chromedriver_win32\\chromedriver.exe',chrome_options=options)
    #driver = webdriver.Chrome(executable_path='C:\\Users\\Administrator\\Desktop\\fcfsinfo\\chromedriver_win32\\chromedriver.exe',chrome_options=options)
    return driver
'''
适用于：
1）、FusionComputeV100R006C10SPC101 高级版
2)、FusionComputeV100R006C10 高级版
'''
def FC_V5(URL,USERINFO):
    driver = DRIVERS()
    driver.get(URL)
    driver.maximize_window()
    sleep(1)
    elem_user = driver.find_element_by_id("userName-inputEl")
    elem_user.send_keys(USERINFO['username'])
    elem_password = driver.find_element_by_id("password-inputEl")
    elem_password.send_keys(USERINFO['password'])
	#登陆按钮
    driver.find_element_by_id("button-1036-btnEl").click()
    sleep(1.5)
	#点击计算池
    driver.find_element_by_xpath("//*[@id='sys-menu']/ul/li[3]").click()	
    sleep(1)
	#点击DTSPFCCluster
    driver.find_element_by_xpath("//table[@class='x-grid-table x-grid-table-resizer']//span[contains(text(), 'DTSPFCCluster')]").click()
	#点击概要
    driver.find_element_by_xpath("//div[@id='portal-task-42A007A1-hostandcluster-hostandclusterview-cluster-tabs']//span[contains(text(), '概要')]").click()
    #采集数据
    page_source = driver.page_source
    patterns = re.compile('占用率.*?<span.*?>(.*?)<.*?false">(.*?)<', re.S)
    items=re.findall(patterns, page_source)
    print(items)
    driver.close()
    return page_source
	
def FC_V6(URL,USERINFO):
    driver = DRIVERS()
    driver.get(URL)
    driver.maximize_window()
    sleep(1)
    elem_user = driver.find_element_by_id("userName-inputEl")
    elem_user.send_keys(USERINFO['username'])
    elem_password = driver.find_element_by_id("password-inputEl")
    elem_password.send_keys(USERINFO['password'])
	#登陆按钮
    driver.find_element_by_id("button-1036-btnEl").click()
    sleep(1.5)
    #点击计算池
    driver.find_element_by_xpath("//*[@id='sys-menu']/ul/li[3]").click()					
    sleep(1)
	#点击ManagementCluster
    driver.find_element_by_xpath("//*[@id='treeview-1129']/table/tbody/tr[3]/td/div/span").click()
	#点击DTSPCCluster  
    #driver.find_element_by_xpath("//*[@id='treeview-1069']/table/tbody/tr[3]/td/div/span").click()
	#//*[@id="treeview-1069"]/table/tbody/tr[3]/td/div/span
	#点击概要
    driver.find_element_by_id("tab-1219-btnEl").click()
	
    #driver.find_element_by_xpath('//div/span[contains(text(), "SJS_Cluster")]').click()
    #driver.find_element_by_xpath('//div[@id="portal-task-402207EB-vmcenter-vmcenterview-hostandcluster-vmcenter-hostandcluster-hostandclusterview-cluster-tabs"]//div[@class="x-box-inner x-horizontal-box-overflow-body"]/div/div[2]/em/button/span[1]').click()
    sleep(1)

    #采集数据
    page_source = driver.page_source
    patterns = re.compile('占用率.*?<span.*?>(.*?)<.*?false">(.*?)<', re.S)
    items=re.findall(patterns, page_source)
    print(items)
    driver.close()
    return page_source
'''
适用版本：
1)、FusionStorage Block V100R006C00SPC103
2）、FusionStorage Block V100R003C30U2SPC003
3)、FusionStorage V100R003C30SPC200	
'''
def FS_V5_V6(URL,USERINFO):
    driver = DRIVERS()
    driver.get(URL)
    driver.maximize_window()
    sleep(1)
    elem_user = driver.find_element_by_id("loginNameId")
    elem_user.send_keys(USERINFO['username'])
    elem_passwd = driver.find_element_by_id("loginPassWordId")
    elem_passwd.send_keys(USERINFO['password'])
    driver.find_element_by_id("loginId").click()
    sleep(5)
    page_source = driver.page_source
    
    #采集数据
    patterns = re.compile('dy="16".*?>(.*?)<.*?总容量.*?ng-scope">(.*?)<.*?已分配.*?ng-scope">(.*?)<.*?已使用.*?ng-scope">(.*?)<', re.S)
    items=re.findall(patterns, page_source)
    print(items)
    driver.close()
    return page_source
def main_v6(FCFS,USERINFO):
    for key in FCFS:
        print('当前集群:'+key)
        print('采集'+key+'集群FC信息,URL:'+FCFS[key]['fc'])
        FC_V6(FCFS[key]['fc'],USERINFO)
        print('采集'+key+'集群FS信息,URL'+FCFS[key]['fs'])
        FS_V5_V6(FCFS[key]['fs'],USERINFO)
def main_v5(FCFS,USERINFO):
    for key in FCFS:
        print('当前集群:'+key)
        print('采集'+key+'集群FC信息,URL:'+FCFS[key]['fc'])
        FC_V5(FCFS[key]['fc'],USERINFO)
        print('采集'+key+'集群FS信息,URL'+FCFS[key]['fs'])
        FS_V5_V6(FCFS[key]['fs'],USERINFO)

dt_start=datetime.now()
main_v6(FCFS1,USERINFO) 
main_v5(FCFS2,USERINFO) 
dt_end=datetime.now()
print('程序开始时间：',end='')
print(dt_start.strftime("%Y-%m-%d %H:%M:%S"))
print('程序结束时间：',end='')
print(dt_end.strftime("%Y-%m-%d %H:%M:%S"))
