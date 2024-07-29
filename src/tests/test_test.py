import unittest # for testing

# test on ci, auto succeeds, previous auto fails
class Test(unittest.TestCase):
    def test_success(self):
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
