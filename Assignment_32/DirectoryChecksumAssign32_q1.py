#DirectoryChecksum

import os
import sys
import hashlib

def CalculateChecksum(FilePath):
    fobj = open(FilePath, "rb")
    data = fobj.read()
    fobj.close()
    return hashlib.md5(data).hexdigest()

def DirectoryChecksum(DirName):
    log = open("Log.txt", "w")

    for file in os.listdir(DirName):
        path = os.path.join(DirName, file)

        if os.path.isfile(path):
            checksum = CalculateChecksum(path)
            log.write(file + " : " + checksum + "\n")

    log.close()

def main():
    if len(sys.argv) != 2:
        return

    DirName = sys.argv[1]

    if os.path.isdir(DirName):
        DirectoryChecksum(DirName)

if __name__ == "__main__":
    main()

