from os import scandir, rename
from os.path import isfile, join, isdir
from unidecode import unidecode


class File:
    def __init__(self, name, new_name):
        self.name = name
        self.new_name = new_name


def make_string_safe(string: str, characters_to_replace: str, replaced_characters_value) -> str:
    # convert unicode string to ascii
    string_safe = unidecode(string)
    # replace other characters
    for char in characters_to_replace:
        string_safe = string_safe.replace(char, replaced_characters_value)
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


def input_binary_decision(decision_text: str) -> bool:
    print(f"\n{decision_text} [y] [n]")
    while True:
        decision = input("  > ")
        if decision == "y":
            return True
        if decision == "n":
            return False
        print("  Try again. Invalid input!")


def input_character_replacements() -> (str, str):
    should_replace_other_characters = input_binary_decision("Want to replace other characters than Unicode e.g. '#$ ?")
    if not should_replace_other_characters:
        return "", ""

    print("\nType the characters you want to replace e.g. #%:")
    characters = input("  > ")

    print("\nWith which character do you want to replace them? [type enter if none]")
    characters_new = input("  > ")

    return characters, characters_new


def rename_filenames() -> None:
    folder_path = input_folder_path()
    characters_to_replace, replaced_characters_value = input_character_replacements()

    # get files 
    files: list[File] = []
    for item in scandir(folder_path):
        if isfile(join(folder_path, item.name)):
            new_filename = make_string_safe(item.name, characters_to_replace, replaced_characters_value)
            files.append(File(item.name, new_filename))

    # print new names of files
    print("\nNew Filenames:")
    for file in files:
        print(file.new_name)

    # rename files (if yes)
    should_rename_files = input_binary_decision("Do you want to rename the files?")
    if should_rename_files:
        for file in files:
            rename(join(folder_path, file.name), join(folder_path, file.new_name))

    print("\nfinished")


def rename_file_contents() -> None:
    file_path = input_file_path()
    characters_to_replace, replaced_characters_value = input_character_replacements()

    print("\nNew File Content:")
    with open(file_path, mode="r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        lines = [make_string_safe(line, characters_to_replace, replaced_characters_value) for line in lines]
        for line in lines:
            print(line)

    should_rename_content = input_binary_decision("Do you want to rename the content of the file?")
    if should_rename_content:
        with open(file_path, "w") as f:
            f.write('\n'.join(lines) + '\n')

    print("\nfinished")


def main() -> None:
    print("** Make Files ASCII **\n")

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


if __name__ == "__main__":
    main()
