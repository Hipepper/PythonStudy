import os


def walk_dir(walk_dir):
    for root, dirs, files in os.walk(walk_dir):
        print(root)
        print(dirs)
        print(files)

if __name__ == "__main__":
    walk_dir("../")
