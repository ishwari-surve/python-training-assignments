#Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.
from functools import reduce

mul = lambda a, b: a * b

def main():
    Data = [1, 2, 3, 4]
    print("Actual Data is :", Data)

    Result = reduce(mul, Data)
    print("Product is :", Result)


if __name__ == "__main__":
    main()
