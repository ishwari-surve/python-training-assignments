#Check if number is divisible by 5

def DivisibleByFive(no):
    return no % 5 == 0

def main():
    num = int(input("Enter number: "))
    result = DivisibleByFive(num)
    print(result)

if __name__ == "__main__":
    main()
