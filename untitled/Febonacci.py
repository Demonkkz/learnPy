class Fibonacci(object):
    # 返回一个fibonacci数列
    def __init__(self):
        self.fList = [0, 1]  # 初始列表设置
        self.main()

    def main(self):
        listLen = input('Please input the Lenth of Fibonacci (3-50):')
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1] + self.fList[-2])
        print('get the List:\n {}'.format(self.fList))

    def checkLen(self, lenth):
        lenList = map(str, range(3, 51))
        if lenth in lenList:
            print('go on')
        else:
            print('unless')
            exit()


if __name__ == '__main__':
    f = Fibonacci()
