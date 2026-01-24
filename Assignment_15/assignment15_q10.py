#Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

def main():
    Data = [1, 2, 3, 4, 5, 6]
    print("Actual Data is :", Data)

    EvenCount = len(list(filter(lambda x: x % 2 == 0, Data)))
    print("Count of Even Numbers :", EvenCount)


if __name__ == "__main__":
    main()
