# solution_with_patterns/classes/cleaner.py
from typing import Any, Callable


class Cleaner:
    def clean(self, data):
        map_type = self._map_type()
        callable_type = map_type.get((isinstance(data, list), isinstance(data, dict)), self._is_any_type)
        return callable_type(data)

    def _map_type(self) -> dict[tuple[bool, bool], Callable]:
        return {
            (True, False): self._is_list_type,
            (False, True): self._is_dict_type,
        }

    def _is_list_type(self, data: list):
        cleaned_list = [self.clean(item) for item in data if item not in ([], {}, '', None)]
        cleaned_list = [item for item in cleaned_list if item not in ([], {})]
        return cleaned_list if cleaned_list else []

    def _is_dict_type(self, data: dict):
        cleaned_dict = {}
        for k, v in data.items():
            cleaned_value = self.clean(v)
            if cleaned_value not in ([], '', None):
                cleaned_dict[k] = cleaned_value
        return cleaned_dict if cleaned_dict else {}

    def _is_any_type(self, data: Any) -> Any:
        return data

