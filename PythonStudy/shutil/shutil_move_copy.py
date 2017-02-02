import shutil
import os

def create_file(filepath):
    file = open(filepath, "w")
    file.write("This is how you create a new text file\n")
    file.close()


if __name__ == "__main__":
    create_file("./test.txt")

    shutil.move("./test.txt", "./test2.txt")

    shutil.copy("./test2.txt", "./test3.txt")

    os.remove("./test2.txt")
    os.remove("./test3.txt")
