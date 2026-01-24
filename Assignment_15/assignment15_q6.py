#Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.
from functools import reduce

minimum = lambda a, b: a if a < b else b

def main():
    Data = [10, 45, 3, 99, 23]
    print("Actual Data is :", Data)

    Result = reduce(minimum, Data)
    print("Minimum element is :", Result)


if __name__ == "__main__":
    main()
