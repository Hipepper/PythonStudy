import shutil
import os


def make_version_file(path, version):
    if version == 0:
        return path
    else:
        return path + "." + str(version)


def rotate(path, version=0):
    old_path = make_version_file(path, version)
    if not os.path.exists(path):
        raise IOError("'%s' does not exist", path)
    new_path = make_version_file(path, version + 1)
    if os.path.exists(new_path):
        rotate(path, version + 1)
    shutil.move(old_path, new_path)


def rotate_log_file(path):
    if not os.path.exists(path):
        file = open(path, "w")
        file.close()
    rotate(path)


if __name__ == "__main__":
    rotate_log_file("./test.txt")
