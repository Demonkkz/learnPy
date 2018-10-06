import random

i = y = 0
while 1:
    S = input('石头0剪刀1布2：')
    C = random.randint(0,2)
    S = int(S)
    C = int(C)
    if (C-S == 1)or(S-C == 2): ##我赢的情况
        print('S.win')
        i= i+1
        if i>1:
            print('you win')
            break
    elif S==C :
        print('Ping')
    else:
        print('C.win')
        y = y+1
        if y>1:
            print('you lose')
            break
