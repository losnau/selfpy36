## 综合一个例子
```python
import datetime
#TIME='Dec 22, 2017 11:05:38 AM'
TIME='Feb 8, 2018 9:53:30 PM'
GMT_FORMAT = '%b %d, %Y %H:%M:%S %p'
dt=datetime.datetime.strptime(TIME, GMT_FORMAT)
dt=dt+datetime.timedelta(minutes=10)#增加10分钟 
print(dt)

import datetime
datetime.datetime.strptime('20180315',  '%Y%H%M').strftime( '%Y-%H-%M')
#输出：'2018-03-15'
```
## 日期格式转换
> 参考：http://ju.outofmemory.cn/entry/1078

```python
import datetime
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
# 生成datetime对象的过程和我可能不同，这里是拿当前时间来生成
TIME = 'Thu, 19 Feb 2009 16:00:07 GMT'
datetime.datetime.strptime(TIME, GMT_FORMAT)
```
##### 日期格式

参数 | 中文释义
---|---
%a  |  本地的星期缩写
%A  |  本地的星期全称
%b  |  本地的月份缩写
%B  |  本地的月份全称
%c  |  本地的合适的日期和时间表示形式
%d  |  月份中的第几天，类型为decimal
%f  |  微秒，类型为decimal
%H  |  小时（24进制），类型为decimal
%I  |  小时（12进制），类型为decimal
%j  |  一年中的第几天，类型为decimal
%m  |  月份，类型为decimal
%M  |  分钟，类型为decimal
%p  |  本地的上午或下午的表示（AM或PM），只当设置为%I（12进制）时才有效
%S  |  秒钟，类型为decimal
%U  |  一年中的第几周（以星期日为一周的开始），类型为decimal
%w  |  星期，类型为decimal
%W  |  一年中的第几周（以星期一为一周的开始），类型为decimal
%x  |  本地的合适的日期表示形式
%X  |  本地的合适的时间表示形式
%y  |  去掉世纪的年份数，类型为decimal
%Y  |  带有世纪的年份数，类型为decimal
%Z  |  时区名字（不存在时区时为空）
%%  |  代表转义的"%"字符

## 时间的加n和减n运算
> 参考：https://www.linuxidc.com/Linux/2013-10/91383.htm

```python
import datetime
>>> d1 = datetime.datetime.now()
>>> d1.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:11:07'
>>> d2 = d1 + datetime.timedelta(seconds=10) #增加10秒
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:11:17'
>>> d2 = d1 + datetime.timedelta(minutes=10) #增加10分钟
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:21:07'
>>> d2 = d1 + datetime.timedelta(hours=10) #增加10小时
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-03 03:11:07'
>>> d2 = d1 + datetime.timedelta(days=10) #增加10天
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-12 17:11:07'
>>> d2 = d1 - datetime.timedelta(seconds=10) #减去10秒
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:11:57'
>>> d2 = d1 - datetime.timedelta(minutes=10) #增加10分钟
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:01:07'
>>> d2 = d1 - datetime.timedelta(hours=10) #减去10小时
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 07:11:07'
>>> d2 = d1 - datetime.timedelta(days=10) #减去10天
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-08-23 17:11:07'
```
