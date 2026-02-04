#Q5 Search a word in file

def SearchWordInFile(filename):
    try:
        file = open(filename, "r")
        content = file.read().lower()
        file.close()

        word = input("Enter word to search: ").lower()

        if word in content.split():
            print("Word is present in the file")
        else:
            print("Word is not present in the file")

    except FileNotFoundError:
        print("File does not exist")

def main():
    fname = input("Enter file name: ")
    SearchWordInFile(fname)

if __name__ == "__main__":
    main()
