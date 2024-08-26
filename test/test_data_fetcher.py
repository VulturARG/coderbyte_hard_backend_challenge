from unittest import TestCase
from unittest.mock import patch
from requests import exceptions

from classes.data_fetcher import DataFetcher


class TestDataFetcher(TestCase):

    @patch('classes.data_fetcher.get')
    def test_get_data_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}

        fetcher = DataFetcher("https://coderbyte.com/api/challenges/json/date-list")

        data = fetcher.get_data()

        self.assertEqual(data, {"key": "value"})
        mock_get.assert_called_once_with("https://coderbyte.com/api/challenges/json/date-list")

    @patch('classes.data_fetcher.get')
    def test_get_data_failure(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = exceptions.HTTPError

        fetcher = DataFetcher("https://coderbyte.com/api/challenges/json/date-list")

        with self.assertRaises(exceptions.HTTPError):
            fetcher.get_data()

        mock_get.assert_called_once_with("https://coderbyte.com/api/challenges/json/date-list")


