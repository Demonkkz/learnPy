# 参数
# 全局变量和局部变量


def te():
    global x
    x = 1
    print(x)


te()
print(x)

# 匿名函数
sum1 = (lambda x,y:x+y)(2,3)
print(sum1)
