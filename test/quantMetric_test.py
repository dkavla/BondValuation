"""
    This is a test file for testing whether the functionality
    of the functions in the quantMetric.py file work as intended
"""

import unittest
from quantMetrics import Macaulay_Duration
from Bond import Bond
import sys

class TestQuantMetrics(unittest.TestCase):

    """First three tests are for Macaulay Duration function"""
    def test_one_Macaulay_Duration(self):
        a = Bond(3, 8, 1000, 10, 950)
        self.assertEqual(Macaulay_Duration(a), 2.78, "Mac. Duration expected to be 2.77")

    def test_two_Macaualy_Duration(self):
        b = Bond(3, 0, 1000, 10, 751)
        self.assertEqual(Macaulay_Duration(b), 3.00, "Mac. Duration expected to be 3.00")

    def test_three_Macaulay_Duration(self):
        c = Bond(10, 6, 1000, 7, 925)
        self.assertEqual(Macaulay_Duration(c), 7.71, "Mac Duration expected to be 2.71")

if __name__ == "__main__":
    unittest.main()