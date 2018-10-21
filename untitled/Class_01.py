class ClassName:
    name = 'Jack'  # 属性

    def welcome(self):  # 方法
        print(self)  # 实例本身
        print(self.__class__)  # 类本身


w = ClassName()  # 对象 类的实例化
print(w.name)
w.welcome()


class MemberClass:  # 类的构造方法和析构方法 私有属性  __init__ and __del__
    __count = 0
    __name = ''

    def __init__(self, name, count):
        self.__count += count
        self.__name = name

    def seek(self):
        print(self.__name+'积分'+str(self.__count))


w = MemberClass('Jack',400)
w.seek()


class MarketMember:
    __name = ''
    count = 600

    def __init__(self, name):
        self.__name += name
        print('User ' + self.__name + ' count ' + str(self.count))

    def change(self, count1):
        self.count += count1
        print('User '+self.__name+' count '+str(self.count))


m = MarketMember('Jack')
m.change(300)
m.change(200)
print(m.count)


class MyMember(MarketMember):  # 单继承
    age = 0

    def seekAge(self):
        print('age '+str(self.age))


x = MyMember('Jsde')
x.change(200)
x.age = 20
x.seekAge()


class Animals:
    color = ''
    weight = 0

    def jump(self):
        print('跳')


class Cats:
    def miao(self):
        print('喵')


class WhiteCat(Animals,Cats):
    def miao(self):
        print('喵喵')
    def catch(self):
        print('I Can')


w = WhiteCat()
w.jump()
w.miao()
w.catch()

class Person:
    def gobyboat(self,boat):
        boat.overriver()

class Boat:
    def overriver(self):
        pass

class employee:
    id=0
    name=''

class company:
    def __init__(self):
        self.employeer=employee()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._registry={
            'name':name,
            'age':age
        }

    def __getitem__(self, key):
         if key not in self._registry.keys():
            raise Exception('faafafaff:%s first' % (key,))
         return self._registry[key]

    def __setitem__(self, key, value):
         if key not in self._registry.keys():
            raise Exception('faafafaff:%s first' % (key,))
         self._registry[key]=value

    def __call__(self, *args):
        return args[0]+args[1]


p = Person('Jack','30')
print(p(70,10))

print(p['age'])
p['age']=40
print(p['age'])

# 迭代器
a = [1,2,3,4,5,6,7,8,9]
it = iter(a)
for i in it:
    print(i)

# 生成器
def count(n):
    x = 0
    while x < n:
        yield x
        x += 1

for i in count(6):
    print(i)

def w(func):
    def inner():
        print('Other')
        return func()
    return inner

@w
def f1():
    print('Self')

f1()
