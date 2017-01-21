
class A(object):
    def __init__(self):
        print "A:__init__"
        pass


class B(A):
    def __init__(self):
        print "B__init__"
        super(B, self).__init__()
        pass

b = B()
