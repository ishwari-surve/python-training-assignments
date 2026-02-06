#Rename files with one extension to another

import os
import sys

def rename_files(folder, old_ext, new_ext):
    for name in os.listdir(folder):
        if name.endswith(old_ext):
            old_name = folder + "/" + name
            new_name = folder + "/" + name.replace(old_ext, new_ext)
            os.rename(old_name, new_name)

def main():
    if len(sys.argv) != 4:
        print("Usage: python rename.py Folder OldExt NewExt")
        return

    folder = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]

    if os.path.isdir(folder):
        rename_files(folder, old_ext, new_ext)
        print("Files renamed")
    else:
        print("Folder not found")

if __name__ == "__main__":
    main()
