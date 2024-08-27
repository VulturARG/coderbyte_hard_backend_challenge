from unittest import TestCase

from main import parser
from tests.constants_for_test import SAMPLE_INPUT_DATA, SAMPLE_FINAL_DATA, ORIGINAL_INPUT, ORIGINAL_OUTPUT


class TestParser(TestCase):
    def test_parser_sample_data(self):
        actual = parser(SAMPLE_INPUT_DATA)
        expected = SAMPLE_FINAL_DATA
        self.assertEqual(expected, actual)

    def test_parser_full_data(self):
        actual = parser(ORIGINAL_INPUT)
        expected = ORIGINAL_OUTPUT
        self.assertEqual(expected, actual)

