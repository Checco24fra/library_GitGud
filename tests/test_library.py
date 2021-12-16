import unittest
import sys
import os
import library


class TestStringInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_values_book(self):
        self.assertEqual(library.check_book("A Christmas Carol"))
        self.assertEqual(library.check_book("A Random Book"))

    # invalid inputs
    def test_wrong_values_book(self):
        # you should input wrong data
        self.assertEqual(library.check_book(None))
        self.assertEqual(library.check_book(1984))
        self.assertEqual(library.check_book([]))
        self.assertEqual(library.check_book())

    # corner case: empty string
    def test_empty_string_book(self):
        self.assertEqual(library.check_book(""))

    # smoke test: valid inputs
    def test_correct_values_book(self):
        self.assertEqual(library.check_book("A Christmas Carol"))
        self.assertEqual(library.check_book("A Random Book"))

    # invalid inputs
    def test_wrong_values_book(self):
        # you should input wrong data
        self.assertEqual(library.check_book(None))
        self.assertEqual(library.check_book(1984))
        self.assertEqual(library.check_book([]))
        self.assertEqual(library.check_book())

    # corner case: empty string
    def test_empty_string_book(self):
        self.assertEqual(library.check_book(""))



if __name__ == '__main__':
    unittest.main(verbosity=2)
