from unittest import TestCase

from tests.tests_doubles.mock_processor import MockProcessor


class TestDataProcessor(TestCase):
    def setUp(self):
        self.processor = MockProcessor()

    def test_process_list(self):
        expected = ["processed_list"]
        actual = self.processor.process([1, 2, 3])
        self.assertEqual(expected, actual)

    def test_process_dict(self):
        expected = {"processed_dict": "processed"}
        actual = self.processor.process({"key": "value"})
        self.assertEqual(expected, actual)

    def test_process_default(self):
        expected = "default_processed"
        actual = self.processor.process("some_string")
        self.assertEqual(expected, actual)
