# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
'''
也可以不创建绘图对象直接调用接下来的plot函数直接绘图，matplotlib会为我们自动创建一个绘图对象。
如果需要同时绘制多幅图表的话，可以是给figure传递一个整数参数指定图标的序号，
如果所指定序号的绘图对象已经存在的话，将不创建新的对象，而只是让它成为当前绘图对象。

figsize参数可以指定绘图对象的宽度和高度，
单位为英寸；dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80。因此本例中所创建的图表窗口的宽度为10*80 = 800像素。
'''

plt.figure(figsize=(10,4))

mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号

mpl.rc('xtick', labelsize=10)   #设置X坐标轴刻度显示大小
mpl.rc('ytick', labelsize=10)   #设置Y坐标轴刻度显示大小

plt.xlabel("日期")  # X轴标签
plt.ylabel("数字")  # Y轴标签
plt.title("自定义X轴图片")  # 标题

x=[1,2,3,4,5]           #定义X轴刻度
y=[0,2,5,16,25]         #定义Y轴刻度
plt.ylim(-30,30)        #限定X轴范围
plt.xlim(-1,8)        #限定X轴范围

#ax is the axes instance
group_labels=['2017-11-10','2017-11-11','2017-11-12','2017-11-13','2017-11-14']
#'r--'：表示红色虚线
plt.plot(x,y,"r--",label="test",linewidth=2)
#使用了"plt.xticks"方法设置x轴文本，标签文本使用group_labels中的内容，因此可以根据需要修改group_labels中的内容。
plt.xticks(x,group_labels,rotation=0)

plt.grid()      #开启网格
plt.show()      #显示图片

#保存图象
#plt.savefig("easyplot.png")
