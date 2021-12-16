import unittest
import sys
import os
import library

class TestStringInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_values_initial_author(self):
        """testing correct values for the function check_by_initial_author()"""
        self.assertEqual(library.check_by_initial_author("A"), ['Arthur C. Clarke'])
        self.assertEqual(library.check_by_initial_author("a"), ['Arthur C. Clarke'])
        self.assertEqual(library.check_by_initial_author("J"), ['Jane Austen', 'J. R. R. Tolkien'])
        self.assertEqual(library.check_by_initial_author("B"), [])
        self.assertFalse(library.check_by_initial_author("Ba"))
        self.assertFalse(library.check_by_initial_author(""))

    def test_wrong_values_initial_author(self):
        """testing wrong values for the function check_by_initial_author()"""
        self.assertEqual(library.check_by_initial_author(3), None)
        self.assertEqual(library.check_by_initial_author(["a"]), None)
        self.assertEqual(library.check_by_initial_author(False), None)

    def test_corner_values_initial_author(self):
        """testing corner values for the function check_by_initial_author()"""
        self.assertEqual(library.check_by_initial_author("@"), [''])

    def test_correct_values_initial_title(self):
        """testing correct values for the function check_by_initial_title()"""
        self.assertEqual(library.check_by_initial_title("a"), ['A Christmas Carol'])
        self.assertEqual(library.check_by_initial_title("T"), [
                                                                'The Great Gatsby',
                                                                'The Lord of the Rings',
                                                                'The Old Man and the Sea',
                                                                'The Picture of Dorian Gray'
                                                                ])
        self.assertEqual(library.check_by_initial_title("v"), [])
        self.assertFalse(library.check_by_initial_title("kek"))

    def test_wrong_values_initial_title(self):
        """testing wrong values for the function check_by_initial_title()"""
        self.assertEqual(library.check_by_initial_title(""), None)
        self.assertEqual(library.check_by_initial_title(["b"]), None)
        self.assertEqual(library.check_by_initial_title(True), None)

    def test_corner_values_initial_title(self):
        """testing corner values for the function check_by_initial_title()"""
        self.assertEqual(library.check_by_initial_author("@"), [''])
