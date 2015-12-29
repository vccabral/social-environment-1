import unittest
from django.core import management
from nose.plugins.skip import SkipTest

class SimplisticTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)


@SkipTest
class OutcomesTest(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('Test error!')


@SkipTest
class FailureMessageTest(unittest.TestCase):
    def test_fail(self):
        self.assertTrue(False, 'failure message goes here')


class TestStringMethods(unittest.TestCase):
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
