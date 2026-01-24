#Accept N numbers and return frequency of a given number

def FrequencyOfNumber():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        value = int(input("Enter element: "))
        data.append(value)

    search = int(input("Enter element to search: "))
    count = data.count(search)
    return count


if __name__ == "__main__":
    result = FrequencyOfNumber()
    print("Frequency:", result)
