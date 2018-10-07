import os


def path_split_ext(path):
    return os.path.splitext(path)


if __name__ == "__main__":
    print(path_split_ext("/test/tt.txt"))
