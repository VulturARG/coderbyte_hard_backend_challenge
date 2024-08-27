# solution_with_patterns/tests/test_duplicate_remover.py

import unittest
from classes.duplicate_remover import DuplicateRemover

from tests.constants_for_test import SAMPLE_DUPLICATE_REMOVED, SAMPLE_ORDERED_DATA


class TestDuplicateRemover(unittest.TestCase):
    def setUp(self):
        self.remover = DuplicateRemover()

    def test_remove_duplicates_simple_list(self):
        data = [1, 2, 2, 3, 4, 4]
        expected = [1, 2, 2, 3, 4, 4]
        actual = self.remover.remove_duplicates(data)
        self.assertEqual(expected, actual)

    def test_remove_duplicates_dicts_in_list(self):
        data = [{"a": 1}, {"a": 1}, {"b": 2}]
        expected = [{"a": 1}, {"b": 2}]
        actual = self.remover.remove_duplicates(data)
        self.assertEqual(expected, actual)

    def test_remove_duplicates_nested_dicts(self):
        data = [{"a": {"b": 2}}, {"a": {"b": 2}}, {"a": {"b": 3}}]
        expected = [{"a": {"b": 2}}, {"a": {"b": 3}}]
        actual = self.remover.remove_duplicates(data)
        self.assertEqual(expected, actual)

    def test_remove_duplicates_sample_ordered_data(self):
        actual = self.remover.remove_duplicates(SAMPLE_ORDERED_DATA)
        expected = SAMPLE_DUPLICATE_REMOVED
        self.assertEqual(expected, actual)


