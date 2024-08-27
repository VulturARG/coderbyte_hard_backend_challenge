
import unittest

from classes.json_handler import JsonHandler
from test.constants_for_test import SAMPLE_INPUT_JSON, SAMPLE_INPUT_DATA


class TestJsonHandler(unittest.TestCase):
    def setUp(self):
        self.handler = JsonHandler()

    def test_to_json(self):
        expected = SAMPLE_INPUT_JSON
        actual = self.handler.to_json(SAMPLE_INPUT_DATA)
        self.assertEqual(expected, actual)

    def test_from_json(self):
        json_str = SAMPLE_INPUT_JSON
        expected = SAMPLE_INPUT_DATA
        actual = self.handler.from_json(json_str)
        self.assertEqual(expected, actual)

