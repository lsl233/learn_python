# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-03-28 21:13:53
# @Last Modified by:   Administrator
# @Last Modified time: 2016-04-02 15:00:15

# for...in 循环
# L = ['Bart', 'Lisa', 'Adam']
# for a in L:
# 	print('hello,', a)

# range()函数 生成一个整数序列-从0开始-
# sum = 0
# for x in range(5, 101):
# 	sum = sum + x
# 	print(sum)

# while 循环
# sum = 0
# n = 99
# while n > 0:
# 	sum = sum + n
# 	n = n - 2
# print(sum)


# 函数
# from abstest import  倒入文件
# more  查看文件
# pass 占位符，定义空
#
# def my_abs(x):
# 	if not isinstance(x, (int, float)): # isinstance检查数据类型
# 		raise TypeError('bad operand type')
# 	if x >= 0:
# 		return x
# 	else:
# 		return -x

# import math
#
# def move(x, y, step, angle = 0):
#   nx = x + step * math.cos(angle)
#   ny = y - step * math.sin(angle)
#   return nx, ny
# print (move(1, 2, 3))

# 一是必选参数在前，默认参数在后
# def power(x, n = 2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5))

# 递归函数
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
# print(fact(100))

# L = []
# n = 1
# while n <= 99:
#     L.append(n)
#     n += 1
# print(L)

# import os
# print(os.listdir())

# 迭代对象
# d = {'a': '1', 'b': '2', 'c': '3'}
# for k, v in d.items():
#     print(k, v)

# 列表生成式
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [a for a in L1 if isinstance(a, str)]
# print(L2)

# 生成器
# g = (x * x for x in range(1, 11))
# for a in g:
#     print(a)

# 斐波拉契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield (b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# f = fib(6)
# while True:
#     try:
#         x = next(f)
#         print('x', x)
#     except StopIteration as e:
#         print('错误--', e.value)
#         break

# 高阶函数 Higher-order function
# def add (a, b, fun):
#     return fun(a) + fun(b)
# result = add (-2, -3, abs)
# print(result)

# map
# def f(x):
#     return x * x
#
# r = map(f, range(1, 10))
# print(list(r))

# 首字母大写 capitalize
# def normal(name):
#     return name.capitalize()
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normal, L1))
# print(L2)

# 乘法运算
# from functools import reduce
# def products(x, y):
#     return x * y
#
# def prod(list):
#     return reduce(products, list)
#
# print('3 * 4 * 5 =', prod([3, 4, 5])

# 字符串转浮点数
# from functools import reduce
# def str2float(s):
#     return float(s)
# print(isinstance(str2float('123.456'), str))
#
# print(isinstance('123.456', str))

# filter 过滤
# def is_add(n):
#     return n % 2 == 1
# print(list(filter(is_add, range(1, 11))))

# 装饰器
# def log (func):
#     def wrapper(*grgs, **kw):
#         print('call %s():' % func.__name__)
#         return func(*grgs, **kw)
#     return wrapper
#
# def now():
#     print('2015-3-25')
#
# log(now)
# def log(fn):
#     def wrapper(*grgs, **kw):
#         print('start...')
#         fn(*grgs, **kw)
#         print('...end')
#     return wrapper
# @log
# def dfn(name):
#     print('name:', name)
#
# dfn('123')

# 类 访问限制
# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#
#     def get_grade(self):
#         if self.__score >= 90:
#             return 'A'
#         elif self.__score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
# bart = Student('lsl', 100)
# bart.name = 'ssss'
# print(bart.__name)

# class Animal(object):
#     def run(self):
#         print('Animal is runing...')
#
# class Dog(Animal):
#     pass
#
# d = Dog()
# print(len('aaa'))
# print('ABDASDFD'.lower())
# print(hasattr(Animal, 'runs', 404))

# import datetime
# now = datetime.now()
# print(datetime.datetime.now())

# file = open('C:/Users/Administrator/Desktop/aaa.text', 'w')
# file.write('aaaaaaaaaaaaaaaaaaaaaaaa')

# print('  *', ' ***', '*****', '  |  ', sep = "\n")

# def foo (num):
#     n = num + num
#     assert n != 0, 'aaaaaaaaaaaaa'
#     return n
# foo(0)

# file = open('C:/Users/Administrator/Desktop/aaa.text', 'r')
# file.read()
# file.close()、

import os
# os.uname()
print(os.path.abspath('.'))
os.path.join('H:\learn\python', 'bbb')
os.mkdir('H:\learn\python')