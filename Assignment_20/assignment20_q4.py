#Small, Capital & Digits threads

import threading

def small(s):
    count = sum(1 for c in s if c.islower())
    print("Lowercase count:", count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)

def capital(s):
    count = sum(1 for c in s if c.isupper())
    print("Uppercase count:", count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)

def digits(s):
    count = sum(1 for c in s if c.isdigit())
    print("Digits count:", count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)

text = input("Enter a string: ")

def main(): 
    t1 = threading.Thread(target=small, args=(text,), name="Small")
    t2 = threading.Thread(target=capital, args=(text,), name="Capital")
    t3 = threading.Thread(target=digits, args=(text,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__=="__main__":
    main()

