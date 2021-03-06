
import random
from collections import Counter
class panduan():
    def __init__(self):
        pass
    '''
    保证每一周只有一个人会值班5个班次，其他都是4个班次
    '''
    def gongshi(self,paibans):
        f = 0
        l = 0
        h = 0
        t = 0
        z = 0
        for paiban in paibans:
            if '符昇' in paiban:
                f = f + 1
            if '凌康志' in paiban:
                l = l + 1
            if '胡钊' in paiban:
                h = h + 1
            if '周贤' in paiban:
                z = z + 1
            if '谭宇涛' in paiban:
                t = t + 1
        gongshi = [f, h, l, z, t]
        maxgongshi = max(gongshi)
        gongshi.remove(maxgongshi)
        if gongshi[0] ==  gongshi[1] == gongshi[2] == gongshi[3] == 4:
            return True
        return False

    '''
        保证每一个人每周值凌晨班次数不会超过两次
    '''
    def lingchenban(self, paibans):
        f = 0
        l = 0
        h = 0
        t = 0
        z = 0
        for paiban in paibans:
            if '符昇' == paiban[0]:
                f = f + 1
            if '凌康志' == paiban[0]:
                l = l + 1
            if '胡钊' == paiban[0]:
                h = h + 1
            if '周贤' == paiban[0]:
                z = z + 1
            if '谭宇涛' == paiban[0]:
                t = t + 1
        lingchenban = [f, h, l, z, t]
        if max(lingchenban) >2:
            return False
        return True
    '''
    name是一个列表，排除name里面值班五天的人，即下一周值班五天的人不应该是names列表里面的人
    '''
    def lastweek5day(self,names,paibans):
        paibans_temp=str(paibans).replace('[', '').replace(']', '').replace("'", '').split(',')
        maxname=Counter(paibans_temp).most_common(1)[0][0].strip()
        if maxname in names:
            return False
        return True
    '''
    排除掉一人连续值两次夜班
    '''
    def day2person(self,names,paibans):
        return True
    '''
    排除掉一人连续值三次夜班
    '''
    def night3person(self,names,paibans):
        return True
    '''
    保证每个人值班的间隔为16小时（间隔两个班次）
    '''
    def hour16(self,paibans):
        for i in range(len(paibans)-1):
            '''
            比如说：(1,0) ---->(0,1) (0,2)  (1,1) ------>(0,2)
            '''
            if paibans[i+1][0] == paibans[i][1] or paibans[i+1][0] == paibans[i][2] or paibans[i+1][1] == paibans[i][2]:
                return False
        return True
    '''
    是否在总排班里面
    '''
    def isinsha(self,paibans,sha):
        if paibans not in sha:
            return True
        return False
    '''
    满足所有条件
    '''
    def all_condition(self,paibans,sha):
        if self.gongshi(paibans) and self.hour16(paibans) and self.isinsha(paibans,sha) and self.lingchenban(paibans):
           return True
        return False
        
names=['符XX','凌XX','胡XX','周XX','谭XX']
nums=50
num=0
sha=[]
panduan=panduan()
while True:
    paibans = [['1', '2', '3'], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
    #随机生成一周的排班表
    for i in range(7):
        names_temp = names.copy()
        for j in range(3):
            a = random.sample(names_temp, 1)
            paibans[i][j] = a[0]
            names_temp.remove(a[0])
    if panduan.all_condition(paibans,sha):
        sha.append(paibans)
        num = num + 1
        print('')
        if num == nums:
            print('----------------------一周排班的分隔符---------------------------')
            for paibans in sha:
                for paiban in paibans:
                    print(paiban)
            exit(0)
