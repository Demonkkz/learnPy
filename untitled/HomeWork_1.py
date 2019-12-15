# Q1
a = 0
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        a += i
print(a)

# Q2
nums = [1, 6, 6, 3, 6, 2, 10, 2, 100]
nums = sorted(set(nums))
nums.remove(6)
print(nums)


x = 20
print('致青春：'.ljust(x))
print('人生苦短，我用Python！'.center(x))
print('奋斗的自己'.rjust(x))

a = 2
s = 1
for i in range(0, 6):
    if i == 0:
        print(s, end=' ')
    elif i == 5:
        print(s)
    else:
        s = s * a
        print(s, end=' ')

a = '123$'
if a[-1] == '$':
    b = float(a[0:-1])
    print('{:.2f}￥'.format(b*6.78))
elif a[-3] == 'USD':
    c = float(a[0:-3])
    print('{:.2f}RMB'.format(c*6.78))
elif a[-1] == '￥':
    b = float(a[0:-1])
    print('{:.2f}$'.format(b/6.78))
elif a[-3] == 'RMB':
    c = float(a[0:-3])
    print('{:.2f}USD'.format(c/6.78))

s = []
for i in range(100, 1000):
    i = int(i)
    a = i // 100
    b = i % 100 // 10
    c = i % 100 % 10
    if i == a*a*a + b*b*b + c*c*c:
        s.append(str(i))
print(", ".join(s))

a = b = 1
for n in range(0,11):
    a = pow(1+n/1000,365)
    for i in range(0,365):
        b = b * (1 + n/1000)
    q = a/b
    if n == 10:
        print('N=1%, UP={:.2f}, DW={:.2f}, UP/DW={:.2f}'.format(a,b,q))
    else:
        print('N={}‰, UP={:.2f}, DW={:.2f}, UP/DW={:.2f}'.format(n,a,b,q))

n = str(19)
s = x = 0
while(1):
    for i in n[:]:
        i = int(i)
        a = i*i
        s += a
    if s == 1:
        print('True')
        break
    elif s == 4:
        print('False')
        break
    n = str(s)
    s = 0

n = 100
a = 9


N = 1
k = []
for i in range(1,n+1):
    N = N*i
for j in range(1,1000):
    y = a**j
    z = y*a
    if N%y == 0 and N%z != 0:
        k.append(j)
print(max(k))

m = 5
n = 8
d = 2147483647
while (m & d) != (n & d):
    d <<= 1
print(m&d)


c = '%python%IS*(GOOD)'
for i in c[:]:
    if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
        if 96 < ord(i) < 120 or 64 < ord(i) < 88:
            s = ord(i) + 3
        else:
            s = ord(i) - 23
        s = chr(s)
        print(s, end='')
    else:
        print(i, end='')

s = []
for i in range(100, 1000):
    i = int(i)
    a = i // 100
    b = i % 100 // 10
    c = i % 100 % 10
    if i == a*a*a + b*b*b + c*c*c:
        s.append(str(i))
print(",".join(s))

n = int(3)
for i in range(1,(n+1)//2+1):
    j=(n+1)//2-i
    print(' '*j,end='')
    for k in range(1,2*i):
        print('*',end='')
    print(' '*j)

c = '2018-Python123-Well-Done‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬'
for i in c[:]:
    if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
        if 96 < ord(i) < 123:
            s = 219 - ord(i)
        elif 64 < ord(i) < 91:
            s = 155 - ord(i)
        s = chr(s)
        print(s, end='')
    else:
        print(i, end='')


c = '罗马数字转换成'
for i in c[:]:
    print(i)

a = 'MCM'
s = 0

F = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

for i in range(len(a)-1):
    if F[a[i]] < F[a[i+1]]:
        s -= F[a[i]]
    else:
        s += F[a[i]]
s += F[a[-1]]
print(s)


c = '1423'
x = a = 0
if c[0] == '-':
    d = c[1:]
    for i in d[:]:
        i = int(i)
        s = pow(10, a)
        a += 1
        x += s * i
    print(-x)
else:
    for i in c[:]:
        i = int(i)
        s = pow(10, a)
        a += 1
        x += s * i
    print(x)


c = 'python'
c = list(c)
x = -1
for i in c[:]:
    x += 1
    if i == 'p':
        c[x] = 'P'
c = ''.join(c)
print(c)

c = 4500

x = c - 3500
if x < 0:
    print('0')
elif 0 <= x <= 1500:
    print(int(x*0.03))
elif 1500 < x <= 4500:
    print(int(x*0.1))
elif 4500 < x <= 9000:
    print(int(x*0.2))
elif 9000 < x <= 35000:
    print(int(x*0.25))
elif 35000 < x <= 55000:
    print(int(x*0.3))
elif 55000 < x <= 80000:
    print(int(x*0.35))
else:
    print(int(x*0.45))


n = 35
a = 95

y = (a-2*n)/2
x = n - y
s = str(y)
if s[-2:] == '.5' or y < 0:
    print('Data Error!‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬')
else:
    print("{:.0f} {:.0f}".format(x, y))

n = 6

for a in range(2, n+1):
    x = pow(a, 3)
    for b in range(2, n+1):
        y = pow(b, 3)
        for c in range(b, n + 1):
            z = pow(c, 3)
            for d in range(c, n + 1):
                t = pow(d, 3)
                if x == y + z + t:
                    print('Cube = {},Tripe = ({},{},{})'.format(a, b, c, d))

n = 10
while n != 1.0:
    if n % 2 == 0:
        n = n/2
        print(n)
    else:
        n = 3*n+1
        print('{:.1f}'.format(n))

s = '500 1'
l, m = s.split(' ')
l = int(l)
m = int(m)
e = 0
s = pow(2, l+1)-1
l = list(str(bin(s))[2:])
for i in range(m):
    c = '150 300'
    a, b = c.split(' ')
    a = int(a)
    b = int(b)
    for j in range(a,b+1):
        l[j] = '0'
for z in l[:]:
    if z == '1':
        e += 1
print(e)

for i in range(1,10):
    for j in range(1, i+1):
        if i ==j :
            print('{}*{}={}'.format(i,j,i*j))
        else:
            print('{}*{}={}'.format(i,j,i*j),end=' ')
    print('\n')