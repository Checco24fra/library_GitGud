import unittest
import sys
import os
import library


class TestStringInput(unittest.TestCase):


    # smoke test: valid inputs
    def test_correct_values_book(self):
        self.assertTrue(library.check_book("A Christmas Carol"))
        self.assertTrue(library.check_book("The Lord of the Rings"))
        self.assertFalse(library.check_book("A Random Book"))

    # invalid inputs
    def test_wrong_values_book(self):
        self.assertEqual(library.check_book(None), None)
        self.assertEqual(library.check_book(1984), None)
        self.assertEqual(library.check_book([]), None)
        self.assertEqual(library.check_book({}), None)

    # corner case: empty string
    def test_empty_string_book(self):
        self.assertFalse(library.check_book(""))

    # smoke test: valid inputs
    def test_correct_values_author(self):
        self.assertTrue(library.check_author("Jane Austen"))
        self.assertTrue(library.check_author("Ernest Hemingway"))
        self.assertFalse(library.check_author("Santa Claus"))
    # invalid inputs
    def test_wrong_values_author(self):
        self.assertEqual(library.check_author(None), None)
        self.assertEqual(library.check_author(1984), None)
        self.assertEqual(library.check_author([]), None)
        self.assertEqual(library.check_author({}), None)

    # corner case: empty string
    def test_empty_string_author(self):
        self.assertFalse(library.check_author(""))



if __name__ == '__main__':
    unittest.main(verbosity=2)
