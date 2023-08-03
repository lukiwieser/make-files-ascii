from os import scandir, rename
from os.path import isfile, join, isdir
from unidecode import unidecode

class File:
    def __init__(self, name, new_name):
        self.name = name
        self.new_name = new_name

def make_string_safe(string: str) -> str:
    string_ascii = unidecode(string) # convert unicode string to ascii
    string_safe = string_ascii.replace("'"," ") # replace ' since it is invalid char in kaggle
    return string_safe

def input_file_path() -> str:
    print("\nFile Path:")
    while True:
        path = input("  > ")
        if isfile(path):
            return path
        print("  Try again. This file does not exist!")

def input_folder_path() -> str:
    print("\nFolder Path:")
    while True:
        path = input("  > ")
        if isdir(path):
            return path
        print("  Try again. This folder does not exist!")

def input_rename_decision() -> bool:
    print("\nDo you want to rename the files? [y] [n]")
    while True:
        decision = input("  > ")
        if decision == "y":
            return True
        if decision == "n":
            return False
        print("  Try again. Invalid input!")

def input_rename_decision_filecontents() -> bool:
    print("\nDo you want to rename the content of the file? [y] [n]")
    while True:
        decision = input("  > ")
        if decision == "y":
            return True
        if decision == "n":
            return False
        print("  Try again. Invalid input!")

def rename_filenames() -> None:
    folder_path = input_folder_path()

    # get files 
    files: list[File] = []
    for item in scandir(folder_path):
        if isfile(join(folder_path, item.name)):
            files.append(File(item.name, make_string_safe(item.name)))

    # print new names of files
    print("\nNew Filenames:")
    for file in files:
        print(file.new_name)

    # rename files (if yes)
    should_rename_files = input_rename_decision()
    if should_rename_files:
        for file in files:
            rename(join(folder_path, file.name), join(folder_path, file.new_name))

    print("\nfinished")

def rename_file_contents() -> None:
    file_path = input_file_path()

    print("\nNew File Content:")
    lines = []
    with open(file_path, mode="r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        lines = [make_string_safe(line) for line in lines]
        for line in lines:
            print(line)

    should_rename_content = input_rename_decision_filecontents()
    if should_rename_content:
        with open(file_path, "w") as f:
            f.write('\n'.join(lines) + '\n')


def main() -> None:
    print("What do you want to do?:")
    print("  [1] Rename all filenames in a folder")
    print("  [2] Rename content of a file")
    decision = input("  > ")

    if decision == "1":
        rename_filenames()
    elif decision == "2":
        rename_file_contents()
    else:
        print("  Error - This Selection does not exist!")


main()

