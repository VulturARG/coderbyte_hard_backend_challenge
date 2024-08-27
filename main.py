from typing import Any

from classes.cleaner import Cleaner
from classes.data_fetcher import DataFetcher
from classes.duplicate_remover import DuplicateRemover
from classes.json_handler import JsonHandler
from classes.key_sorter import KeySorter


def gateway() -> str:
    # The result of this request changes. It originally returned the data that was in the ORIGINAL_JSON_INPUT variable
    data_fetcher = DataFetcher("https://coderbyte.com/api/challenges/json/date-list")
    return data_fetcher.get_data()


def parser(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    key_sorter = KeySorter()
    sorted_data = key_sorter.sort_keys(data)

    duplicate_remover = DuplicateRemover()
    unique_data = duplicate_remover.remove_duplicates(sorted_data)

    cleaner = Cleaner()
    return cleaner.process(unique_data)


def main() -> str:
    json_handler = JsonHandler()

    json_data = gateway()
    data = json_handler.from_json(json_data)
    cleaned_data = parser(data)
    return json_handler.to_json(cleaned_data)


if __name__ == "__main__":
    print(main())
