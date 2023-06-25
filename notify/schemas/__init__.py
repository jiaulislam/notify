from datetime import datetime
from typing import Any, Mapping
from zoneinfo import ZoneInfo

import orjson
from fastapi.encoders import jsonable_encoder
from pydantic import BaseConfig, BaseModel, root_validator


def orjson_dumps(v: Any, *, default: Any) -> str:
    return orjson.dumps(v, default=default).decode()


def convert_datetime_to_gmt(dt: datetime) -> str:
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=ZoneInfo("UTC"))

    return dt.strftime("%Y-%m-%dT%H:%M:%S%z")


def snake_to_camelcase(snake_case_txt: str) -> str:
    words = snake_case_txt.split("_")
    camel_case = words[0] + "".join(word.title() for word in words[1:])
    return camel_case


class BaseSchema(BaseModel):
    class Config(BaseConfig):
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        json_encoders = {datetime: convert_datetime_to_gmt}
        alias_generator = snake_to_camelcase
        allow_population_by_field_name = True

        @root_validator()
        def set_null_microseconds(cls, data: Mapping[str, Any]) -> Mapping[str, Any]:
            """Drops microseconds in all the datetime field values."""
            datetime_fields = {
                k: v.replace(microsecond=0)
                for k, v in data.items()
                if isinstance(k, datetime)
            }

            return {**data, **datetime_fields}

        def serializable_dict(self, **kwargs: Any):
            """Return a dict which contains only serializable fields."""
            default_dict = super().dict(**kwargs)  # type: ignore

            return jsonable_encoder(default_dict)
