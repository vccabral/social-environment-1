import unittest


class SimplisticTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

class OutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('Test error!')

class FailureMessageTest(unittest.TestCase):

    def test_fail(self):
        self.assertTrue(False, 'failure message goes here')

if __name__ == '__main__':
    unittest.main()