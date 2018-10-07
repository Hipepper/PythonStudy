import os

print(os.getcwd())

strpath = "E:\workspace\python-projects\OpenStackTest.rar"
parent_path,name = os.path.split(strpath)
print(parent_path)
os.chdir(parent_path)

print(os.getcwd())