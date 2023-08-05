#调用函数的练习
# n1 = 255
# n2 = 1000
# n3 = hex(n1)
# n4 = hex(n2)
# print(f'{n1}的十六进制为:{n3}', f'{n2}的十六进制为:{n4}')

#调用函数的升级练习
# m = int(input('请输入你的数字：'))
# a = hex(m)
# print(f'你输入的数字的十六进制是：{a}')


# 定义函数的例子
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print(my_abs(-99))


# 定义函数的练习
# import math
# def my_quadratic(a,b,c):
#     if not isinstance(a,(int,float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
#         raise TypeError('bad operand type')
#     if b*b - 4*a*c < 0:
#         return '无解'
#     elif b*b - 4*a*c == 0:
#         x1 = x2 = b*b - 4*a*c
#     else:
#         # x1 = ((-1)*b + math.sqrt(b*b-4*a*c)) / (2*a)
#         # x2 = ((-1)*b + math.sqrt(b*b-4*a*c)) / (2*a)
#         x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
#         x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
#         return x1, x2
#
# r = my_quadratic(int(input('请输入a的值：')), int(input('请输入b的值：')), int(input('请输入c的值：')))
# print(r)


# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person(20,10,)
# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
# enroll('Bob', 'M', 4, 'Taiwd')

