#Prime number check

def Prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    num = int(input("Enter number: "))
    if Prime(num):
        print("It is Prime Number")
    else:
        print("It is Not Prime")

if __name__ == "__main__":
    main()
