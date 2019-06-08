try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestKey(unittest.TestCase):
    def test_key(self):
        a = ['a', 'b']
        b = ['b']
        self.assertEqual(a, b)
