#Q4 Copy file contents into another file

def copy_file(source, destination):
    try:
        src = open(source, "r")
        dest = open(destination, "w")

        text = src.read()
        dest.write(text)

        src.close()
        dest.close()

        print("File copied successfully")
    except FileNotFoundError:
        print("Source file not found")

def main():
    src_name = input("Enter source file name: ")
    dest_name = input("Enter destination file name: ")

    copy_file(src_name, dest_name)

if __name__ == "__main__":
    main()
