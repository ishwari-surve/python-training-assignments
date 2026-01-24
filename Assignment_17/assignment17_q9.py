#Count digits
def CountDigits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def main():
    num = int(input("Enter number: "))
    print("Digits:", CountDigits(num))

if __name__ == "__main__":
    main()
