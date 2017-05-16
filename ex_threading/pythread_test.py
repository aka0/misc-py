import threading
import Queue


names = []
name_queue = Queue.Queue()

def cap_name(tid):
    global names
    global name_queue

    while name_queue.qsize() != 0:
        name = name_queue.get()
        print(tid + ' ' + str(name_queue.qsize()) + ' ' + name.rstrip().upper())
        name_queue.task_done()
    
def main():
    global names
    global name_queue

    with open('firstnames.txt') as f:
        names = f.readlines()

    print('Total Names: {}'.format(str(len(names))))

    for n in names:
        name_queue.put(n)

    threads = []
    for i in range(10):
        t = threading.Thread(target=cap_name, args=(str(i),))
        t.setDaemon(True)
        threads.append(t)
        t.start()
    
    name_queue.join()

if __name__ == '__main__':
    main()