import os


def path_split(path):
    print(os.path.split(path))


def path_split_fully(path):
    parent_path, name = os.path.split(path)
    if name == "":
        return (parent_path, )
    else:
        return path_split_fully(parent_path) + (name,)


if __name__ == "__main__":
    path_split("/test/tt.txt")
    print(path_split_fully("/test/tt.txt"))
