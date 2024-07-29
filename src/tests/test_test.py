import unittest

class Test(unittest.TestCase):
    def test_fail(self):
        self.assertEqual(1, 2)
    
    def test_success(self):
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()