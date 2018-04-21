# -*- coding:utf-8
import socket
import sys
#
HOST='127.0.0.1'
PORT='5001'
HOST_PORT=(HOST,PORT)
BUFSIZE=1024
#创建socket对象
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
user = str(sys.argv[1])     #zabbix传过来的第一个参数
subject = str(sys.argv[2])  #zabbix传过来的第二个参数
content = str(sys.argv[3])  #zabbix传过来的第三个参数
msg=user+'===***==='+subject+'===***==='+content
#连接socket
s.connect_ex(HOST_PORT)  
#发送消息
s.send(msg.encode('utf-8'))         
s.close()  
