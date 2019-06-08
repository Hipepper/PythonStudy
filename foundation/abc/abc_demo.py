


class RegisteredImplementation(object):
    def func_c(self, data):
        print("Method in third-party class, " + str(data))


class SubclassImplementation(PluginBase):
    def func_a(self, data):
        print("Overriding func_a, " + str(data))

    def func_b(self, data):
        print("Overriding func_b, " + str(data))

    def func_d(self, data):
        print(data)


PluginBase.register(RegisteredImplementation)

if __name__ == '__main__':
    for sc in PluginBase.__subclasses__():
        print("subclass of PluginBase: " + sc.__name__)
    print("")

    print(issubclass(RegisteredImplementation, PluginBase))
    print(isinstance(RegisteredImplementation(), PluginBase))
    print(issubclass(SubclassImplementation, PluginBase))
    print("")

    obj1 = RegisteredImplementation()
    obj1.func_c("It's right!")
    print("")

    obj2 = SubclassImplementation()
    obj2.func_a("It's right!")
    print("")
