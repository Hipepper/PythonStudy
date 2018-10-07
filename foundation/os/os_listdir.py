import os


def print_dir(path):
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        print(full_path)


def os_listdir(path):
    return os.listdir(path)


if __name__ == "__main__":
    print(os_listdir("."))
    print_dir(".")