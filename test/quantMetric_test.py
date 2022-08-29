"""
    This is a test file for testing whether the functionality
    of the functions in the quantMetric.py file work as intended
"""

import unittest
from quantMetrics import Macaulay_Duration, Modified_Duration
from Bond import Bond
import sys

class TestQuantMetrics(unittest.TestCase):

    def test_one_Macaulay_Duration(self):
        a = Bond(3, 8, 1000, 10, 950)
        self.assertEqual(Macaulay_Duration(a), 2.78, "Mac. Duration expected to be 2.77")

    def test_two_Macaualy_Duration(self):
        b = Bond(3, 0, 1000, 10, 751)
        self.assertEqual(Macaulay_Duration(b), 3.00, "Mac. Duration expected to be 3.00")

    def test_three_Macaulay_Duration(self):
        c = Bond(10, 6, 1000, 7, 925)
        self.assertEqual(Macaulay_Duration(c), 7.71, "Mac Duration expected to be 7.71")


    def test_one_Modified_Duration(self):
        a = Bond(3, 8, 1000, 10, 950)
        self.assertEqual(Modified_Duration(a), 2.53, "Mod. Duration expected to be 2.78")

    def test_two_Modified_Duration(self):
        b = Bond(3, 0, 1000, 10, 751)
        self.assertEqual(Modified_Duration(b), 2.73, "Mod. Duration expected to be 2.73")

    def test_three_Modified_Duration(self):
        c = Bond(10, 6, 1000, 7, 925)
        self.assertEqual(Modified_Duration(c), 7.21, "Mod. Duration expected to be 7.21")


if __name__ == "__main__":
    unittest.main()