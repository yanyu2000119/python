#计算x^2
#def pwoer1(x):
#    return x * x

#a = pwoer1(4)
#print(a)

#计算x^n次方
# def power1(x, n):
#     b = 1
#     while n > 0:
#         n = n - 1
#         b = b * x
#     return b
#
# c = power1(5,1)
# print(c)

#默认函数和位置函数的应用
# def enroll(name, age, city="重庆", phone="130"):
#     print("name:",name)
#     print("age:",age)
#     print(city)
#     print(phone)
#
# enroll("lifufei", "13", city="s",phone="1")

#可变参数的应用
# def power(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#
#     return sum
#
# c = power([1,2,3])
# print(c)
#
# ----------------------
# def power(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#
#     return sum
#
# c = power(1,2,3)
# print(c)



#
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person(20,10,)
