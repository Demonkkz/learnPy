class SweetPotato:
    "这是烤地瓜的类"

    # 定义初始化方法
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []

    #定制print时的显示内容
    def __str__(self):
        return "地瓜状态：%s(%d),添加的佐料：%s"\
               %(self.cookedString,
                 self.cookedLevel,
                 str(self.condiments))

    #烤地瓜方法
    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.cookedString = "烤成灰了"
        elif self.cookedLevel > 5:
            self.cookedString = "烤好了"
        elif self.cookedLevel > 3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"

    #添加配料
    def addCondiments(self, condiments):
        self.condiments.append(condiments)

# 用来进行测试
mySweetPotato = SweetPotato()
print("------有了一个地瓜，还没有烤-----")
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
print(mySweetPotato.condiments)
print("------接下来要进行烤地瓜了-----")
mySweetPotato.cook(1)  # 烤1分钟
print(mySweetPotato)
mySweetPotato.cook(2)  # 又烤了2分钟
print(mySweetPotato)
print("------接下来要添加配料-番茄酱------")
mySweetPotato.addCondiments("番茄酱")
print(mySweetPotato)
mySweetPotato.cook(2)  # 又烤了2分钟
print(mySweetPotato)
print("------接下来要添加配料-芥末酱------")
mySweetPotato.addCondiments("芥末酱")
print(mySweetPotato)
mySweetPotato.cook(2)  # 又烤了2分钟
print(mySweetPotato)
mySweetPotato.cook(2)  # 又烤了2分钟
print(mySweetPotato)
