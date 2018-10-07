import  re

a = "123"
patten = "12*"

if re.match(patten, a):
    print("true")
else:
    print("false")
