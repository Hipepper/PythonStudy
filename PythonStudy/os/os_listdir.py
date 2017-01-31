import os


def os_listdir(path):
    return os.listdir(path)


if __name__ == "__main__":
    print(os_listdir("."))
