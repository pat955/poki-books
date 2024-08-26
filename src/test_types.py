import unittest
import book_types


class TypesTest(unittest.TestCase):
    def test_get_extensions(self) -> None:
        """
        tests if get_extension() returns correct extension
        """
        cases = [
            ('something.txt', 'txt'),
            ('else,txt', ''),
            ('trueeeeee.mobi', 'mobi'),
            ('testtestest.epub', 'epub')
        ]
        for case in cases:
            with self.subTest(case=case):
                extension = book_types.get_extension(case[0])
                # Optional: you can remove this line in actual tests
                print(extension)
                self.assertEqual(extension, case[1])