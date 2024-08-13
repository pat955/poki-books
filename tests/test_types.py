import unittest
from src import book_types

class TypesTest(unittest.TestCase):
    def test_get_extensions(self):
        cases = [
            ('something.txt','txt'),
            ('else,txt', ''),
            ('trueeeeee.mobi', 'mobi'),
            ('testtestest.epub', 'epub')
        ]
        for case in cases:
            with self.subTest(case=case):
                extension =  book_types.get_extension(case[0])
                print(extension)  # Optional: you can remove this line in actual tests
                self.assertEqual(extension, case[1])

if __name__ == '__main__':
    unittest.main()