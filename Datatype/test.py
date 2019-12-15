# list 创建一个有序列表 元素可以按照索引取值
# 创建列表
import timeit

words = ['face']
print(words)
# list中新增元素
words.append('eys')  # 调用方法 新增元素
print(words)
words.extend('noses') # 拆分
print(words)
del words[3]
print(words)
words[0] = 'ear'
print(words)
words[2:4] = [2, 1]
print(words)
print(len(words))


tuple = (1, 2, 3, 4, 5)
print(tuple[2:3])

count = 0
while count < 5:
    count += 1
    print(count)


year = 2019
if year % 4 == 0 and year % 100 != 0 or year %400 == 0:
    print(year, "闰年")
else:
    print(year, '不是闰年')

n = 1
while n<6:
    c = 1
    while c <= n:
        print(n,end='\t')
        c += 1
    n += 1
    print()

# 正数负数
nums = [-1, -2, 3, 4, -5, -6, 5, 6, -9]
count = 0
s = 0
cs = 0
for i in nums:
    if i<0 :
        count += 1
    elif i>=0 :
        s += i
        cs += 1
print('负数个数为', count)
if cs == 0:
    print('没有正数')
else:
    print('正数和为', s)


# 判定质数
import math
num = 1974
n = 2

flag = True

while n <= math.sqrt(num):
    if num % n == 0:
        print(n)
        flag = False
        break
    n += 1

if flag:
    print(num, 'yes')
else:
    print(num, 'no')

# 判断2的n次幂
n = 2
while True:
    if n % 2 == 0:
        n /= 2
        if n == 1:
            print('yes')
            break
    else:
        print('no')
        break

n = 10
if n & (n-1) == 0:
    print('yes')
else:
    print('no')


class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def rename(self,new_name):
        self._name = new_name


p = Person('wong',12)
p.rename('wa')
print(p.get_name())

### pass 代表什么都不做 只是占位


class Student(Person):
    def set_score(self, score):
        self.set_score = score

    def get_score(self):
        return self.set_score


s = Student('liu',24)
a = s.get_name()
print(a)
s.set_score(100)
a = s.get_score()
print(a)


# 如何操作mysql 关系型数据库

import json

data_1 = '{"a":1,"b":2}'
j_data = json.loads(data_1)
print(type(j_data))
#
# import MySQLdb
#
# DATABASE = {
#     'host': 'localhost',
#     'database': 'Examination',
#     'user': 'root',
#     'password': '123456',
#     'charset': 'utf8mb4'
# }
# db = MySQLdb.connect(**DATABASE)
#
# curosr = db.cursor()
# sql = "select * from class"
# curosr.execute(sql)
# results = curosr.fetchall()
# for result in results:
#     print(result)
# sql = "insert into class(id,name)values(5,'Grand four');"
# curosr = db.cursor()
# curosr.execute(sql)
# db.commit()

s = 'asdfghjk'
print(s[:-2])


import numpy as np

a_list = list(range(10))
b = np.array(a_list)  # 原有列表转换数组
a = np.zeros(10)
print(type(a))

a = np.zeros((4,4), dtype=int)
print(a.dtype)
print(a)

b = np.array(list(range(10)))
print(b)
print(a+10)

print(np.sum(b))

n = np.random.rand(100)

a = np.full((2,10),1)

a = a.reshape(4,5)
print(a)

a = [
    [1,2,3],
    [33,4,2],
    [6.36,78]
]

np.sort(a)
print(a.sort())
