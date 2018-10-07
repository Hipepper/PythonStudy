
class route(object):
    def __init__(self, res):
        print 'route __init__'
        self.resource = res

    @classmethod
    def factory(cls):
        print 'factory'
        return cls()

    def __call__(self, req):
        print 'route __call__'
        return self.resource(req)


class resource(object):
    def __call__(self, req):
        print 'resource __call__'


class API(route):
    def __init__(self):
        print 'API __init__'
        res = resource()
        super(API, self).__init__(res)


a = API.factory()("AA")
# a("AA")

