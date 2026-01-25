# Multiple Threads Updating a Shared Variable (Using Lock)

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

def main():
    threads = []

    for _ in range(5):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Final counter value:", counter)

if __name__ == "__main__":
    main()
