import hashlib

m = hashlib.md5()  # m=hashlib.sha256()
m.update('hello'.encode('utf8'))
print(m.hexdigest())  # 5d41402abc4b2a76b9719d911017c592
m.update('alvin'.encode('utf8'))
print(m.hexdigest())  # 92a7e713c30abbb0319fa07da2a5c4af
m2 = hashlib.md5()
m2.update('helloalvin'.encode('utf8'))
print(m2.hexdigest())  # 92a7e713c30abbb0319fa07da2a5c4af
