# 1.Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

def main():
    Data = [1, 2, 3, 4, 5]
    print("Actual Data is :", Data)

    Square = list(map(lambda x: x * x, Data))
    print("Squares are :", Square)


if __name__ == "__main__":
    main()
