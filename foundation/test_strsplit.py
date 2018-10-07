
ip = "1.2.3.4:4321"

tt = ip.split(":")
print(tt)
print(tt[1].isdigit())

ip = "1.2.3.4:12x3"

tt = ip.split(":")
print(tt)
print(tt[1].isdigit())

ip = "1.2.3.4"
tt = ip.split(":")
print(tt)

if len(tt) == 1:
    print("no port")