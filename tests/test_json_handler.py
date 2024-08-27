import unittest

from classes.json_handler import JsonHandler
from tests.constants_for_test import SAMPLE_INPUT_DATA, SAMPLE_INPUT_JSON


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
