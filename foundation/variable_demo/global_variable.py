name = 'derek1'


def change_name():
    global name
    print('before change:', name)
    name = 'derek2'
    print('after change:', name)


change_name()
print('change after function call: ', name)