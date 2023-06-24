from datetime import datetime
from typing import Any

import orjson
import pendulum
from pydantic import BaseConfig, BaseModel


def orjson_dumps(v: Any, *, _: Any) -> str:
    def custom_serializer(obj: Any) -> datetime:
        if isinstance(obj, datetime):
            return pendulum.instance(obj)
        raise TypeError(
            f"Object of type '{type(obj).__name__}' is not JSON serializable"
        )

    return orjson.dumps(v, default=custom_serializer).decode()


def snake_to_camelcase(snake_case_txt: str) -> str:
    words = snake_case_txt.split("_")
    camel_case = words[0] + "".join(word.title() for word in words[1:])
    return camel_case


class BaseSchema(BaseModel):
    class Config(BaseConfig):
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        alias_generator = snake_to_camelcase
        allow_population_by_field_name = True
