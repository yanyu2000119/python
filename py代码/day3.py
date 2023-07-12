# def power(x):
#     return x * x
#
# e = power(5)
# print(e)

def power2(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

a = power2(2,6)
print(a)