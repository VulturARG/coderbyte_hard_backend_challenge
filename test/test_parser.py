from test.constants_for_test import (
    ORIGINAL_INPUT,
    ORIGINAL_OUTPUT,
    SAMPLE_FINAL_DATA,
    SAMPLE_INPUT_DATA,
)
from unittest import TestCase

from main import parser


class TestParser(TestCase):
    def test_parser_sample_data(self):
        actual = parser(SAMPLE_INPUT_DATA)
        expected = SAMPLE_FINAL_DATA
        self.assertEqual(expected, actual)

    def test_parser_full_data(self):
        actual = parser(ORIGINAL_INPUT)
        expected = ORIGINAL_OUTPUT
        self.assertEqual(expected, actual)
