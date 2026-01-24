#Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5

def main():
    Data = ["python", "java", "coding", "AI", "machine"]
    print("Actual Data is :", Data)

    Result = list(filter(lambda x: len(x) > 5, Data))
    print("Strings with length > 5 :", Result)


if __name__ == "__main__":
    main()
