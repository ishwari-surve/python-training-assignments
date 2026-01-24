#Star pattern (5 × 5)
def Pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def main():
    num = int(input("Enter number: "))
    Pattern(num)

if __name__ == "__main__":
    main()
