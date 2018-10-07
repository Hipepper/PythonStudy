import os
import re


def print_py(root, dirs, files):
    for file in files:
        path = os.path.join(root, file)
        path = os.path.normcase(path)
        if re.search(r".*\.py", path):
            print(path)


def walk_dir(walk_dir):
    for root, dirs, files in os.walk(walk_dir):
        print_py(root, dirs, files)


if __name__ == "__main__":
    walk_dir("../")
