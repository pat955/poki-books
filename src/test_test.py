""" test_test.py
follow *_test.py pattern for test modules
this test will auto succeed, previously auto fail for ci testting
"""
import unittest

class Test(unittest.TestCase):
    """
    test for testing unitests :) 

    """
    def test_success(self):
        """
        auto succeeds
        """
        self.assertEqual(1, 1)

    # def test_failure(self):
    #     """
    #     auto fails
    #     """
    #     self.assertEqual(1, 2)
