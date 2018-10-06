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
num1=0
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

for i in range(1,10):
    for j in range(1,1+i):
       num=str(i)+'*'+str(j)+'='+str(i*j)
       print(num,end=' ')
    print('\n')
