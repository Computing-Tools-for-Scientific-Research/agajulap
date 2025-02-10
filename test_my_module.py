import unittest
from my_module import function_to_test

class TestMyModule(unittest.TestCase):
    def test_function_to_test(self):
        self.assertEqual(function_to_test(5), 10)

if __name__ == '__main__':
    unittest.main()