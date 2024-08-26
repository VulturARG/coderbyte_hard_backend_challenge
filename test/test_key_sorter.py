# solution_with_patterns/tests/test_key_sorter.py

import unittest
from classes.key_sorter import KeySorter
from test.constants_for_test import SAMPLE_ORDERED_DATA, SAMPLE_INPUT_DATA


class TestKeySorter(unittest.TestCase):
    def setUp(self):
        self.sorter = KeySorter()

    def test_sort_keys_dict(self):
        data = {"b": 1, "a": 2, "C": 3}
        expected = {"a": 2, "b": 1, "C": 3}
        actual = self.sorter.sort_keys(data)
        self.assertEqual(expected, actual)

    def test_sort_keys_nested_dict(self):
        data = {"b": {"d": 4, "c": 3}, "a": 2}
        expected = {"a": 2, "b": {"c": 3, "d": 4}}
        actual = self.sorter.sort_keys(data)
        self.assertEqual(expected, actual)

    def test_sort_keys_list_of_dicts(self):
        data = [{"b": 1, "a": 2}, {"C": 3, "B": 4}]
        expected = [{"a": 2, "b": 1}, {"B": 4, "C": 3}]
        actual = self.sorter.sort_keys(data)
        self.assertEqual(expected, actual)

    def test_sort_keys_mixed(self):
        data = {"z": [{"b": 1, "A": 2}, {"C": 3}], "a": {"B": 4, "c": 5}}
        expected = {"a": {"B": 4, "c": 5}, "z": [{"A": 2, "b": 1}, {"C": 3}]}
        actual = self.sorter.sort_keys(data)
        self.assertEqual(expected, actual)

    def test_sort_keys_realistic_data(self):
        data = SAMPLE_INPUT_DATA
        expected = SAMPLE_ORDERED_DATA
        actual = self.sorter.sort_keys(data)
        self.assertEqual(expected, actual)
