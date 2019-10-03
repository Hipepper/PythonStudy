name = 'derek1'


def change_name(name):
    print('before change:', name)
    name = 'derek2'
    print('after change:', name)


change_name(name)
print('not change after function call: ', name)

x = 0


def grandpa():
    x = 1

    def dad():
        x = 2

        def son():
            x = 3
            print(x)

        son()

    dad()


grandpa()
print(x)
