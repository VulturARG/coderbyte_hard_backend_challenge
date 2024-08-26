from json import dumps, loads
from typing import Any


class JsonHandler:
    def to_json(self, data: list[dict[str, Any]]) -> str:
        return dumps(data, default=str)

    def from_json(self, data: str) -> list[dict[str, Any]]:
        return loads(data)
