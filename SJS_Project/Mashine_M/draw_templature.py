#-*- coding:utf-8
import  csv
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei'];
mpl.rcParams['axes.unicode_minus'] = False
y1=[]
y2=[]
x1=[]
temp=0
with open("temprature.csv", "rt", encoding="gbk") as vsvfile:
    reader = csv.reader(vsvfile)
    #reader=pd.read_csv("temprature.csv", header=False)
    print(type(reader))
    for row in reader:
        if temp==100:
            continue
        else:
            y1.append(row[3])
            y2.append(row[4])
            x1.append(row[0].replace('2018/','')+' '+row[1])
            temp = temp + 1
del y1[0]
del y2[0]
del x1[0]
print(y1)
print(y2)
print(x1)
x=range(len(x1))
plt.figure(figsize=(20,15)) #创建绘图对象
plt.subplot(211)    #这个必须放在plt.plo前面
plt.plot(x, y1, 'ro--',label="送风温度", color="green", linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.xticks(x,x1,rotation = 90)
plt.xlabel(u"日期时间") #X轴标签
plt.ylabel(u"送风温度")  #Y轴标签
plt.title(u"送风温度图") #图标题


plt.subplot(212)
plt.plot(x,y2,"ro--",label="回风温度", color="green",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.xticks(x,x1,rotation = 45)
plt.xlabel("日期时间") #X轴标签
plt.ylabel("回风温度")  #Y轴标签
plt.title("回风温度图") #图标题

plt.grid()
plt.show()
