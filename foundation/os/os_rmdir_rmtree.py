import os
import shutil

if __name__ == "__main__":
    # os.makedir("./test")
    os.makedirs("./test/123")
    os.makedirs("./test2")

    os.rmdir("./test2")
    # os.rmdir("./test")

    shutil.rmtree("./test")