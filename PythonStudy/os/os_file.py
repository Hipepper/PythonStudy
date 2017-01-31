import os


def create_file(filepath):
    file = open(filepath, "w")
    file.write("This is how you create a new text file\n")
    file.close()


def create_exist_file(filepath):
    if os.path.exists(filepath):
        print("You are trying to create a file that already exists")
    else:
        create_file(filepath)


def add_text_to_file(filepath):
    file = open(filepath, "a")
    file.write("Here is some additional text\n")
    file.close()


def readline_file(filepath):
    file = open(filepath, "r")
    for line in file.readlines():
        print(line, end="")
    file.close()


def read_file(filepath):
    file = open(filepath, "r")
    lines = file.read()
    print(lines)
    file.close()


if __name__ == "__main__":
    create_file("./test.txt")
    # create_exist_file("./test.txt")
    add_text_to_file("./test.txt")
    readline_file("./test.txt")
    read_file("./test.txt")
