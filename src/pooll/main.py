import multiprocessing
from multiprocessing import Process


def f1(name, q):
    while True:
        item = q.get()
        if item is None:
            break
        print(item)
        print(" " + name + "    " + str(item))


# 固定数量的任务
def size_task():
    q = multiprocessing.Queue()
    for i in range(10):
        q.put(i)
    
    producer = []
    for i in range(3):
        producer.append(Process(target=f1, args=(('name' + str(i), q))))
    
    for p in producer:
        p.start()
    for p in producer:
        q.put(None)
    for p in producer:
        p.join()
    print('父进程结束')


def q1(name, q, id):
    for i in range(10):
        q.put(id * 10 + i)


def c1(name, q):
    while True:
        x = q.get()
        if x is None:
            break
        print(x)


def not_size_task():
    producer = []
    q = multiprocessing.Queue()
    for i in range(3):
        x = Process(target=q1, args=(('生产者-1', q, i)))
        producer.append(x)
    for x in producer:
        x.start()
    for x in producer:
        x.join()
    consumer = []
    for i in range(2):
        x = Process(target=c1, args=(('消费者', q)))
        x.daemon = True
        consumer.append(x)
    for x in consumer:
        x.start()
    for x in consumer:
        q.put(None)
    for x in consumer:
        x.join()
    print('main is over')


if __name__ == '__main__':
    # 固定任务生产者
    size_task()
    # 不定项消费者
    not_size_task()
