from json import dumps
from typing import Any

def json_serializer(value: Any) -> bytes:
    return dumps(value, default=str).encode("utf-8")
