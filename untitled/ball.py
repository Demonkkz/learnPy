import random


class SelectBall(object):
    def __init__(self):
        self.run()

    def run(self):
        while True:
            numStr = input('Test times:')
            try:
                num = int(numStr)
            except ValueError as e:
                print('Number')
                continue
            else:
                break
        ball = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(num):
            n = random.randint(0, 9)
            ball[n] += 1
        for i in range(1, 11):
            print('{}号球概率为{}'.format(i, ball[i-1]/num))


if __name__ == '__main__':
    SB = SelectBall()