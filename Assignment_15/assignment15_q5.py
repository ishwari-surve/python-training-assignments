#Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element

from functools import reduce

maximum = lambda a, b: a if a > b else b

def main():
    Data = [10, 45, 3, 99, 23]
    print("Actual Data is :", Data)

    Result = reduce(maximum, Data)
    print("Maximum element is :", Result)


if __name__ == "__main__":
    main()
