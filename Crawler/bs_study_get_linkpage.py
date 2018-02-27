#-*- coding:utf-8
from bs4 import  BeautifulSoup
import bs4
soup=BeautifulSoup(open('content.text'),'html.parser')
titles=soup.find_all('div',class_='title')
for title in titles:

    print title.a['href'],'-------',
    if type(title.a.string) == bs4.element.Comment:
        print title.a.string
    else:
        for name in title.stripped_strings:
            print name.strip()
#print type(soup)
#right_info
