class Route(object):
    def __init__(self, res):
        self.resource = res

    @classmethod
    def factory(cls):
        print 'factory'
        return cls()

    def __call__(self):
        print 'route __call__'
        return self.resource()


class Resource(object):
    def __call__(self):
        print 'resource __call__'


class API(Route):
    def __init__(self):
        res = Resource()
        super(API, self).__init__(res)


api = API.factory()
api()
