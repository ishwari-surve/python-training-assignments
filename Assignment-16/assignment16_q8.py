#Print * number of times

def DisplayStars(no):
    for i in range(no):
        print("*", end=" ")

def main():
    num = int(input("Enter number: "))
    DisplayStars(num)

if __name__ == "__main__":
    main()
