import os


def path_abspath(path):
    return os.path.abspath(path)


if __name__ == "__main__":
    print(path_abspath("os_path_abspath.py"))
