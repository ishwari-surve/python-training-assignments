#Check positive, negative or zero

def CheckNumber(no):
    if no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    num = int(input("Enter number: "))
    CheckNumber(num)

if __name__ == "__main__":
    main()
