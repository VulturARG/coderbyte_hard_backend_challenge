
import unittest
from classes.json_handler import JsonHandler
from test.constants_for_test import SAMPLE_CLEANED


class TestJsonHandler(unittest.TestCase):
    def setUp(self):
        self.handler = JsonHandler()

    def test_to_json(self):
        expected = '[{"Hobbies": ["reading", "swimming", "hiking", "swimming"], "age": 30, "affiliations": [], "city": "New York", "country": "USA", "favorite_foods": {"Breakfast": "pancakes", "dinner": "pasta"}, "friends": [{"age": 28, "city": "New York", "country": "USA", "name": "Jane"}, {"age": 32, "city": "London", "country": "UK", "name": "Tom", "occupation": "teacher"}], "gear": {}, "name": "John", "occupation": "programmer"}]'
        actual = self.handler.to_json(SAMPLE_CLEANED)
        self.assertEqual(expected, actual)

    def test_from_json(self):
        json_str = '[{"Hobbies": ["reading", "swimming", "hiking", "swimming"], "age": 30, "affiliations": [], "city": "New York", "country": "USA", "favorite_foods": {"Breakfast": "pancakes", "dinner": "pasta"}, "friends": [{"age": 28, "city": "New York", "country": "USA", "name": "Jane"}, {"age": 32, "city": "London", "country": "UK", "name": "Tom", "occupation": "teacher"}], "gear": {}, "name": "John", "occupation": "programmer"}]'
        expected = SAMPLE_CLEANED
        actual = self.handler.from_json(json_str)
        self.assertEqual(expected, actual)

