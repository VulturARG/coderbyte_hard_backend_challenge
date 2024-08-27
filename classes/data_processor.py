from abc import ABC, abstractmethod
from typing import Callable


class DataProcessor(ABC):

    def process(self, data):
        data_type_map = self._map_type()
        callable_type = data_type_map.get((isinstance(data, list), isinstance(data, dict)), self._process_default)
        return callable_type(data)

    def _map_type(self) -> dict[tuple[bool, bool], Callable]:
        return {
            (True, False): self._process_list,
            (False, True): self._process_dict,
        }

    @abstractmethod
    def _process_list(self, data):
        """Process data if data is a list."""

    @abstractmethod
    def _process_dict(self, data):
        """Process data if data is a dict."""

    def _process_default(self, data):
        """Process data if data is not a list or dict."""
        return data
