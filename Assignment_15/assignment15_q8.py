#Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.
def main():
    Data = [10, 15, 20, 30, 45, 7]
    print("Actual Data is :", Data)

    Result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, Data))
    print("Divisible by 3 and 5 :", Result)


if __name__ == "__main__":
    main()
