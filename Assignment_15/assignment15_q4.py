#Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.
from functools import reduce

add = lambda a, b: a + b

def main():
    Data = [12, 45, 67, 3, 8]
    print("Actual Data is :", Data)

    Result = reduce(add, Data)
    print("Addition is :", Result)


if __name__ == "__main__":
    main()
