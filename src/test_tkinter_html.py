# import unittest
# from tkinter_html import extract_title


# class TkHTMLTest(unittest.TestCase):
#     def test_extract_title(self) -> None:
#         """
#         Checks if extract_title() returns correct titles
#         """

#         test_cases = [
#             ('something.txt', 'txt'),
#             ('else,txt', None),
#             ('should-fail,txt', None),
#             ('Fundamental-Accessibility-Tests-Basic-Functionality-v2.0.0.epub', 'epub'),
#             ('more.dots.more.dots.mobi', 'mobi'),
#             ('trueeeeee.mobi', 'mobi'),
#             ('testtestest.epub', 'epub'),
#             ('finance.csv', 'csv')
#         ]
#         for case in test_cases:
#             with self.subTest(case=case):
#                 extension = book_types.get_extension(case[0])
#                 self.assertEqual(extension, case[1])
