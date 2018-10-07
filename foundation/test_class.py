from oslo_utils import reflection

class A(object):
    def __init__(self):
        print "enter A"
        print "leave A"


class B(A):
    def __init__(self):
        print "enter B"
        super(B, self).__init__()
        print "leave B"
        cls_name = reflection.get_class_name(self, fully_qualified=False)
        print cls_name

    def test(self):
        print "test"


app = B()

print '.'.join(["test", 'haha'])


