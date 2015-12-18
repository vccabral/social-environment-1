import unittest
from import_raw_data import get_year_range

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
class TestStringMethods(unittest.TestCase):
    def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

class test_get_year_range(unittest.TestCase):
    def test_is_valid_year(self):
        self.assertEqual(get_year_range('2013','2014'),1)

if __name__ == '__main__':
    unittest.main()


