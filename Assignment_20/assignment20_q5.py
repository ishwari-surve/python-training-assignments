#Thread synchronization (Thread2 after Thread1)

import threading

def thread1():
    print("Thread1 output:")
    for i in range(1, 51):
        print(i)

def thread2():
    print("Thread2 output:")
    for i in range(50, 0, -1):
        print(i)

def main():
    t1 = threading.Thread(target=thread1, name="Thread1")
    t2 = threading.Thread(target=thread2, name="Thread2")

    t1.start()
    t1.join()   # Thread2 starts only after Thread1 finishes

    t2.start()
    t2.join()

if __name__=="__main__":
    main()