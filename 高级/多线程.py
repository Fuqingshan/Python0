#_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。
import _thread
import  time
import threading
import queue

'''
#为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s : %s" % (threadName, time.ctime(time.time())))


#创建两个线程
try:
    _thread.start_new_thread(print_time, ("Thread-1",2,))
    _thread.start_new_thread(print_time, ("Thread-2",4,))
except:
    print("启动线程失败")
while 1:
    pass
'''

'''
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self,threadID,name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print("开始线程" + self.name)
        print_time(self.name, self.delay, 5)
        print("退出线程" + self.name)
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s %s" % (threadName, time.ctime(time.time())))
        counter -= 1
#创建新线程
thread1 = myThread(1,"***Thread-1",1)
thread2 = myThread(2,"***Thread-2",2)

#开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
'''

#锁
'''
class myThread(threading.Thread):
    def __init__(self,threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print("开启线程" + self.name)
        #获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.delay, 3)
        #释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s %s" % (threadName, time.ctime(time.time())))
        counter -= 1
threadLock = threading.Lock()
threads = []

#创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
#开启新线程
thread1.start()
thread2.start()

#添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

#等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
'''

#线程优先级队列（ Queue）
exitFlag = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("开启线程" + self.name)
        process_data(self.name, self.q)
        print("退出线程" + self.name)

def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1","Thread-2","Thread-3"]
nameList = ["One","Two","Three","Four","Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1
#创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

#填充队列
queueLock.acquire()
for work in nameList:
    workQueue.put(work)
queueLock.release()

#等待队列清空
while not workQueue.empty():
    pass

#通知线程退出
exitFlag = 1

#等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
