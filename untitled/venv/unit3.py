##if…else
num1 =2004 ##int(input('please input a year number:'))
if num1%100 == 0:
    if num1%400==0:
        print('run')
    else:
        print('none')
else:
    if num1%4 == 0 :
        print('run')
    else:
        print('none')
##while
num1 = 0
while num1<10:
    print(num1)
    num1+=1
##for
for i in range(0,6,3):
     print(i)

##continue
i=0
while i<5:
    i+=1
    if i ==3:
        print('i=',i)
    elif i==4:
        print('i=',i)
    else:
        continue
        print('wrong')
print('OVER')

##9*9
##two ways
for i in range(1,10):
    for j in range(1,1+i):
        print('{}*{}={}'.format(j, i, i * j), end=' ')
    print('')

i=9
while i>0:
    j = 1
    while j<i+1:
        print('{}*{}={}'.format(j,i,i*j), end=' ')
        j += 1
    print('\n')
    i-=1

##等腰三角形
for i in range(1,6):
    j=5-i
    print(' '*j,end='')
    for k in range(1,2*i):
        print('*',end='')
    print('\n')
