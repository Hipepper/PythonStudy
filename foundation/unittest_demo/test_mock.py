try:
    import unittest2 as unittest
except ImportError:
    import unittest
try:
    from unittest import mock
except ImportError:
    import mock

m = mock.Mock()
m.some_method.return_value = 42
print(m.some_method())
def print_hello():
    print("Hello world!")

m.some_method.side_effect = print_hello
m.some_method()

print(m.some_method.call_count)

m.some_method('foo', 'bar')
