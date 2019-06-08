import six
import abc


@six.add_metaclass(abc.ABCMeta)
class Base(object):
    @abc.abstractproperty
    def value(self):
        return 'Should never get here'


class Implementation(Base):
    @property
    def value(self):
        return 'concrete property'


try:
    b = Base()
    print('Base.value:', b.value)
except Exception as err:
    print('ERROR:', str(err))

i = Implementation()
print('Implementation.value:', i.value)
