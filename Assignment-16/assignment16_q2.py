#Check whether a number is even or odd
def ChkNum(no):
    if no % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    num = int(input("Enter number: "))
    ChkNum(num)

if __name__ == "__main__":
    main()
