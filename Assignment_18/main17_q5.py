import MarvelousNum_q5

def ListPrime(numbers):
    prime_list = []

    for num in numbers:
        if MarvelousNum_q5.ChkPrime(num):
            prime_list.append(num)

    return prime_list


def main():
    n = int(input("Input number of elements: "))

    elements = list(map(int, input("Input Elements: ").split()))

    prime_numbers = ListPrime(elements)
    total = sum(prime_numbers)

    prime_str = " + ".join(str(p) for p in prime_numbers)
    print(f"Output: {total} ({prime_str})")


if __name__ == "__main__":
    main()

