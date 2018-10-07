import os


def path_exists(path):
    return os.path.exists(path)


if __name__ == "__main__":
    print(path_exists("os_path_abspath.py"))
