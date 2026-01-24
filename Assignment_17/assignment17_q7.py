#Number pattern (1 to 5 repeated)

def Pattern(n):
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()

def main():
    num = int(input("Enter number: "))
    Pattern(num)

if __name__ == "__main__":
    main()
