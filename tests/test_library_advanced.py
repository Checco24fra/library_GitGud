import unittest
import sys
import os
import library


class TestStringInput(unittest.TestCase):
    # smoke test: valid inputs
    def test_correct_values_initial_author(self):
        """testing correct values for the function check_by_initial_author()"""
        self.assertEqual(library.check_by_initial_author("A"), [
            'Ackroyd, Peter', 'Aczel, Amir',
            'Archer, Jeffery', 'Archer, Jeffery'
            ])
        self.assertEqual(library.check_by_initial_author("a"), [
            'Ackroyd, Peter', 'Aczel, Amir',
            'Archer, Jeffery', 'Archer, Jeffery'
            ])
        self.assertEqual(library.check_by_initial_author("J"), [
            'Janert, Phillip'
            ])
        self.assertEqual(library.check_by_initial_author("u"), [])
        self.assertFalse(library.check_by_initial_author("Ba"))
        self.assertFalse(library.check_by_initial_author(""))

    # invalid inputs
    def test_wrong_values_initial_author(self):
        """testing wrong values for the function check_by_initial_author()"""
        self.assertEqual(library.check_by_initial_author(3), None)
        self.assertEqual(library.check_by_initial_author(["a"]), None)
        self.assertEqual(library.check_by_initial_author(False), None)

    # corner case: symbol instead of character
    def test_corner_values_initial_author(self):
        """testing corner values for the function check_by_initial_author()"""
        self.assertEqual(library.check_by_initial_author("@"), [''])

    # smoke test: valid inputs
    def test_correct_values_initial_title(self):
        """testing correct values for the function check_by_initial_title()"""
        self.assertEqual(library.check_by_initial_title("z"), [
            'Zen & The Art of Motorcycle Maintenance'
            ])
        self.assertEqual(library.check_by_initial_title("T"), [
            'Half A Life',
            'Hidden Connections, The',
            'History of England, Foundation',
            'History of the DC Universe',
            'History of Western Philosophy',
            'How to Think Like Sherlock Holmes',
            'Hunchback of Notre Dame, The'
            ])
        self.assertEqual(library.check_by_initial_title("y"), [])
        self.assertFalse(library.check_by_initial_title("kek"))

    # invalid inputs
    def test_wrong_values_initial_title(self):
        """testing wrong values for the function check_by_initial_title()"""
        self.assertEqual(library.check_by_initial_title(""), None)
        self.assertEqual(library.check_by_initial_title(["b"]), None)
        self.assertEqual(library.check_by_initial_title(True), None)

    # corner case: symbol instead of character
    def test_corner_values_initial_title(self):
        """testing corner values for the function check_by_initial_title()"""
        self.assertEqual(library.check_by_initial_author("@"), [''])


if __name__ == '__main__':
    unittest.main(verbosity=2)
