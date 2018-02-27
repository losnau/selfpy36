#-*- coding:utf-8
from bs4 import  BeautifulSoup
fp=open('content.text','r')
content=fp.read()
soup=BeautifulSoup(content,'html.parser',from_encoding='utf-8')

div=soup.find_all('div',class_='pagination')
'''
contents返回值为一个list
以下for循环是遍历div中子节点
'''
print '-------------------contents-------------------------'
print type(div[0].contents)
for content in div[0].contents:
    print content['href']
'''
children返回值为一个list生成器对象
以下for循环是遍历div中子节点
'''
print '-------------------children-------------------------'
print type(div[0].children)
for content in div[0].children:
    print content['href']
'''
descendants遍历所有子孙节点
'''
print type(div[0].descendants)
for child in div[0].descendants:
    print child
'''
遍历class=pagination的div下面的标签下面的a标签
'''
# for content in div[0].find_all('a'):
#     print content['href']

for row in div:
    for col in row.find_all('a'):
        print col['href']
'''
先在整个文档中遍历class=pagination的div标签
将 menu转换为str类型之后，
在遍历div中的a标签
'''
values = ','.join(str(v) for v in div)
soup2=BeautifulSoup(values,'html.parser')
for i in soup2.find_all('a'):
    print i['href']
fp.close()
print type(div[0].contents)
print div[0].contents[-1]
print div[0].contents[-1]['href']
print div[0].contents[-1]['href'].split('/')
print type(div[0].contents[-1]['href'].split('/')[-1])
print int(div[0].contents[-1]['href'].split('/')[-1])
