#Q3: Copy File Contents into New File (Command Line)

import sys

def CopyFile(SourceFile, DestFile):
    try:
        with open(SourceFile, "r") as src:
            data = src.read()

        with open(DestFile, "w") as dest:
            dest.write(data)

        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <ABC.txt>")
        return

    SourceFile = sys.argv[1]
    DestFile = "Demo.txt"
    CopyFile(SourceFile, DestFile)

if __name__ == "__main__":
    main()