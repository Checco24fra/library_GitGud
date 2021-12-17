import unittest
import sys
import os
import library


class TestStringInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_values_book(self):
        """testing correct values for check_book()"""
        self.assertTrue(library.check_book("Pillars of the Earth, The"))
        self.assertTrue(library.check_book("Farewell to Arms, A"))
        self.assertFalse(library.check_book("A Random Book"))

    # invalid inputs
    def test_wrong_values_book(self):
        """testing wrong values for check_book()"""
        self.assertEqual(library.check_book(None), None)
        self.assertEqual(library.check_book(1984), None)
        self.assertEqual(library.check_book([]), None)
        self.assertEqual(library.check_book({}), None)

    # corner case: empty string
    def test_empty_string_book(self):
        """testing corner values for check_book()"""
        self.assertFalse(library.check_book(""))

    # smoke test: valid inputs
    def test_correct_values_author(self):
        """testing correct values for check_author()"""
        self.assertTrue(library.check_author("Feynman, Richard"))
        self.assertTrue(library.check_author("Hemingway, Ernest"))
        self.assertFalse(library.check_author("Santa Claus"))

    # invalid inputs
    def test_wrong_values_author(self):
        """testing wrong values for check_author()"""
        self.assertEqual(library.check_author(None), None)
        self.assertEqual(library.check_author(1984), None)
        self.assertEqual(library.check_author([]), None)
        self.assertEqual(library.check_author({}), None)

    # corner case: empty string
    def test_empty_string_author(self):
        """testing corner values for check_author()"""
        self.assertFalse(library.check_author(""))


if __name__ == '__main__':
    unittest.main(verbosity=2)
