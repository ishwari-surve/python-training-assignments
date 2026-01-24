#2. EvenFactor & OddFactor threads

import threading

def even_factor(n):
    even_factors = [i for i in range(1, n+1) if n % i == 0 and i % 2 == 0]
    print("Even factors:", even_factors)
    print("Sum of even factors:", sum(even_factors))

def odd_factor(n):
    odd_factors = [i for i in range(1, n+1) if n % i == 0 and i % 2 != 0]
    print("Odd factors:", odd_factors)
    print("Sum of odd factors:", sum(odd_factors))

num = int(input("Enter a number: "))
def main(): 

    t1 = threading.Thread(target=even_factor, args=(num,), name="EvenFactor")
    t2 = threading.Thread(target=odd_factor, args=(num,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()

    print("Exit from Main")
