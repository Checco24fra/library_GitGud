import unittest
import sys
import os
import library

class TestStringInput(unittest.TestCase):
    # smoke test: valid inputs
    def test_correct_values_book(self):
        """testing correct values for books_by_author()"""
        self.assertEqual(library.books_by_author("Capra"), [
                                                            "Hidden Connections, The",
                                                            "Tao of Physics, The",
                                                            "Uncommon Wisdom"
                                                            ])
        self.assertEqual(library.books_by_author("Aczel"), ["Artist and the Mathematician, The"])
        self.assertFalse(library.books_by_author("Paniccia"))

    # invalid inputs: empty string
    def test_wrong_values_initial_author(self):
        """testing wrong values for the function check_by_initial_author()"""
        self.assertEqual(library.check_by_initial_author(""), None)

    #the other wrong types are dealt by the argparse

if __name__ == '__main__':
    unittest.main(verbosity=2)