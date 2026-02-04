#Q2: Count Words in a File

def CountWords(FileName):

    fobj = open(FileName, "r")
    data = fobj.read()
    fobj.close()

    words = data.split()
    return len(words)

def main():

    FileName = input("Enter file name: ")

    result = CountWords(FileName)
    print("Total number of words:", result)

if __name__ == "__main__":
    main()
