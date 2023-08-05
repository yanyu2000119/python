班级名字=['小明','小红','小白','小丽','小黑',['小粉','小鬼']]

#打印名字'小鬼'

print(班级名字[5][1])

print(班级名字[-1][-1])

#集合最后加入名字'小刚'

班级名字.append('小刚')

#在集合内的集合里的，第一位置加入名字'白白'

班级名字[5].insert(0,'白白')

 #删除名字'小黑'

班级名字.pop(4)

#把名字'小鬼'，替换为'大鬼'

班级名字[4][2]='大鬼'

#练习2、

二班名单=('莉莉','晴晴','圆圆',['小明','小红',['小粉','小鬼'],'壮壮'])

#名字'小红'更改为'红红'。

二班名单[3][1]='红红'

#删除名字'小鬼'；

二班名单[3][2].pop(1)

#报错 AttributeError: 'tuple' object has no attribute 'pop'

#那么我们试试换一种思路,把名字‘小黑’用*替代，借此来达到删除目的。

#二班名单[3][2][1]='*'
print(二班名单)




height = 1.75
weight = 80.5

bmi = weight / (height * height)

if bmi > 18.5:
    print(f'过轻，bmi为：{bmi}')
elif 18.5 <= bmi < 25:
    print(f'正常，bmi为:{bmi}')
elif 25 <= bmi < 28:
    print(f'过重，bmi为:{bmi}')
elif 28 <= bmi < 32:
    print(f'肥胖,bmi为：{bmi}')
else:
    print(f'严重肥胖，bmi为：{bmi}')

#while计算100以内的奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#循环打印1-100对数字
#m = 0
#while m < 100:
#    m = m + 1
#    print(m)

#print('END')

#利用break提前结束循环
#m = 0
#while m < 100:
#    if m > 10:
#        break
#    print(m)
#    m = m + 1
#
#print('END')

#continue语句跳过循环打印1-10的奇数
#n = 0
#while n < 10:
#    n = n + 1
#    if n % 2 == 0:
#        continue
#    print(n)

#死循环
#n = 10
#while n < 1000:
#    print(n)
