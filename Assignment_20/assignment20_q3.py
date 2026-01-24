#EvenList & OddList threads

import threading

def even_list(lst):
    evens = [i for i in lst if i % 2 == 0]
    print("Even elements:", evens)
    print("Sum of even elements:", sum(evens))

def odd_list(lst):
    odds = [i for i in lst if i % 2 != 0]
    print("Odd elements:", odds)
    print("Sum of odd elements:", sum(odds))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

def main(): 
    t1 = threading.Thread(target=even_list, args=(numbers,), name="EvenList")
    t2 = threading.Thread(target=odd_list, args=(numbers,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()

    print("Exit from Main")