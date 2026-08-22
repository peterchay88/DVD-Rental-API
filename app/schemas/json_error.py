from typing import (
    TypeVar,
    Generic
)

from pydantic import (
    BaseModel,
    ConfigDict,
)
from pydantic.alias_generators import to_camel


T = TypeVar('T')

class JsonError(BaseModel, Generic[T]):

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )

    error: dict[str, T]