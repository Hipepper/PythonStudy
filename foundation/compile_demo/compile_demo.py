test = 0
cmd = "import os\nprint(os.getcwd())\ntest=1"
aa = compile(cmd,'','exec')
scope = {}
exec(cmd, scope)
print(test)