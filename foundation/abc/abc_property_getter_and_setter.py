import six
import abc


@six.add_metaclass(abc.ABCMeta)
class Base(object):
    def value_getter(self):
        return ('Should never see this')

    def value_setter(self, newvalue):
        return

    value = abc.abstractproperty(value_getter, value_setter)


class PartialImplementation(Base):
    @abc.abstractproperty
    def value(self):
        return 'Read-only'


class Implementation(Base):
    _value = 'Default value'

    def value_getter(self):
        return self._value

    def value_setter(self, newvalue):
        self._value = newvalue

    # 定义具体类的property时必须与抽象类的abstract property相同。如果只覆盖其中一个将不会工作。
    value = property(value_getter, value_setter)


try:
    b = Base()
    print('Base.value:', b.value)
except Exception as err:
    print('ERROR:', str(err))

try:
    p = PartialImplementation()
    print('PartialImplementation.value:', p.value)
except Exception as err:
    print('ERROR:', str(err))

i = Implementation()
print('Implementation.value:', i.value)

i.value = 'New value'
print('Changed value:', i.value)
