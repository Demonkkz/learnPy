import threading


def test(x, y):
    for i in range(x, y):
        print(i)


thread1 = threading.Thread(name='t1', target=test, args=(100, 300))
thread2 = threading.Thread(name='t2', target=test, args=(310, 500))
thread3 = threading.Thread(name='t3', target=test, args=(510, 700))
thread1.start()
thread2.start()
thread3.start()


class mythread(threading.Thread):
    def run(self):
        for i in range(800, 1000):
            print(i)


thread1 = mythread()
thread2 = mythread()
thread1.start()
thread2.start()
