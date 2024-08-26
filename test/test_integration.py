from json import dumps
from unittest import TestCase
from unittest.mock import patch, MagicMock

from main import main
from test.constants_for_test import SAMPLE_INPUT_JSON, SAMPLE_FINAL_DATA, ORIGINAL_JSON_INPUT, ORIGINAL_OUTPUT


@patch('main.DataFetcher')
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
