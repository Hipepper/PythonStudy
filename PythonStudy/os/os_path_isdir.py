import os


def print_tree(path):
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        print(full_path)
        if os.path.isdir(full_path):
            print_tree(full_path)


if __name__ == "__main__":
    print(print_tree(".."))
