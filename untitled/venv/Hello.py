print('hello')
num1 = float(15)
print(num1)
com1 = 15.j
print(complex(1))
str1 = 'Hello World!'
print(str1)
print(str1[-6:8])
strq = ('A','Y','Y')
sy = 'w'
AA = sy.join(strq)
print(AA)
print(r'射飞镖\a十多岁哦')
print('{}的{}'.format('d',8))
stu1=['10001','小陈','男',20]

print(stu1[1][0])

stu1.append('上海')
print(stu1)
stu1.insert(2,'上海')
print(stu1)
stu1.pop()
print(stu1)
stu1.reverse()
print(stu1)

sor1=[45,76,23,54,99]
sor2=sor1[:]
print(id(sor1))
sor2.sort()
print(sor2)
print(id(sor2))
sor1.sort(reverse=True)
print(sor1)
print(id(sor1))
print(sor1[:-2])
print(sor1[1:5]) ##步长 默认是1

sf=('asfsdvfrrreijwndfewfe')
print(sf[:-8])
print(max(sor1))

dct1={1:'Hello','我':'Zhujunjie','d':20}
print(dct1.keys())
print(dct1.values())
print(dct1.items())
print(dct1.get(1))

crs=(1,2,3,4)
dct2 = dict.fromkeys(crs)
print(dct2.items())
print(dct1.setdefault('ddss',22))

set1 = set([1,2,3,4,5])
set2 = set([5,6,7,8,9])
print(set1.difference(set2))

T = [i for i in range(40) if i%5 is 0]
print(T)
