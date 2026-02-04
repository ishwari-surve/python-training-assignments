#Q5: Frequency of a string in file

def CountFrequency(FileName, Word):

    fobj = open(FileName, "r")
    data = fobj.read()
    fobj.close()

    count = data.count(Word)
    return count

def main():

    FileName = input("Enter file name: ")
    Word = input("Enter string to search: ")

    result = CountFrequency(FileName, Word)
    print("Frequency is:", result)

if __name__ == "__main__":
    main()
