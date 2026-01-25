# Maximum and Minimum Using Two Threads

import threading

def find_max(nums):
    print("Maximum element:", max(nums))

def find_min(nums):
    print("Minimum element:", min(nums))

def main():
    nums = list(map(int, input("Enter numbers: ").split()))

    t1 = threading.Thread(target=find_max, args=(nums,))
    t2 = threading.Thread(target=find_min, args=(nums,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
