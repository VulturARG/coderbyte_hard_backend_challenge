from json import dumps
from unittest import TestCase
from unittest.mock import MagicMock, patch

from main import main
from tests.constants_for_test import (
    ORIGINAL_JSON_INPUT,
    ORIGINAL_OUTPUT,
    SAMPLE_FINAL_DATA,
    SAMPLE_INPUT_JSON,
)


@patch("main.DataFetcher")
class TestIntegration(TestCase):
    def test_integration_sample_data(self, mock_data_fetcher: MagicMock):
        expected = dumps(SAMPLE_FINAL_DATA)
        mock_data_fetcher.return_value.get_data.return_value = SAMPLE_INPUT_JSON

        actual = main()
        self.assertEqual(expected, actual)

    def test_integration_full_data(self, mock_data_fetcher: MagicMock):
        expected = dumps(ORIGINAL_OUTPUT)
        mock_data_fetcher.return_value.get_data.return_value = ORIGINAL_JSON_INPUT

        actual = main()
        self.assertEqual(expected, actual)
