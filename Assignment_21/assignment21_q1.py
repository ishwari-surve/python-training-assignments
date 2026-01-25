# Prime and NonPrime Threads

import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_thread(nums):
    print("Prime numbers:")
    for n in nums:
        if is_prime(n):
            print(n)

def nonprime_thread(nums):
    print("Non-prime numbers:")
    for n in nums:
        if not is_prime(n):
            print(n)

def main():
    nums = list(map(int, input("Enter numbers: ").split()))

    t1 = threading.Thread(target=prime_thread, args=(nums,))
    t2 = threading.Thread(target=nonprime_thread, args=(nums,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
