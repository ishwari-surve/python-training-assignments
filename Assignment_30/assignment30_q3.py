#Q3 Display File Line by Line

def display_words(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                for word in line.strip().split():
                    print(word)
    except FileNotFoundError:
        print("File not found. Please check the file name.")

def main():
    fname = input("Enter file name: ")
    display_words(fname)

if __name__ == "__main__":
    main()
