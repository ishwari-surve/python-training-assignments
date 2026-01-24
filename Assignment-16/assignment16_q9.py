#Display first 10 even numbers

def DisplayEven():
    count = 0
    num = 2
    while count < 10:
        print(num, end=" ")
        num += 2
        count += 1

def main():
    DisplayEven()

if __name__ == "__main__":
    main()
