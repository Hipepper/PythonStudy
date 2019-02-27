module = __import__("test_class")
print(module)
obj = getattr(module, "obj")
obj.test()
