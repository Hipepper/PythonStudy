try:
    import unittest2 as unittest
except ImportError:
    import unittest
try:
    import mylib
except ImportError:
    mylib = None

class TestSkipped(unittest.TestCase):
    @unittest.skip("Do not run this")
    def test_fail(self):
        self.fail("This should not be run")
    @unittest.skipIf(mylib is None, "mylib is not available")
    def test_mylib(self):
        self.assertEqual(mylib.foobar(), 42)

    def test_skip_at_run_time(self):
        if True:
            self.skipTest("Finally I don't want to run it")


