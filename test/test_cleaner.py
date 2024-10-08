import unittest
from test.constants_for_test import SAMPLE_CLEANED, SAMPLE_DUPLICATE_REMOVED

from classes.cleaner import Cleaner


class TestCleaner(unittest.TestCase):
    def setUp(self):
        self.cleaner = Cleaner()

    def test_clean_list(self):
        data = [1, "", None, 2, [], {}, 3]
        expected = [1, 2, 3]
        actual = self.cleaner.clean(data)
        self.assertEqual(expected, actual)

    def test_clean_dict(self):
        data = {"a": 1, "b": "", "c": None, "d": [], "e": {}, "f": 2}
        expected = {"a": 1, "e": {}, "f": 2}
        actual = self.cleaner.clean(data)
        self.assertEqual(expected, actual)

    def test_clean_nested(self):
        data = {"a": [1, "", None], "b": {"c": "", "d": [2, None]}, "e": None}
        expected = {"a": [1], "b": {"d": [2]}}
        actual = self.cleaner.clean(data)
        self.assertEqual(expected, actual)

    def test_clean_sample_duplicate_removed(self):
        actual = self.cleaner.clean(SAMPLE_DUPLICATE_REMOVED)
        expected = SAMPLE_CLEANED
        self.assertEqual(expected, actual)

    def test_clean_empty_list(self):
        data = [{"name": "John", "affiliations": ["", "", ""]}]
        expected = [{"name": "John"}]
        actual = self.cleaner.clean(data)
        self.assertEqual(expected, actual)
