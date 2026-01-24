#2.Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

def main():
    Data = [1, 2, 3, 4, 5, 6]
    print("Actual Data is :", Data)

    Even = list(filter(lambda x: x % 2 == 0, Data))
    print("Even Numbers are :", Even)


if __name__ == "__main__":
    main()

